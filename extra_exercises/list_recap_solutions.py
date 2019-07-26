# Inspired by the exercises from Automate the boring stuff Chapter 4.



# Create a list called animals, containing the following strings: 'cat', 'bat', 'rat', 'elephant'
# Solution
animals = ['cat', 'bat', 'rat', 'elephant']
# Indexes    0      1      2         3

# print the first element from animals
# Solution
# print(animals[0])


# print the animal "rat"
# Solution
#print(animals[2])

# print all of the animals
# Solution
# print(animals[0],animals[1],animals[2],animals[3])


# What happens if we use the index 100?
# print(animals[100])
# Solution
# It will give an IndexError: list index out of range


# Can a list contain the following [1,2,3,"a","b","c",[1,2,3]]?
# Solution
# funky_list = [1,2,3,"a","b","c",[1,2,3]]
# print(type(funky_list))
# Yes it can


# Create a new list named animals_with_weights containing the following two list: ['dog', 'bird', 'snake', 'fish'], [10, 20, 30, 40]
# Solutions
# animals_with_weights = [['dog', 'bird', 'snake', 'fish'], [10, 20, 30, 40]]

# Alternative
animals_with_weights = []       # Initialize an empty list
animals_with_weights.append(['dog', 'bird', 'snake', 'fish'])   # This will append the entire list of names, to the list animals_with_weights
animals_with_weights.append([10, 20, 30, 40])
# print(animals_with_weights)


# Create a new varibale called animal_names containing all of the animal names, from animals_with_weights
# Solution
animal_names = animals_with_weights[0]
# print(animal_names)


# Create a new varibale called animal_weights containing all of the animal weights, from animals_with_weights
# Solution
animal_weights = animals_with_weights[1]
# print(animal_weights)


# What will the following print?
# print(animal_names[-1])
# Solution
# fish

# print(animal_weights[-2])
# Solution
# 30


# print(animals[1:2])
# Solution
# ['bat']


# print(animals[1:4])
# Solution
# ['bat', 'rat', 'elephant']


# print(animals[::2])
# Solution
# ['cat','rat']


# print(animals[1::2])
# Solution
# ['bat','elephant']


# What is the lenght of animals_with_weights
# Solution
print(len(animals_with_weights))
# 2

# What is the lenght of animals_names
# Solution
print(len(animal_names))
# 4

# Try to create the following list  ['dog', 'bird', 'snake', 'fish', 10, 20, 30, 40], by using animal_names and animal_weights
# Solution
# new_list = animal_names + animal_weights
# print(new_list)


# create the following list ['dog', 'bird', 'snake', 'fish','dog', 'bird', 'snake', 'fish','dog', 'bird', 'snake', 'fish'], by using animal_names
# Solution
# new_list2 = animal_names * 3
# print(new_list2)


# Remove "bird" from animal_names
# Solution
# del animal_names[1]
print(animal_names)

# Remove the last item from animal_names
# Solution
del animal_names[-1]
print(animal_names)