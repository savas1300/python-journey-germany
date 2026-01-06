import math
price = 50.5
tip_percentage = 10
tip_amount = (price * tip_percentage) / 100
total_payment = price + tip_amount
total = round(total_payment, 1)

print(f"Meal price: {price}")
print(f"Tip amount: {tip_amount}")
print(f"Total: {total}")
