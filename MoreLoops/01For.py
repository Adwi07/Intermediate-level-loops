# Write a program to print numbers from 1 to 100 using a for loop

for i in range(1, 101):
    print(i)



for j in range(1, 101):
    if j % 2 == 0:
        print(j, "Is even")
    else:
        print(j, "Is odd")


Value_int = int(input("Enter the number: "))

for number in range(1, 21):
    print(f"{Value_int} * {number} = {Value_int * number} ") 


n = int(input("Enter the number you want sum upto: ")
)

sum = 0

for i in range(1, n+1):
    sum = sum + i


print("Sum is: ",sum)


'Calculate the factorial of a number without using any built-in factorial function.'


number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    print("Factorial:", factorial)