# budget_planner.py
import streamlit as st
import pandas as pd
from layout import feedback_form
from helpers import load_data, save_data

feedback_form()

st.title("💸 Budget Planner")
st.markdown("Plan your budget across different categories.")

# Load budgets DataFrame from CSV
if 'budgets' not in st.session_state:
    st.session_state['budgets'] = load_data('budgets.csv', ['Category', 'Allocated'])

# Add Budget Category
with st.form("Add Budget Category"):
    category = st.text_input("Category")
    allocated = st.number_input("Allocated Amount ($)", min_value=0.0, step=10.0)
    submitted = st.form_submit_button("Add")

if submitted:
    new_row = {'Category': category, 'Allocated': allocated}
    st.session_state['budgets'] = pd.concat([st.session_state['budgets'], pd.DataFrame([new_row])], ignore_index=True)
    save_data(st.session_state['budgets'], 'budgets.csv')
    st.success("Budget category added!")

# Display Budgets
st.subheader("Your Budget Plan")
if not st.session_state['budgets'].empty:
    st.dataframe(st.session_state['budgets'])
    st.session_state['total_budget'] = st.session_state['budgets']['Allocated'].sum()
else:
    st.write("No budget categories added yet.")
