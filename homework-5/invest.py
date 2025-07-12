def invest(amount, rate, years):
    for i in range(1, years + 1):
        amount = amount *(1 + rate)
        print(f"year {i}: {amount:.2f}")

initial_amount = float(input('Enter the initial amount: '))
annual_rate = float(input('Enter the annual percentage rate: '))
years_number = int(input('Enter the amount of years: '))
invest(initial_amount, annual_rate, years_number)
