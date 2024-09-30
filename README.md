# PDF_Concordance_App

This project is a PDF Concordance Generator built with Flask and Python. It extracts words from a PDF and creates a concordance, showing the pages where each word appears. Users can search for words and view their occurrences and definitions using NLTK, with results displayed in a simple web interface.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Usage](#usage)
- [How to Upload a PDF](#how-to-upload-a-pdf)
- [How to Search](#how-to-search)
- [Contributing](#contributing)
- [License](#license)

## Features
- Generate a concordance for any PDF file.
- Search for specific words in the PDF and get page references.
- Displays word definitions using the NLTK library.
- Easy-to-use Flask web interface.

## Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.x
- Flask
- PyMuPDF (for PDF handling)
- NLTK (Natural Language Toolkit)

You can install them by running:
```bash
pip install Flask
pip install PyMuPDF
pip install nltk
```

## Installation
1. Clone this repository:
```bash
git clone https://github.com/yourusername/PDF_Concordance_App.git
```
2. Navigate into the project directory:
```bash
cd PDF_Concordance_App
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```


## How to Run
1. Make sure you have a PDF file ready for concordance.
2. Open the `app.py` file and replace the `pdf_file_path` with the path to your PDF:
```
pdf_file_path = r"your\path\to\pdf\file.pdf"
```
Start the Flask server:
```
python app.py
```
Open your browser and go to http://127.0.0.1:5000/ to access the app.
4. Usage
1. How to Upload a PDF
Currently, the PDF file path is hardcoded in the app.py file. Modify the pdf_file_path variable to point to the desired PDF before running the app.

2. How to Search
Go to the main page at http://127.0.0.1:5000/.
3. Enter a word in the search bar.
The results page will show:
The pages where the word appears.
The word definition (if available via NLTK).
Viewing the Entire Concordance
To view the full concordance, go to the /concordance route:

```
http://127.0.0.1:5000/concordance
```
This page lists all the words in the PDF, their definitions, and the page numbers where they occur.
