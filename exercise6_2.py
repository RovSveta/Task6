running = True
result = 0

# while loop takes care of running the app, if it runs or not:
while running:
    number = int(input("Which multiplication table would you like to see? (1/10). 0 stops program.\n"))
    if 0 < number <= 10:
        #for-loop prints all the rows of the multiplication table:
        for i in range(10):
           result = number * (i+1)
           print(f"{number} * {i+1} = {result}")
    elif number == 0:
        running = False
    else:
        print("Wrong number format.")
