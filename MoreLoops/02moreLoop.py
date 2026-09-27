# Print every language along with its length.

languages = ["Python", "Java", "C++", "JavaScript", "Go"]

for language in languages:
    print(f"languege is {language} with the length {len(language)}")




# print every key and value.

student = {

"name": "Rahul",

"age": 22,

"course": "Data Science",

"city": "Bangalore"

}

for key,value in student.items():
    print(f"Key: {key} and its value: {value}")



# Count how many vowels exist in a user-provided string.


vowels = "aeiou"

user_string = str(input("Enter the string in which you want to check the vowel count: ")).lower()

vowel_count = 0

for character in user_string:
    if character in vowels:
        vowel_count += 1

print(f"The no of vowel is {vowel_count}")



# Reverse a string using a for loop without using [::-1] or reversed().

usr_string = str(input("Enter a valid string:"))

reversed_string = ""

for chr in usr_string:
    reversed_string = chr + reversed_string


print("Reversed string is: ",reversed_string)

    

# Find the largest number from a list without using max().


numbers = [23, 45, 76, 12, 54, 88, 43]

largest = numbers[0]

for number in range(len(numbers)):
    if numbers[number] > largest:
        largest = numbers[number]

print("Largest", largest)


    


