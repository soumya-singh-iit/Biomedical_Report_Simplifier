# Biomedical Report Simplifier

## Overview

Biomedical Report Simplifier is a Python-based web application that converts complex medical and biomedical terminology into simple, patient-friendly language. The application helps users understand medical reports more easily by replacing difficult medical terms with plain English explanations.

## Features

* Upload medical reports in PDF format
* Extract text automatically from uploaded reports
* Detect common biomedical and medical terms
* Convert complex terms into simple English
* View original and simplified reports side-by-side
* Download the simplified report
* Display statistics such as word count and terms detected

## Technologies Used

* Python
* Streamlit
* PyPDF2
* spaCy
* Natural Language Processing (NLP)

## How It Works

1. Upload a PDF medical report or paste medical text.
2. The application extracts the text.
3. Medical terms are identified using a biomedical dictionary.
4. Complex terms are replaced with patient-friendly explanations.
5. The simplified report is displayed and can be downloaded.

## Installation

Install the required packages:

pip install -r requirements.txt

Run the application:

streamlit run app.py

## Example

Input:

"The patient was diagnosed with hypertension and tachycardia."

Output:

"The patient was diagnosed with high blood pressure and fast heart rate."

## Future Improvements

* AI-generated report summaries
* Hindi language support
* Medical term categorization
* Advanced biomedical NLP models
* Export simplified reports as PDF

## Author

Soumya Singh
