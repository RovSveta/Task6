original_price = int(input("Original price of the car:\n"))
year = int(input("Year of manufacturing:\n"))
kilometers = int(input("Driven kilometers (mileage):\n"))
price_category = int(input("Price category of the manufacturer (1 or 2):\n"))
import_car = input("Is it an import car or not (y/n)\n")

years_use = 2023 - year
limit_price_1 =  original_price * 0.18
limit_price_2 =  original_price * 0.12

#First check category:
if price_category == 2:
    #Second check km:
    if kilometers >= 30000:
        #Third check if years of using the car more and equal to 5:
        if years_use >= 5:
            #for-loop calculates decrease of the original price for first 5 years, year by year:
            for i in range(5):
                price_decrease_5 = original_price * 0.10
                original_price = original_price - price_decrease_5
            #loop calculates decrease of the original price after 5th year for each  year:
            for p in range(years_use - 5):
                price_decrease_after = original_price * 0.07
                original_price = original_price - price_decrease_after
            # if statement checks if price after decrease more than limit price:
            if original_price < limit_price_2:
                original_price = limit_price_2
        else:
            #loop calculates decrease in case car was used less than 5 years:
            for p in range(years_use):
                price_decrease_after = original_price * 0.10
                original_price = original_price - price_decrease_after
            #comparison with limit price
            if original_price < limit_price_2:
                original_price = limit_price_2
    else:
        #the same logic in case driven km more than 30 000km
        if years_use >= 5:
            for i in range(5):
                price_decrease_5 = original_price * 0.08
                original_price = original_price - price_decrease_5
            for p in range(years_use - 5):
                price_decrease_after = original_price * 0.05
                original_price = original_price - price_decrease_after
            if original_price < limit_price_2:
                original_price = limit_price_2
        else:
            for p in range(years_use):
                price_decrease_after = original_price * 0.08
                original_price = original_price - price_decrease_after
            if original_price < limit_price_2:
                original_price = limit_price_2
#the same logic as above:
elif price_category == 1:
    if kilometers >= 30000:
        if years_use >= 5:
            for i in range(5):
                price_decrease_5 = original_price * 0.07
                original_price = original_price - price_decrease_5
            for p in range(years_use - 5):
                price_decrease_after = original_price * 0.04
                original_price = original_price - price_decrease_after
            if original_price < limit_price_1:
                original_price = limit_price_1
        else:
            for p in range(years_use):
                price_decrease_after = original_price * 0.07
                original_price = original_price - price_decrease_after
            if original_price < limit_price_1:
                original_price = limit_price_1
    else:
        if years_use > 5:
            for i in range(5):
                price_decrease_5 = original_price * 0.05
                original_price = original_price - price_decrease_5
            for p in range(years_use - 5):
                price_decrease_after = original_price * 0.03
                original_price = original_price - price_decrease_after
            if original_price < limit_price_1:
                original_price = limit_price_1
        else:
            for p in range(years_use):
                price_decrease_after = original_price * 0.05
                original_price = original_price - price_decrease_after
            print(original_price)
            if original_price < limit_price_1:
                original_price = limit_price_1
else:
    print("Try again!")

#checking for user input and if needed adding tax of 24%
if import_car == "y":
    final_price_tax = original_price * 1.24
    print(f"Final price:{int(round(final_price_tax,0))} €")
else:
    print(f"Final price:{int(round(original_price,0))} €")
