# Practice for, break, continue, else, range(), enumerate(), and nested loops.


# Print numbers from 1–100 but skip numbers divisible by 5 using continue


for i in range(1, 101):
    if i % 5 == 0:
        continue
    print(i)

# Iterate from 1–100 and stop when you encounter the first number divisible by both 7 and 11

for i in range(1, 101):
    if i % 7 == 0 and i % 11 == 0:
        break
    print(i)



# Search for a user-provided number inside a list. Use for-else to print:

listt = [2, 45, 6, 8, 1, 5, 7, 3, 57, 8]

user_input = int(input("Enter the number you want to look inside the list: "))

if user_input in listt:
    print(f"The number you are looking for is,{user_input} and its index is {listt.index(user_input)} ")
else:
    print("Number Not Found")


# names = ["Aman", "Ravi", "Sudhanshu", "Priya", "Anjali"]

# use enumerate() to display

# 1 Aman

# 2 Ravi

# 3 Sudhanshu

names = ["Aman", "Ravi", "Sudhanshu", "Priya", "Anjali"]

for index, name in enumerate(names, start=1):
    print(f"Sr No: {index} Name: {name}")
    index+=1



