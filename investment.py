initial_investment = int(input("please input your initial investment: "))
target_value = int(input("please input your target value: "))
interest_rate = float(input("what is your interest rate: "))
years = 0
while initial_investment < target_value:
    initial_investment *= (1 + interest_rate)
    years += 1
print("It will take", years, "years for the initial investment to grow to the target value.")
