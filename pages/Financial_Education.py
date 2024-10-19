# pages/financial_education.py
import streamlit as st
import random
from layout import feedback_form

feedback_form()

def main():
    st.title("📚 Financial Education")
    st.markdown("Enhance your financial knowledge.")

    st.header("📝 Interactive Flashcards")

    flashcards_data = [
        {"term": "Budget", "definition": "A plan for how to spend and save money."},
        {"term": "Savings Account", "definition": "A bank account that earns interest on the money deposited."},
        {"term": "Interest", "definition": "The cost of borrowing money or the reward for saving money."},
        {"term": "Investment", "definition": "Putting money into something with the expectation of earning a profit."},
        {"term": "Credit Score", "definition": "A number representing the creditworthiness of a person."},
        {"term": "Debt", "definition": "Money owed to another person or institution."},
        {"term": "Income", "definition": "Money received, especially on a regular basis, for work or through investments."},
        {"term": "Expense", "definition": "Money spent on goods and services."},
        {"term": "Compound Interest", "definition": "Interest calculated on the initial principal and also on the accumulated interest of previous periods."},
        {"term": "Asset", "definition": "Anything valuable that an individual or business owns."},
        {"term": "Liability", "definition": "A financial obligation or amount owed."},
        {"term": "Net Worth", "definition": "The difference between assets and liabilities."},
        {"term": "Stock", "definition": "A share of ownership in a company."},
        {"term": "Bond", "definition": "A fixed income investment representing a loan made by an investor to a borrower."},
        {"term": "Diversification", "definition": "Investing in a variety of assets to reduce risk."},
        {"term": "Inflation", "definition": "The rate at which the general level of prices for goods and services is rising."},
        {"term": "Gross Income", "definition": "Total income earned before taxes and other deductions."},
        {"term": "Net Income", "definition": "Income remaining after taxes and deductions."},
        {"term": "Liquidity", "definition": "How easily assets can be converted into cash."},
        {"term": "Retirement Account", "definition": "An account such as an IRA or 401(k) used to save for retirement."},
    ]

    if 'flashcards' not in st.session_state:
        st.session_state.flashcards = flashcards_data.copy()
        random.shuffle(st.session_state.flashcards)
        st.session_state.flashcard_index = 0
        st.session_state.show_definition = False

    current_flashcard = st.session_state.flashcards[st.session_state.flashcard_index]

    st.subheader(f"Flashcard {st.session_state.flashcard_index + 1} of {len(st.session_state.flashcards)}")

    card_style = """
    <style>
    .flashcard {
        background-color: #fff;
        padding: 50px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        text-align: center;
        font-size: 24px;
        margin-bottom: 20px;
    }
    .definition {
        background-color: #f0f0f0;
        padding: 30px;
        border-radius: 10px;
        font-size: 20px;
        margin-top: -20px;
    }
    </style>
    """
    st.markdown(card_style, unsafe_allow_html=True)

    st.markdown(f"<div class='flashcard'>{current_flashcard['term']}</div>", unsafe_allow_html=True)

    if st.session_state.show_definition:
        st.markdown(f"<div class='definition'>{current_flashcard['definition']}</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2, 2.5, .5])

    with col1:
        if st.button("Previous"):
            if st.session_state.flashcard_index > 0:
                st.session_state.flashcard_index -= 1
                st.session_state.show_definition = False
            else:
                st.warning("This is the first flashcard.")

    with col2:
        show_button = st.button("Show Definition")
        if show_button:
            st.session_state.show_definition = True

    with col3:
        if st.button("Next"):
            if st.session_state.flashcard_index < len(st.session_state.flashcards) - 1:
                st.session_state.flashcard_index += 1
                st.session_state.show_definition = False
            else:
                st.success("You've reached the end of the flashcards.")

    st.divider()

    # Quizzes Section
    st.header("🧠 Financial Quiz")

    quiz_data = [
        {"question": "What is a budget?", "options": ["A list of expenses", "A plan for spending and saving money", "An investment account"], "answer": "A plan for spending and saving money"},
        {"question": "Which of the following is a fixed income investment?", "options": ["Stock", "Bond", "Savings Account"], "answer": "Bond"},
        {"question": "What is a credit score used for?", "options": ["To determine how much you earn", "To represent your creditworthiness", "To calculate taxes"], "answer": "To represent your creditworthiness"},
        {"question": "What is the difference between gross income and net income?", "options": ["Gross income includes taxes; net income does not", "Net income is before taxes; gross income is after taxes", "Gross income is before taxes and deductions; net income is after"], "answer": "Gross income is before taxes and deductions; net income is after"},
        {"question": "What is an asset?", "options": ["A financial obligation", "Something valuable owned by a person or business", "Money owed to someone"], "answer": "Something valuable owned by a person or business"},
        {"question": "What is diversification?", "options": ["Investing in a single asset", "Spreading investments across different assets", "Saving all money in a savings account"], "answer": "Spreading investments across different assets"},
        {"question": "What is the purpose of a savings account?", "options": ["To store money and earn interest", "To borrow money", "To invest in stocks"], "answer": "To store money and earn interest"},
        {"question": "What is a bond?", "options": ["A loan made by an investor to a borrower", "A type of stock", "A savings account"], "answer": "A loan made by an investor to a borrower"},
        {"question": "What does inflation refer to?", "options": ["The rise in the general price level of goods and services", "An increase in interest rates", "A decrease in the value of investments"], "answer": "The rise in the general price level of goods and services"},
        {"question": "What is net worth?", "options": ["The value of all assets minus liabilities", "Total earnings in a year", "The total value of a person's investments"], "answer": "The value of all assets minus liabilities"},
        {"question": "What is liquidity?", "options": ["The ease of converting assets into cash", "The value of an investment over time", "A type of investment strategy"], "answer": "The ease of converting assets into cash"},
        {"question": "What is a retirement account?", "options": ["An account used to save for retirement, like an IRA", "A regular savings account", "An account for borrowing money"], "answer": "An account used to save for retirement, like an IRA"},
        {"question": "What is interest?", "options": ["A fee for borrowing money or a reward for saving money", "The value of an asset", "A form of tax"], "answer": "A fee for borrowing money or a reward for saving money"},
        {"question": "What is debt?", "options": ["Money you owe to another person or institution", "Money earned from an investment", "A type of investment account"], "answer": "Money you owe to another person or institution"},
        {"question": "What is a stock?", "options": ["A share of ownership in a company", "A type of loan", "A financial obligation"], "answer": "A share of ownership in a company"},
        {"question": "What is compound interest?", "options": ["Interest calculated on both principal and accumulated interest", "Interest on the initial principal only", "The return from selling stocks"], "answer": "Interest calculated on both principal and accumulated interest"},
        {"question": "What is an expense?", "options": ["Money spent on goods and services", "Money received for investments", "An amount saved"], "answer": "Money spent on goods and services"},
        {"question": "What is income?", "options": ["Money received for work or investments", "Money spent on goods and services", "Assets owned by a person"], "answer": "Money received for work or investments"},
        {"question": "What does a financial liability mean?", "options": ["A financial obligation or amount owed", "An asset that increases in value", "A type of investment"], "answer": "A financial obligation or amount owed"},
        {"question": "What is gross income?", "options": ["Total income before taxes and deductions", "Income after taxes", "Earnings from investments"], "answer": "Total income before taxes and deductions"},
    ]

    if 'quiz_questions' not in st.session_state:
        st.session_state.quiz_questions = random.sample(quiz_data, 5)
        st.session_state.quiz_index = 0
        st.session_state.quiz_score = 0
        st.session_state.quiz_completed = False

    if not st.session_state.quiz_completed:
        current_quiz = st.session_state.quiz_questions[st.session_state.quiz_index]
        st.subheader(f"Question {st.session_state.quiz_index + 1} of {len(st.session_state.quiz_questions)}")
        st.write(current_quiz["question"])
        user_answer = st.radio("Select an answer:", current_quiz["options"])

        if st.button("Submit Answer"):
            if user_answer == current_quiz["answer"]:
                st.success("Correct!")
                st.session_state.quiz_score += 1
            else:
                st.error(f"Incorrect. The correct answer is: {current_quiz['answer']}")

            if st.session_state.quiz_index < len(st.session_state.quiz_questions) - 1:
                st.session_state.quiz_index += 1
            else:
                st.session_state.quiz_completed = True

    if st.session_state.quiz_completed:
        st.subheader("Quiz Completed!")
        st.write(f"Your score: {st.session_state.quiz_score} out of {len(st.session_state.quiz_questions)}")
        if st.button("Restart Quiz"):
            st.session_state.quiz_questions = random.sample(quiz_data, 5)
            st.session_state.quiz_index = 0
            st.session_state.quiz_score = 0
            st.session_state.quiz_completed = False

if __name__ == "__main__":
    main()
