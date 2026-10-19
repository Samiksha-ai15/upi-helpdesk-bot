import json
import re
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Find the project folder
base_path = Path(__file__).resolve().parent.parent
faq_file = base_path / "data" / "faqs.json"


# Load FAQ data
with open(faq_file, "r", encoding="utf-8") as file:
    faqs = json.load(file)


# Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


# Store FAQ information
questions = []
answers = []
categories = []
matched_questions = []


# Prepare FAQ data
for faq in faqs:

    questions.append(clean_text(faq["question"]))
    answers.append(faq["answer"])
    categories.append(faq["category"])
    matched_questions.append(faq["question"])

    # Add variations
    for variation in faq.get("variations", []):
        questions.append(clean_text(variation))
        answers.append(faq["answer"])
        categories.append(faq["category"])
        matched_questions.append(faq["question"])


# Convert questions into TF-IDF vectors
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)


# --------------------------------------------------
# FIND BEST MATCH
# --------------------------------------------------

def get_match(user_question):

    user_question = clean_text(user_question)

    user_vector = vectorizer.transform([user_question])

    similarity = cosine_similarity(
        user_vector,
        question_vectors
    )

    best_match = similarity.argmax()
    best_score = similarity[0][best_match]

    # Low similarity
    if best_score < 0.25:

        return {
            "answer": "Sorry, I could not find a suitable answer to your question.",
            "category": "Unknown",
            "score": best_score,
            "matched_question": "No suitable FAQ found",
            "related_questions": []
        }

    # Find related questions
    related_indexes = similarity[0].argsort()[::-1]

    related_questions = []

    for index in related_indexes:

        question = matched_questions[index]

        # Don't show the same matched FAQ
        if question == matched_questions[best_match]:
            continue

        if question not in related_questions:
            related_questions.append(question)

        if len(related_questions) == 3:
            break

    return {
        "answer": answers[best_match],
        "category": categories[best_match],
        "score": best_score,
        "matched_question": matched_questions[best_match],
        "related_questions": related_questions
    }


# Keep old function
def get_answer(user_question):

    result = get_match(user_question)

    return result["answer"]


# Test matcher directly
if __name__ == "__main__":

    print("UPI Assist - AI FAQ Matcher")
    print("Type 'exit' to stop.")

    while True:

        user_question = input("\nYou: ")

        if user_question.lower() == "exit":

            print("Chatbot: Goodbye!")

            break

        result = get_match(user_question)

        print("\nCategory:", result["category"])

        print(
            "Match Score:",
            round(result["score"] * 100, 2),
            "%"
        )

        print(
            "Matched FAQ:",
            result["matched_question"]
        )

        print(
            "Answer:",
            result["answer"]
        )

        print("\nRelated Questions:")

        for question in result["related_questions"]:
            print("-", question)