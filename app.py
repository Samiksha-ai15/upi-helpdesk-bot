import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import streamlit as st
from src.matcher import get_match


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="UPI Assist",
    page_icon="💳",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

/* Main title */
.main-title {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 4px;
    color: #2563eb;
    letter-spacing: -1px;
}

/* Subtitle */
.subtitle {
    font-size: 17px;
    color: #64748b;
    margin-top: 0px;
    margin-bottom: 20px;
}

/* Welcome box */
.welcome-box {
    padding: 28px;
    border-radius: 18px;
    border: 1px solid #dbeafe;
    background: linear-gradient(
        135deg,
        rgba(219, 234, 254, 0.45),
        rgba(255, 255, 255, 0.8)
    );
    margin-top: 20px;
    margin-bottom: 25px;
}

/* Section headings */
h2, h3 {
    font-weight: 700;
}

/* Buttons */
.stButton > button {
    border-radius: 10px;
    min-height: 42px;
    font-weight: 600;
    transition: all 0.2s ease;
}

/* Button hover effect */
.stButton > button:hover {
    border-color: #2563eb;
    color: #2563eb;
}

/* Chat input */
.stChatInput textarea {
    border-radius: 12px;
}

/* Uploaded image */
[data-testid="stImage"] {
    border-radius: 12px;
    overflow: hidden;
}

/* Responsive title for smaller screens */
@media (max-width: 768px) {
    .main-title {
        font-size: 32px;
    }

    .subtitle {
        font-size: 15px;
    }

    .welcome-box {
        padding: 18px;
    }
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:
    st.title("💳 UPI Assist")
    st.write("### Help Center")
    st.write("Get quick answers to common UPI payment questions.")

    st.divider()

    st.write("### 📚 Categories")
    st.write("💰 Payments")
    st.write("🔄 Refunds")
    st.write("🔐 UPI PIN")
    st.write("🏦 Bank Issues")
    st.write("🛡️ Security")

    st.divider()

    if st.button("🧹 Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.caption("UPI Assist • AI-powered FAQ Support")


# --------------------------------------------------
# MAIN HEADER
# --------------------------------------------------

# --------------------------------------------------
# MAIN HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">💳 UPI Assist</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Intelligent UPI Payment Support System</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# UPI PAYMENT SCREENSHOT ANALYZER
# ----------------------------------------yes----------

st.divider()

st.header("📸 UPI Payment Screenshot Analyzer")

st.write(
    "Upload a UPI payment screenshot to extract "
    "visible payment details."
)

uploaded_file = st.file_uploader(
    "Upload your payment screenshot",
    type=["png", "jpg", "jpeg"],
    key="upi_screenshot"
)

if uploaded_file is not None:

    from PIL import Image

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Payment Screenshot",
        use_container_width=True
    )

    if st.button("🔍 Extract Text", key="extract_upi_text"):

        try:
            extracted_text = pytesseract.image_to_string(image)

            st.session_state["screenshot_text"] = extracted_text
            st.session_state["screenshot_available"] = True

            st.subheader("📝 Extracted Text")

                                    # 🔍 Detect likely payment status
            text_lower = extracted_text.lower()

            if "pending" in text_lower:
                st.warning("🟡 Likely Payment Status: PENDING")

                st.markdown("### 💡 Recommended Actions")
                st.write("1. Open your UPI app and check transaction history.")
                st.write("2. Check your bank account for the latest transaction status.")
                st.write("3. Avoid repeating the payment while its status is uncertain.")
                st.write("4. If the issue continues, contact your UPI app or bank support.")

            elif "failed" in text_lower:
                st.error("🔴 Likely Payment Status: FAILED")

                st.markdown("### 💡 Recommended Actions")
                st.write("1. Check whether money was deducted from your bank account.")
                st.write("2. Check the transaction status in your UPI app.")
                st.write("3. If money was deducted, follow your bank's refund or dispute process.")
                st.write("4. Avoid paying again until you confirm the first transaction's status.")

            elif (
                "successful" in text_lower
                or "completed" in text_lower
            ):
                st.success("🟢 Likely Payment Status: SUCCESSFUL")

                st.markdown("### 💡 Recommended Actions")
                st.write("1. Check your bank statement and transaction details.")
                st.write("2. If the receiver has not received the money, ask them to check their account.")
                st.write("3. If the issue continues, contact your UPI app or bank support.")

            else:
                st.info("ℹ️ Payment status could not be identified from the extracted text.")
                st.write("💡 Try uploading a clearer screenshot showing the payment status.")

            if extracted_text.strip():

                st.text_area(
                    "Text found in your screenshot",
                    extracted_text,
                    height=200
                )

                st.info(
                    "This text was extracted from your image. "
                    "It does not independently verify your transaction."
                )

            else:
                st.warning(
                    "No text was detected. Try a clearer screenshot."
                )

        except Exception as e:
            st.error(f"Could not extract text: {e}")


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# WELCOME MESSAGE + QUICK QUESTIONS
# --------------------------------------------------

if len(st.session_state.messages) == 0:

    st.markdown("""
    <div class="welcome-box">

    <h3>👋 Welcome to UPI Assist</h3>

    <p>
    Ask questions about UPI payments, failed transactions,
    refunds, UPI PINs, bank issues and payment security.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("### ⚡ Quick Questions")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "❌ Why did my UPI payment fail?",
            use_container_width=True
        ):

            st.session_state.quick_question = (
                "Why did my UPI payment fail?"
            )

            st.rerun()

        if st.button(
            "💰 Money deducted but payment failed",
            use_container_width=True
        ):

            st.session_state.quick_question = (
                "Money was deducted but my UPI payment failed"
            )

            st.rerun()

    with col2:

        if st.button(
            "🔄 Where is my UPI refund?",
            use_container_width=True
        ):

            st.session_state.quick_question = (
                "Where is my UPI refund?"
            )

            st.rerun()

        if st.button(
            "🔐 How can I keep my UPI account safe?",
            use_container_width=True
        ):

            st.session_state.quick_question = (
                "How can I keep my UPI account safe?"
            )

            st.rerun()


# --------------------------------------------------
# DISPLAY CHAT HISTORY
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        if message["role"] == "user":

            st.write(message["content"])

        else:

            result = message["content"]

            st.markdown("### 🤖 UPI Assist")

            # Category and match score

            col1, col2 = st.columns(2)

            with col1:

                st.info(
                    f"🏷️ Category\n\n"
                    f"**{result['category']}**"
                )

            with col2:

                st.success(
                    f"📊 Match Score\n\n"
                    f"**{result['score'] * 100:.2f}%**"
                )

            # Matched FAQ

            st.markdown("#### 🔎 Matched FAQ")

            st.write(result["matched_question"])

            # Answer

            st.markdown("#### 💡 Answer")

            st.write(result["answer"])

            # Related questions

            if result["related_questions"]:

                st.markdown(
                    "#### 🔗 You may also want to ask"
                )

                for question in result["related_questions"]:

                    st.write("•", question)


# --------------------------------------------------
# CHAT INPUT
# --------------------------------------------------

user_question = st.chat_input(
    "💬 Type your UPI question..."
)


# --------------------------------------------------
# QUICK QUESTION HANDLING
# --------------------------------------------------

if "quick_question" in st.session_state:

    user_question = st.session_state.quick_question

    del st.session_state.quick_question


# --------------------------------------------------
# PROCESS USER QUESTION
# --------------------------------------------------

if user_question and user_question.strip():

    # Save user question
    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    # Get previous conversation context
    previous_question = ""

    for message in reversed(st.session_state.messages[:-1]):
        if message["role"] == "user":
            previous_question = message["content"]
            break

    # Add previous context for short follow-up questions
    follow_up_words = [
        "what should i do",
        "what now",
        "how long",
        "why",
        "how",
        "when",
        "can i",
        "what about",
        "tell me more",
        "and then"
    ]

    question_lower = user_question.lower().strip()

    if previous_question and any(
        word in question_lower for word in follow_up_words
    ):
        question_for_matcher = (
            previous_question + " " + user_question
        )
    else:
        question_for_matcher = user_question

    # Add screenshot payment status when available
    screenshot_text = st.session_state.get("screenshot_text", "")

    if screenshot_text:
        text_lower = screenshot_text.lower()

        if "failed" in text_lower:
            question_for_matcher += " UPI payment failed"

        elif "pending" in text_lower:
            question_for_matcher += " UPI payment pending"

        elif "successful" in text_lower or "completed" in text_lower:
            question_for_matcher += " UPI payment successful"

    # Get AI result
    result = get_match(question_for_matcher)

    # Save AI result
    st.session_state.messages.append({
        "role": "assistant",
        "content": result
    })

    # Refresh the page
    st.rerun()