# savings_goals.py
import streamlit as st
import pandas as pd
from layout import feedback_form
from helpers import load_data, save_data

feedback_form()

st.title("💰 Savings Goals")
st.markdown("Set and track your savings goals.")

if 'savings_goals' not in st.session_state:
    st.session_state['savings_goals'] = load_data('savings_goals.csv', ['Goal', 'Target Amount', 'Saved Amount'])

with st.form("Add Savings Goal"):
    goal = st.text_input("Savings Goal")
    target_amount = st.number_input("Target Amount ($)", min_value=0.0, step=10.0)
    saved_amount = st.number_input("Amount Saved So Far ($)", min_value=0.0, step=10.0)
    submitted = st.form_submit_button("Add Goal")

if submitted:
    new_row = {'Goal': goal, 'Target Amount': target_amount, 'Saved Amount': saved_amount}
    st.session_state['savings_goals'] = pd.concat([st.session_state['savings_goals'], pd.DataFrame([new_row])], ignore_index=True)
    save_data(st.session_state['savings_goals'], 'savings_goals.csv')
    st.success("Savings goal added!")

st.subheader("Your Savings Goals")
if not st.session_state['savings_goals'].empty:
    for index, row in st.session_state['savings_goals'].iterrows():
        st.write(f"**{row['Goal']}**")
        progress = row['Saved Amount'] / row['Target Amount'] if row['Target Amount'] > 0 else 0
        st.progress(min(progress, 1.0))
        st.write(f"Progress: ${row['Saved Amount']:.2f} / ${row['Target Amount']:.2f} ($)")
else:
    st.write("No savings goals added yet.")
