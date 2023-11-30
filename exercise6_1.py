int_max_number = 0
wrong_number = True

# for-loop asks the user 5 times for input:
for x in range(5):
    number = int(input("Give a number:\n"))
    if number > 0:
        if number > int_max_number:
            int_max_number = number
            wrong_number = False
    else:
        print("Give the positive number!")
        wrong_number = True
        break
if not wrong_number:
    print(f"The biggest number from user: {int_max_number}")
