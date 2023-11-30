original_price = 50000
year = 2016
kilometers = 140000
price_category = 2
import_car = "y"

years_use = 2023 - year

first_5_percent = 1
last_percent = 1

# setting percentages based on given input
if price_category == 2:
	limit_price = original_price * 0.12

	if kilometers >= 30000:
		first_5_percent = 0.9
		last_percent = 0.93
	else:
		first_5_percent = 0.92
		last_percent = 0.95
elif price_category == 1:
	limit_price = original_price * 0.18

	if kilometers >= 30000:
		first_5_percent = 0.93
		last_percent = 0.96
	else:
		first_5_percent = 0.95
		last_percent = 0.97
else:
	raise ValueError("Try again")

# calculating price based on given percentages
for i in range(years_use):
	if i < 5:
		original_price = original_price * first_5_percent
	else:
		original_price = original_price * last_percent

# price_cap
if original_price < limit_price:
	original_price = limit_price

# adding tax and output
if import_car == "y":
	final_price_tax = original_price * 1.24
	print(f"Final price:{int(round(final_price_tax, 0))} €")
else:
	print(f"Final price:{int(round(original_price, 0))} €")
