import streamlit as st
import numpy as np
import pandas as pd

def simulate_payments_staggered(
    initial_balance=30000,
    annual_interest_rate=0.04,
    months=12,
    days_per_month=30,
    payment_days=(7, 14, 21, 28),
    payment_amount=1000
):
    """
    Simulate the daily balance of a savings account when credit card payments
    are staggered through each month (multiple smaller payments).
    Returns:
      - daily_balances (list of floats)
      - annual_interest_earned (float)
      - average_daily_balance (float)
    """
    daily_balances = []
    current_balance = initial_balance

    # Simulate month by month
    for month in range(months):
        for day in range(1, days_per_month + 1):
            # If today is a payment day, reduce balance
            if day in payment_days:
                current_balance -= payment_amount
                if current_balance < 0:
                    current_balance = 0  # simple cutoff for negative
                
            daily_balances.append(current_balance)
    
    avg_daily_balance = np.mean(daily_balances)
    annual_interest_earned = avg_daily_balance * annual_interest_rate
    
    return daily_balances, annual_interest_earned, avg_daily_balance


def simulate_payments_lump_sum(
    initial_balance=30000,
    annual_interest_rate=0.04,
    months=12,
    days_per_month=30,
    payment_day=28,
    payment_amount=4000
):
    """
    Simulate the daily balance of a savings account when credit card payments
    are lump-sum each month (one larger payment).
    Returns:
      - daily_balances (list of floats)
      - annual_interest_earned (float)
      - average_daily_balance (float)
    """
    daily_balances = []
    current_balance = initial_balance

    # Simulate month by month
    for month in range(months):
        for day in range(1, days_per_month + 1):
            # If today is the lump-sum payment day, reduce balance
            if day == payment_day:
                current_balance -= payment_amount
                if current_balance < 0:
                    current_balance = 0
            
            daily_balances.append(current_balance)
    
    avg_daily_balance = np.mean(daily_balances)
    annual_interest_earned = avg_daily_balance * annual_interest_rate
    
    return daily_balances, annual_interest_earned, avg_daily_balance

def main():
    st.title("Credit Card Payment Simulator")
    st.write(
        """This app simulates the difference between making multiple staggered credit card payments 
        throughout the month vs. making a single lump-sum payment near the end of the month. It then 
        compares the **average daily balance** in your savings account and the **approximate annual 
        interest** you earn under each scenario."""
    )
    
    st.sidebar.header("Simulation Parameters")
    
    # Input parameters
    initial_balance = st.sidebar.number_input(
        "Initial Savings Balance ($)",
        min_value=1000,
        max_value=1000000,
        value=30000,
        step=1000
    )
    
    annual_interest_rate = st.sidebar.slider(
        "Annual Interest Rate (%)",
        min_value=0.0,
        max_value=10.0,
        value=4.0,
        step=0.1
    ) / 100.0  # convert % to decimal
    
    months = st.sidebar.slider(
        "Number of Months to Simulate",
        min_value=1,
        max_value=24,
        value=12
    )
    
    days_per_month = st.sidebar.slider(
        "Days per Month (for simplicity)",
        min_value=28,
        max_value=31,
        value=30
    )
    
    st.sidebar.subheader("Staggered Payment Settings")
    payment_days_str = st.sidebar.text_input(
        "Payment Days (comma-separated)",
        value="7, 14, 21, 28"
    )
    # Convert user input (e.g., "7,14,21,28") into a tuple of integers
    payment_days = tuple(int(x.strip()) for x in payment_days_str.split(",") if x.strip().isdigit())
    
    payment_amount_staggered = st.sidebar.number_input(
        "Payment Amount Each Time ($)",
        min_value=100,
        max_value=20000,
        value=1000,
        step=100
    )
    
    st.sidebar.subheader("Lump-Sum Payment Settings")
    lump_sum_day = st.sidebar.slider(
        "Lump-Sum Payment Day",
        min_value=1,
        max_value=31,
        value=28
    )
    
    lump_sum_amount = st.sidebar.number_input(
        "Lump-Sum Payment Amount ($)",
        min_value=100,
        max_value=50000,
        value=4000,
        step=100
    )
    
    # Run both simulations
    daily_balances_staggered, annual_interest_staggered, avg_balance_staggered = simulate_payments_staggered(
        initial_balance=initial_balance,
        annual_interest_rate=annual_interest_rate,
        months=months,
        days_per_month=days_per_month,
        payment_days=payment_days,
        payment_amount=payment_amount_staggered
    )
    
    daily_balances_lump_sum, annual_interest_lump_sum, avg_balance_lump_sum = simulate_payments_lump_sum(
        initial_balance=initial_balance,
        annual_interest_rate=annual_interest_rate,
        months=months,
        days_per_month=days_per_month,
        payment_day=lump_sum_day,
        payment_amount=lump_sum_amount
    )
    
    # Prepare data for plotting
    days = list(range(1, len(daily_balances_staggered) + 1))
    
    df_results = pd.DataFrame({
        "Day": days,
        "Staggered Balance": daily_balances_staggered,
        "Lump-Sum Balance": daily_balances_lump_sum
    })
    
    # Display results
    st.subheader("Simulation Results")
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(
            label="Staggered: Average Daily Balance",
            value=f"${avg_balance_staggered:,.2f}"
        )
        st.metric(
            label="Staggered: Annual Interest (Approx)",
            value=f"${annual_interest_staggered:,.2f}"
        )
        
    with col2:
        st.metric(
            label="Lump-Sum: Average Daily Balance",
            value=f"${avg_balance_lump_sum:,.2f}"
        )
        st.metric(
            label="Lump-Sum: Annual Interest (Approx)",
            value=f"${annual_interest_lump_sum:,.2f}"
        )
    
    difference = annual_interest_lump_sum - annual_interest_staggered
    
    st.write(
        f"**Difference in annual interest (Lump-Sum – Staggered):** "
        f"${difference:,.2f}"
    )
    
    # Chart
    st.subheader("Daily Balances Over Time")
    st.line_chart(df_results.set_index("Day"))

if __name__ == "__main__":
    main()
