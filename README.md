# Piggy Pal: AI Agent for Personal Finance

# Just One Feature

# Credit Card Payment Simulator

This **Streamlit** application simulates the difference in annual interest earnings for a savings account when credit card payments are:

1. **Staggered** over multiple days during the month (e.g., four smaller payments).
2. **Lump-Sum** on a single day each month (one larger payment).

It calculates:
- **Average Daily Balance** for each scenario.
- **Approximate Annual Interest** earned for each scenario.
- The **difference** between the two approaches.

## Features

- **Interactive Inputs**  
  Easily modify parameters in the sidebar, such as:
  - Initial savings balance
  - Annual interest rate
  - Number of months to simulate
  - Days per month (for simplicity)
  - Staggered payment days and amounts
  - Lump-sum payment day and amount

- **Visual Comparison**  
  - Line chart displays daily balances over the entire simulation period for both scenarios.
  - Metrics compare average daily balances and approximate annual interest earnings.

- **Real-Time Updates**  
  Any change to the sidebar inputs immediately re-runs the simulation and updates the results.

## Prerequisites

1. **Python 3.7+**  
   Make sure Python is installed on your machine.  
2. **Streamlit**  
   You can install Streamlit using:
   ```bash
   pip install streamlit
   ```
3. **NumPy** and **Pandas**  
   If you don’t have these already:
   ```bash
   pip install numpy pandas
   ```

## Installation

1. **Clone or Download** this repository.  
2. **Navigate** to the project folder in your terminal.

## Usage

1. **Save** the file (e.g., `credit_card_sim_app.py`) in your project folder.
2. **Install dependencies** (if not already installed):
   ```bash
   pip install streamlit numpy pandas
   ```
3. **Run** the Streamlit app:
   ```bash
   streamlit run credit_card_sim_app.py
   ```
4. **Open** your browser to the link displayed in your terminal (usually [http://localhost:8501](http://localhost:8501)).

## Code Overview

```python
import streamlit as st
import numpy as np
import pandas as pd

def simulate_payments_staggered(...):
    """
    Simulate the daily balance when credit card payments
    are staggered throughout the month.
    Returns daily balances, annual interest earned, and average daily balance.
    """

def simulate_payments_lump_sum(...):
    """
    Simulate the daily balance when a single lump-sum
    credit card payment is made each month.
    Returns daily balances, annual interest earned, and average daily balance.
    """

def main():
    st.title("Credit Card Payment Simulator")
    # 1) Sidebar: Collect user inputs
    # 2) Run the simulations
    # 3) Display results and chart

if __name__ == "__main__":
    main()
```

### Simulation Logic

1. **Daily Balances**  
   For each day of each month, the code checks whether a payment is due (based on user-specified days). The balance is reduced by the payment amount and stored in a list for that day.

2. **Average Daily Balance**  
   Once all the daily balances are calculated, the mean (`np.mean`) of these balances is considered your **average daily balance** for the scenario.

3. **Annual Interest**  
   The approximate annual interest is calculated by:
   \[
   \text{Annual Interest} \approx \text{Average Daily Balance} \times \text{Annual Rate}
   \]  
   (\*Note: This is a simplified model that assumes no daily compounding.)

4. **Comparison**  
   - Both scenarios (Staggered vs. Lump-Sum) are run separately.
   - You’ll see the **line chart** of daily balances.
   - The difference in **annual interest** (Lump-Sum – Staggered) is displayed.

## Customizing the Simulation

- **Payment Days**  
  Enter multiple days (e.g., `7,14,21,28`) for staggered payments. 
- **Payment Amounts**  
  You can change how much you pay in each scenario.  
- **Months**  
  Increase or decrease the simulation length from 1 to 24 months (or more).
- **Days per Month**  
  Set to 30 by default for simplicity, but you can adjust to 28-31.

## Limitations

- **Simplified Interest Calculation**  
  This model uses average daily balance × annual interest rate. Actual calculations at a bank may involve daily or monthly compounding.  
- **No Negative Balances**  
  If a payment exceeds the current balance, it’s set to 0 instead of going negative.  
- **No Transaction Lag**  
  Payments are assumed instantaneous; there’s no delay in the money leaving your account.

## Contributing

1. Fork the repository and create your branch.
2. Make changes or add new features.
3. Submit a pull request, and we'll review your changes.

## License

This project is provided **as-is** and is intended for **educational** and **illustrative** purposes only. It is **not** financial advice.  

---

Enjoy experimenting with **Credit Card Payment Simulator** and seeing how a simple change in payment timing can (slightly) affect your savings account’s annual interest!