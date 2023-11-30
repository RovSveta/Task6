#Asking user to give start and end number:
start = int(input("Give the range start:\n"))
end = int(input("Give the range end:\n"))
found = False

#checking in for-loop if number divisible by 5 and 7 and
#based on that, printing the result:
for number in range(start, end + 1):
    if number % 5 == 0 and number % 7 == 0:
        print(f"The {number} is divisible by both 5 and 7!")
        print("Stopping the search.")
        found = True
        break
    elif number % 5 == 0 and number % 7 != 0:
         print(f"{number} is not divisible by 7, skip.")
         continue
    elif number % 7 == 0 and number % 5 !=0:
        print(f"{number} is not divisible by 5, skip.")
        continue
    elif number % 7 !=0 and number % 5 != 0:
        print(f"{number} is not divisible by 5, skip.")

#using boolean checking if number was fount or not:
if not found:
    print("Suitable number not found within range.")

