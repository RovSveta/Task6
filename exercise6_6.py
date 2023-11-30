basket = ["apple","banana","cherry","carrot","potato","tomato","cabbage"]

choice = input("Which fruit to ignore?\n")

# cheching if input is a number:
if choice.isnumeric():
   choice = int(choice)
   choice = basket[choice - 1]

if choice not in basket:
    print("Word not found.")
else:
    # in a loop conditional statement checks if input match a fruit in the list
    # and than according to result prints a fruit or ignor:
    for fruit in basket:
        if choice == fruit:
            continue
        else:
            print(fruit)
