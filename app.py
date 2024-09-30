from flask import Flask, render_template, request
import fitz
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet
from collections import defaultdict

import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')

app = Flask(__name__)

def tokenize(text):
    sentences = sent_tokenize(text)
    words = [word_tokenize(sentence) for sentence in sentences]
    return words

def create_concordance(pdf_file_path):
    concordance = defaultdict(list)

    doc = fitz.open(pdf_file_path)

    for page_number in range(doc.page_count):
        page = doc.load_page(page_number)
        page_text = page.get_text()
        words = [word.lower() for word in re.findall(r'\b\w+\b', page_text)]

        for word in words:
            concordance[word].append(page_number + 1)

    doc.close()

    return concordance

def get_word_definition(word):
    synsets = wordnet.synsets(word)
    if synsets:
        definition = synsets[0].definition()
        return definition
    return None

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form['search_term']
        if search_term in concordance:
            occurrences = []
            for page_number in concordance[search_term]:
                definition = get_word_definition(search_term)
                occurrences.append((page_number, search_term, definition))
            return render_template('results.html', occurrences=occurrences)
        else:
            return render_template('results.html', message=f"'{search_term}' not found in the PDF.",
                                   concordance_link='/concordance')
    return render_template('index.html')

@app.route('/concordance')
def show_concordance():
    output_text = ""
    for word, page_numbers in concordance.items():
        definition = get_word_definition(word)
        output_text += f"Word: {word}\n"
        output_text += f"Definition: {definition}\n"
        output_text += f"Page Numbers: {', '.join(map(str, page_numbers))}\n"
        output_text += "------\n"
    return render_template('concordance.html', output_text=output_text)

if __name__ == '__main__':
    pdf_file_path = r"C:\Users\GULFAM MALIK\Desktop\Enoch\Enoch.pdf"  # Replace with the correct file path
    concordance = create_concordance(pdf_file_path)
    app.run()