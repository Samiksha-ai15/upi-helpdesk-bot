import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK data (only runs once, then it's cached)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    """Lowercase and remove everything except letters and spaces."""
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

def preprocess(text):
    """
    Full preprocessing pipeline:
    1. Clean the text (lowercase, remove punctuation/numbers)
    2. Tokenize (split into words)
    3. Remove stopwords (common words like 'the', 'is', 'a')
    4. Lemmatize (reduce words to their base form, e.g. 'deducted' -> 'deduct')
    """
    cleaned = clean_text(text)
    tokens = nltk.word_tokenize(cleaned)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return " ".join(tokens)

# Quick test — only runs if you execute this file directly
if __name__ == "__main__":
    test_sentences = [
        "Why did my UPI payment fail?",
        "Money deducted but not received!!",
        "My money got cut but the transaction failed"
    ]
    for sentence in test_sentences:
        print(f"Original:    {sentence}")
        print(f"Preprocessed: {preprocess(sentence)}")
        print()