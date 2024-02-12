import tkinter as tk
from tkinter import ttk
import math


def calculate():
    # Get the selected calculation (investment or bond)
    selection = choice_var.get()

    if selection == 'investment':
        # For investment calculation
        deposit = float(deposit_entry.get())  # Get deposit amount
        interest_rate = float(interest_rate_entry.get()) / 100  # Get interest rate (convert to decimal)
        years = int(years_entry.get())  # Get number of years
        interest = interest_var.get()  # Get interest type (simple or compound)

        if interest == 'simple':
            # Calculate total amount with simple interest
            total_amount = deposit * (1 + interest_rate * years)
        else:
            # Calculate total amount with compound interest
            total_amount = deposit * math.pow((1 + interest_rate), years)

        # Display the calculated total amount
        result_label.config(text=f"The total amount after {years} years will be: £{total_amount:.2f}")

    elif selection == 'bond':
        # For bond calculation
        house_value = float(house_value_entry.get())  # Get house value
        interest_rate2 = float(interest_rate2_entry.get())  # Get interest rate
        months = int(months_entry.get())  # Get number of months for repayment

        monthly_rate = (interest_rate2 / 100) / 12  # Convert annual interest rate to monthly rate
        repayment = (monthly_rate * house_value) / (
                    1 - (1 + monthly_rate) ** (-months))  # Calculate monthly repayment amount

        # Display the calculated monthly repayment amount
        result_label.config(text=f"The monthly repayment amount will be: £{repayment:.2f}")


# Create the main tkinter window
root = tk.Tk()
root.title("Finance Calculators")

# Create a frame to hold all widgets
mainframe = ttk.Frame(root, padding="20")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.N, tk.E, tk.S))

# Label for selecting the calculation
choice_label = ttk.Label(mainframe, text="Choose Calculation:")
choice_label.grid(column=0, row=0, sticky=tk.W)

# Dropdown menu for selecting calculation
choice_var = tk.StringVar()
choice_combobox = ttk.Combobox(mainframe, textvariable=choice_var, values=['investment', 'bond'])
choice_combobox.grid(column=1, row=0, sticky=tk.W)


# Function to show the appropriate frame based on selection
def show_frame(*args):
    selection = choice_var.get()
    if selection == 'investment':
        investment_frame.grid(column=0, row=1, columnspan=2, sticky=(tk.W, tk.N, tk.E, tk.S))
        bond_frame.grid_remove()
    elif selection == 'bond':
        bond_frame.grid(column=0, row=1, columnspan=2, sticky=(tk.W, tk.N, tk.E, tk.S))
        investment_frame.grid_remove()


# Trace the variable to call show_frame() when its value changes
choice_var.trace('w', show_frame)

# Investment frame
investment_frame = ttk.Frame(mainframe, padding="10")
investment_frame.grid(column=0, row=1, columnspan=2, sticky=(tk.W, tk.N, tk.E, tk.S))

# Labels and entry fields for investment calculation
deposit_label = ttk.Label(investment_frame, text="Deposit:")
deposit_label.grid(column=0, row=0, sticky=tk.W)
deposit_entry = ttk.Entry(investment_frame)
deposit_entry.grid(column=1, row=0)

interest_rate_label = ttk.Label(investment_frame, text="Interest Rate (%):")
interest_rate_label.grid(column=0, row=1, sticky=tk.W)
interest_rate_entry = ttk.Entry(investment_frame)
interest_rate_entry.grid(column=1, row=1)

years_label = ttk.Label(investment_frame, text="Years:")
years_label.grid(column=0, row=2, sticky=tk.W)
years_entry = ttk.Entry(investment_frame)
years_entry.grid(column=1, row=2)

interest_label = ttk.Label(investment_frame, text="Interest Type:")
interest_label.grid(column=0, row=3, sticky=tk.W)
interest_var = tk.StringVar()
interest_combobox = ttk.Combobox(investment_frame, textvariable=interest_var, values=['simple', 'compound'])
interest_combobox.grid(column=1, row=3)

# Bond frame
bond_frame = ttk.Frame(mainframe, padding="10")
bond_frame.grid(column=0, row=1, columnspan=2, sticky=(tk.W, tk.N, tk.E, tk.S))
bond_frame.grid_remove()

# Labels and entry fields for bond calculation
house_value_label = ttk.Label(bond_frame, text="Present Value of House:")
house_value_label.grid(column=0, row=0, sticky=tk.W)
house_value_entry = ttk.Entry(bond_frame)
house_value_entry.grid(column=1, row=0)

interest_rate2_label = ttk.Label(bond_frame, text="Annual Interest Rate (%):")
interest_rate2_label.grid(column=0, row=1, sticky=tk.W)
interest_rate2_entry = ttk.Entry(bond_frame)
interest_rate2_entry.grid(column=1, row=1)

months_label = ttk.Label(bond_frame, text="Months for Repayment:")
months_label.grid(column=0, row=2, sticky=tk.W)
months_entry = ttk.Entry(bond_frame)
months_entry.grid(column=1, row=2)

# Result label
result_label = ttk.Label(mainframe, text="")
result_label.grid(column=0, row=2, columnspan=2, sticky=(tk.W, tk.N, tk.E, tk.S))

# Calculate button
calculate_button = ttk.Button(mainframe, text="Calculate", command=calculate)
calculate_button.grid(column=0, row=3, columnspan=2, sticky=(tk.W, tk.N, tk.E, tk.S))

# Show the initial frame
show_frame()

# Run the main event loop
root.mainloop()
