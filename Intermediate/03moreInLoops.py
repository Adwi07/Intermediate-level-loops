# Generate multiplication tables from 1 to 10 using nested loops

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")
    print()
  

# Find all numbers between 1 and 200 divisible by both 3 and 5


for i in range(1, 201):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


# Given a list containing duplicate elements, create another list containing only unique elements without using set()

items = ['banana', 'apple', 'banana', 'grapes', 'pomegrenate', 'apple', 'kiwi', 'banana']

unique_items = []

for item in items:
    if item not in unique_items:
        unique_items.append(item)

print(unique_items)



