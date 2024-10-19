# reports.py
import streamlit as st
import pandas as pd
from layout import feedback_form

feedback_form()

st.title("📊 Reports")
st.markdown("Download your financial data as CSV files.")

def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

# Budget Data Download
if 'budgets' in st.session_state and not st.session_state['budgets'].empty:
    st.subheader("Download Budget Data")
    budget_csv = convert_df_to_csv(st.session_state['budgets'])
    st.download_button(
        label="Download Budgets as CSV",
        data=budget_csv,
        file_name="budgets.csv",
        mime="text/csv"
    )
else:
    st.write("No budget data available.")

if 'expenses' in st.session_state and not st.session_state['expenses'].empty:
    st.subheader("Download Expense Data")
    expense_csv = convert_df_to_csv(st.session_state['expenses'])
    st.download_button(
        label="Download Expenses as CSV",
        data=expense_csv,
        file_name="expenses.csv",
        mime="text/csv"
    )
else:
    st.write("No expense data available.")

if 'savings_goals' in st.session_state and not st.session_state['savings_goals'].empty:
    st.subheader("Download Savings Goals Data")
    savings_csv = convert_df_to_csv(st.session_state['savings_goals'])
    st.download_button(
        label="Download Savings Goals as CSV",
        data=savings_csv,
        file_name="savings_goals.csv",
        mime="text/csv"
    )
else:
    st.write("No savings goals data available.")
