# Loop recap exercises

# Some lists to loop over
characters = ['a','b','c','d','e','f']
numbers = [1,2,3,4,5,6,7,8,9,10]


# Create for loop, which prints all elements from character
# for elm in characters:
#     print(elm)


# Create for loop, which prints all elements from character with their index
# for i, charter in enumerate(characters):
#     print(i,charter)


# Create a for loop which increments all elements from numbers by 1
# for i in range(len(numbers)):
#     numbers[i] += 1
# print(numbers)


# Create a for loop which increments all elements from numbers by their index value
# for i in range(len(numbers)):
#     numbers[i] += i
# print(numbers)


# Loop over the list numbers and print all numbers less than 5
# for number in numbers:
#     if number < 5:
#         print(number)


# Loop over the list numbers and print all the even numbers
#for number in numbers:
#    if number % 2 == 0:
#        print(number)

# Loop over the list numbers and print all the even numbers, between 4 and 10.
# for number in numbers:
#    if number % 2 == 0 and number >= 4 and number <= 10:
#         print(number)



# loop over characters and muplitply it with some random numer, and add it to a new list
# import random
# new_char = []
# for char in characters:
#     new_char.append(char * random.randint(1,10))
# print(new_char)

# Write a Python program to construct the following pattern, using a nested for loop.
# *
# * *
# * * *
# * * * *
# Hint use a range, which starts at 0 and ends at 5

for i in range(5):
    for j in range(i):
        print('*', sep='', end='')
    print()

# Write a Python program to construct the following pattern, using a nested for loop.
# * * * * *
# * * * *
# * * *
# * *
# *
# Hint use a range, which starts at 5 and ends at 0
for i in range(5,0,-1):
    for j in range(i):
        print('*', sep='', end='')
    print()


