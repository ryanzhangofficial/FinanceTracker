import streamlit as st
import numpy as np
import plotly.graph_objects as go
from layout import feedback_form

feedback_form()

tooltip_style = """
<style>
div[data-baseweb="tooltip"] {
  width: 250px;
}
</style>
"""
st.markdown(tooltip_style, unsafe_allow_html=True)

st.title("📈 Investment Simulator")
st.markdown("See how your investments can grow over time.")

definitions = {
    "Initial Investment": "The initial amount of money you invest.",
    "Monthly Contribution": "The amount you add to your investment every month.",
    "Investment Period": "The duration of your investment in years.",
    "Expected Annual Return": "The estimated percentage gain on your investment annually.",
    "Annual Return Volatility": "The fluctuation in returns, representing risk. Higher volatility means higher potential gains or losses.",
    "Inflation Rate": "The rate at which the general price level for goods and services rises, reducing purchasing power over time.",
    "Compounding Frequency": "How often your investment returns are calculated and added back to your balance."
}

initial_investment = st.number_input(
    "Initial Investment ($)", 
    min_value=0.0, value=1000.0, step=100.0, 
    help=definitions["Initial Investment"]
)
monthly_contribution = st.number_input(
    "Monthly Contribution ($)", 
    min_value=0.0, value=100.0, step=10.0, 
    help=definitions["Monthly Contribution"]
)
years = st.slider(
    "Investment Period (Years)", 
    min_value=1, max_value=50, value=10, 
    help=definitions["Investment Period"]
)
annual_return = st.slider(
    "Expected Annual Return (%)", 
    min_value=0.0, max_value=15.0, value=7.0, 
    help=definitions["Expected Annual Return"]
)
annual_return_volatility = st.slider(
    "Annual Return Volatility (%)", 
    min_value=0.0, max_value=10.0, value=5.0, 
    help=definitions["Annual Return Volatility"]
)
inflation_rate = st.slider(
    "Inflation Rate (%)", 
    min_value=0.0, max_value=10.0, value=2.0, 
    help=definitions["Inflation Rate"]
)
compound_frequency = st.selectbox(
    "Compounding Frequency", 
    ["Monthly", "Quarterly", "Annually"], 
    help=definitions["Compounding Frequency"]
)

months = years * 12
if compound_frequency == "Monthly":
    periods_per_year = 12
elif compound_frequency == "Quarterly":
    periods_per_year = 4
else:
    periods_per_year = 1

periodic_return = (1 + annual_return / 100) ** (1/periods_per_year) - 1
balances = []

balance = initial_investment
for i in range(months):
    annual_return_with_volatility = np.random.normal(annual_return, annual_return_volatility)
    monthly_return_adjusted = (1 + annual_return_with_volatility / 100) ** (1/12) - 1
    inflation_adjustment = (1 + inflation_rate / 100) ** (1/12)
    balance = (balance * (1 + monthly_return_adjusted) / inflation_adjustment) + monthly_contribution
    balances.append(balance)

fig = go.Figure()
fig.add_trace(go.Scatter(x=list(range(1, months + 1)), y=balances, mode='lines'))
fig.update_layout(
    title='Investment Growth Over Time (Adjusted for Inflation)',
    xaxis_title='Months',
    yaxis_title='Balance ($)',
    template='plotly_white'
)
st.plotly_chart(fig)

final_balance = balances[-1]
st.markdown(f"### Final Balance: ${final_balance:,.2f}")
st.markdown(f"### Total Contributions: ${monthly_contribution * months + initial_investment:,.2f}")
st.markdown(f"### Total Growth: ${final_balance - (monthly_contribution * months + initial_investment):,.2f}")
