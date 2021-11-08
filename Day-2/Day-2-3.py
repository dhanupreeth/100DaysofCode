# Simple Monthly Interest Calculator 
import datetime
from calendar import monthrange

year = input("Enter the year: ")
month = int(input("Enter the month in number Example - 2, the Feburary month will be taken: "))
num_days = monthrange(int(year), month)[1]
per_day_ineterest = input("Interest Per Day: ")

# Enter the Principle Amount 
principle_amount = int(input("Enter the principle amount, Example - 500000 : "))
print("Interest will be calculate for", num_days, "Days")
interest_rate = num_days * int(per_day_ineterest)
print("Per Lac the interest rate is:", interest_rate)
total_interest = (principle_amount / 100000)  * int(interest_rate)
total_interest_as_init = int(total_interest)
print(f"Your Payable Interest rate for the {month}th month is {total_interest_as_init}")

