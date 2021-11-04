print("welcome to the tip calculator")
bill_total = float(input("What was the total bill? "))
num_people = int(input("How many people to split the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? "))

share = round((bill_total / num_people) * (tip_percentage/100+1), 2)

print(f"Each person should pay: {share}")