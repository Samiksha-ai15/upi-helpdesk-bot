<div align="center">

# 💳 UPI Assist
### Intelligent UPI Payment Support System

An AI-powered support assistant for understanding UPI payment issues through intelligent FAQ matching and screenshot text analysis.

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-TF--IDF-orange?style=for-the-badge)
![OCR](https://img.shields.io/badge/OCR-Tesseract-blue?style=for-the-badge)

</div>

---

## 📌 Overview

**UPI Assist** is an intelligent payment-support application designed to help users understand and troubleshoot common Unified Payments Interface (UPI) payment issues.

The application combines text-based FAQ matching with Optical Character Recognition (OCR) to provide relevant answers to user queries and analyze text extracted from payment screenshots.

Built with Python and Streamlit, the project demonstrates practical applications of Natural Language Processing (NLP), text similarity techniques, OCR, and interactive web application development.

## ✨ Key Features

- **Intelligent FAQ Matching:** Matches user queries with relevant questions from a predefined FAQ dataset.
- **NLP-Based Text Processing:** Uses TF-IDF vectorization and cosine similarity to identify relevant FAQ entries.
- **Interactive Chat Interface:** Provides a conversational interface for UPI-related support.
- **Screenshot Text Extraction:** Extracts readable text from uploaded payment screenshots using OCR.
- **Payment Status Analysis:** Uses extracted text and keyword-based logic to identify possible successful, failed, or pending payment statuses.
- **Troubleshooting Guidance:** Provides suggestions for common payment-related issues.
- **Streamlit Web Interface:** Offers an accessible interface for interacting with the application's features.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| Streamlit | Interactive web application |
| Scikit-learn | Text vectorization and similarity calculation |
| TF-IDF | Text representation for FAQ matching |
| Cosine Similarity | Finding relevant FAQ entries |
| Pytesseract | Python interface for OCR |
| Tesseract OCR | Extracting text from images |
| Pillow | Image handling and processing |
| JSON | Storing FAQ data |

## ⚙️ How It Works

### 1. FAQ Chatbot

1. The user enters a UPI-related question.
2. The application preprocesses the text.
3. TF-IDF represents the text numerically.
4. Cosine similarity compares the query with available FAQ questions.
5. The application identifies a relevant FAQ and returns its answer when a suitable match is found.

### 2. Payment Screenshot Analyzer

1. The user uploads a payment screenshot.
2. OCR extracts the text from the image.
3. The application analyzes the extracted text using keyword-based rules.
4. A possible payment status is identified.
5. Relevant guidance is displayed to the user.

> **Important:** Screenshot analysis is based on extracted text and predefined rules. It does not independently verify transactions with a bank or UPI service.

## 🏗️ Project Structure

```text
upi-helpdesk-bot/
│
├── app.py                  # Streamlit application
│
├── data/
│   └── faqs.json           # FAQ dataset
│
├── src/
│   ├── matcher.py          # FAQ matching logic
│   └── preprocess.py       # Text preprocessing
│
├── requirements.txt        # Python dependencies
├── .gitignore              # Git exclusions
└── README.md               # Project documentation
