import statistics

amount_students = int(input("How many students?\n"))

grades_list = []
total = 0

#for-loop asks user for input:
for x in range(amount_students):
    user_input = int(input("Student grade:\n"))

    #creating a list of grades:
    grades_list.append(user_input)

#calculating meidan value
median_value = statistics.median(grades_list)
print(f"Median: {median_value}")

#calculating average value using list of grades:
average = round(sum(grades_list) / amount_students,1)
print(f"Average grade: {average}")

#evaluating average value:
if  0 <= average < 1:
    print("Bad result")
elif 1 <= average < 2:
    print("Weak result")
elif 2 <= average < 3:
    print("Average result")
elif 3 <= average < 4:
    print("Good result")
elif 4 <= average <= 5:
    print("Excellent result")
else:
    print("Something went wrong. Try again!")

#finding the most common grade with dictionary and for-loop:

grades_dict = {}
#for-loop calculates how many times each grade appeared in the grade list and creates a dictionary:
for grade in grades_list:
    count = grades_dict.get(grade,0)
    grades_dict[grade] = count + 1

most_common = [0,0]

#for-loop finds the most common grade from dictionary I created below:
for key in grades_dict:
    if grades_dict[key] > most_common[1]:
        most_common = [key,grades_dict[key]]

print(f"The most common grade is: {most_common[1]}")



