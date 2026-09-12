# Richard Hearne
# 9/12/2026
# P1HW2
# Travel Budget Calculatons



budget = float(input("Give me your money: "))
destination = input("Where you wanna go?")
gas = float(input("Give me your gas money: "))
accommodation = float(input("Give me your accommodation money: "))
food = float(input("Give me your food money: "))




# Add expenses
total_expenses = gas + accommodation + food

# Calculate remaining budget
remaining_budget = budget - total_expenses

# Display results
print("-------Travel Budget Summary-------")
print(f"Destination: {destination}")
print(f"Gas: ${gas:.2f}")
print(f"Accommodation: ${accommodation:.2f}")
print(f"Food: ${food:.2f}")
print(f"Iitial Budget: ${budget:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")