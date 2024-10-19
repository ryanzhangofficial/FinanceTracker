# home.py
import streamlit as st
import pandas as pd
import altair as alt
from layout import feedback_form
from helpers import load_data
from datetime import datetime

feedback_form()

st.title("📊 Dashboard")
st.markdown("Overview of your financial status.")

if 'budgets' not in st.session_state:
    st.session_state['budgets'] = load_data('budgets.csv', ['Category', 'Allocated'])
if 'expenses' not in st.session_state:
    st.session_state['expenses'] = load_data('expenses.csv', ['Date', 'Category', 'Amount', 'Description'])
if 'savings_goals' not in st.session_state:
    st.session_state['savings_goals'] = load_data('savings_goals.csv', ['Goal', 'Target Amount', 'Saved Amount'])

if not st.session_state['expenses'].empty:
    st.session_state['expenses']['Date'] = pd.to_datetime(st.session_state['expenses']['Date'])

total_budget = st.session_state['budgets']['Allocated'].sum()
total_expenses = st.session_state['expenses']['Amount'].sum()

total_saved_goals = st.session_state['savings_goals']['Saved Amount'].sum()

total_savings = (total_budget - total_expenses if total_budget > total_expenses else 0) + total_saved_goals

col1, col2, col3 = st.columns([1, 1, 1], gap="small")
col1.metric("Total Budget", f"${total_budget:.2f}")
col2.metric("Total Expenses", f"${total_expenses:.2f}")
col3.metric("Total Savings", f"${total_savings:.2f}")

if total_budget > 0:
    budget_utilization = (total_expenses / total_budget) * 100
    st.progress(min(budget_utilization / 100, 1.0))
    st.write(f"Budget Utilization: {budget_utilization:.2f}%")
else:
    st.write("Set up your budget to see utilization.")

st.subheader("Details")
col4, col5 = st.columns(2)
col4.write("**Monthly Overview**")
col5.write("**Yearly Trends**")

if not st.session_state['expenses'].empty:
    st.markdown("### Monthly Expense Breakdown")
    st.session_state['expenses']['Date'] = pd.to_datetime(st.session_state['expenses']['Date'])
    st.session_state['expenses']['Month'] = st.session_state['expenses']['Date'].dt.strftime('%Y-%m')
    monthly_expenses = st.session_state['expenses'].groupby('Month')['Amount'].sum().reset_index()

    expense_chart = alt.Chart(monthly_expenses).mark_bar(color='steelblue').encode(
        x='Month',
        y='Amount'
    ).properties(
        width=700,
        height=400
    )

    st.altair_chart(expense_chart, use_container_width=True)
else:
    st.write("No expenses recorded yet.")

# Yearly Trends
if not st.session_state['expenses'].empty:
    st.markdown("### Yearly Expense Trends")
    st.session_state['expenses']['Year'] = st.session_state['expenses']['Date'].dt.year
    yearly_expenses = st.session_state['expenses'].groupby('Year')['Amount'].sum().reset_index()

    line_chart = alt.Chart(yearly_expenses).mark_line(point=True).encode(
        x='Year',
        y='Amount'
    ).properties(
        width=700,
        height=400
    )

    st.altair_chart(line_chart, use_container_width=True)
else:
    st.write("No expenses recorded yet.")

# Top Expense Categories
if not st.session_state['expenses'].empty:
    st.markdown("### Top Expense Categories")
    category_expenses = st.session_state['expenses'].groupby('Category')['Amount'].sum().reset_index()
    category_expenses = category_expenses.sort_values(by='Amount', ascending=False)

    st.table(category_expenses)
else:
    st.write("No expenses recorded yet.")

# Savings Progress
if not st.session_state['savings_goals'].empty:
    st.subheader("Savings Goals Progress")
    for index, row in st.session_state['savings_goals'].iterrows():
        st.write(f"**{row['Goal']}**")
        progress = row['Saved Amount'] / row['Target Amount']
        st.progress(min(progress, 1.0))
        st.write(f"Progress: ${row['Saved Amount']:.2f} / ${row['Target Amount']:.2f}")
else:
    st.write("No savings goals added yet.")
