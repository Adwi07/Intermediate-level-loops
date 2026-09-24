# count:-

# positive numbers

# negative numbers

# zeros

# Write a program to determine whether a number is prime using a loop.

# Print all prime numbers between 1 and 100

numbers = [10, -4, 8, -2, 0, 15, -9, 21]

positive_count = 0
negative_count = 0
zero_count = 0

for number in numbers:
    if number > 0:
        print("Positive number:", number)
        positive_count += 1
    elif number < 0:
        print("Negative number:", number)
        negative_count += 1
    else:
        print("Zero:", number)
        zero_count += 1

print("Positive count:", positive_count)
print("Negative count:", negative_count)
print("Zero count:", zero_count)


#prime or not loop

check_number = int(input("Enter the number you want to check whether it is prime or not: "))

if check_number <= 1:
    print("Not prime")
else:
    is_prime = True

    for i in range(2, check_number):
        if check_number % i == 0:
            is_prime = False
            break

    print(f"Prime" if is_prime else "Not Prime")

