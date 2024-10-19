# expense_tracker.py
import streamlit as st
import pandas as pd
from datetime import datetime
from layout import feedback_form
from helpers import load_data, save_data

feedback_form()

st.title("🧾 Expense Tracker")
st.markdown("Log your expenses and track where your money goes.")

# Load expenses DataFrame from CSV
if 'expenses' not in st.session_state:
    st.session_state['expenses'] = load_data('expenses.csv', ['Date', 'Category', 'Amount', 'Description'])

with st.form("Add Expense"):
    date = st.date_input("Date", datetime.today())
    category_options = st.session_state.get('budgets', pd.DataFrame({'Category': []}))['Category'].unique()
    category = st.selectbox("Category", options=category_options if len(category_options) > 0 else ['Miscellaneous'])
    amount = st.number_input("Amount ($)", min_value=0.0, step=1.0)
    description = st.text_area("Description")
    submitted = st.form_submit_button("Add Expense")

if submitted:
    new_row = {'Date': date, 'Category': category, 'Amount': amount, 'Description': description}
    st.session_state['expenses'] = pd.concat([st.session_state['expenses'], pd.DataFrame([new_row])], ignore_index=True)
    save_data(st.session_state['expenses'], 'expenses.csv')
    st.success("Expense added!")
    st.session_state['total_expenses'] = st.session_state['expenses']['Amount'].sum()

# Display Expenses
st.subheader("Your Expenses")
if not st.session_state['expenses'].empty:
    st.dataframe(st.session_state['expenses'])
else:
    st.write("No expenses recorded yet.")
