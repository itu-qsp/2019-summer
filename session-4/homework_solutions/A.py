#A_1

#What is the difference between the variable called ingredients and the variable called ingredient?
#Ingredients is a list that is an item within list_of_lists.
#Ingredient is an item within a list (ingredients) that is within list_of_lists.

#Why are there two for loops?
#Loops are there because we want to repeat certain operations with these lists.
#And there are two loops because we want to do the same operations to all of these lists
#and when doing that we want to operate on each of the strings within those lists.

list_of_lists = [
    ['Gin', 'Vermouth', 'Campari', 'Orange peel'],
    ['White port', 'Tonic water'],
    ['Vodka', 'Triple sec', 'Cranberry juice', 'Lime juice'],
    ['Vodka', 'Tequila', 'Light rum', 'Triple sec', 'Gin', 'Cola'],
    ['Vodka', 'Tomato juice', 'Worcestershire sauce']
]

for ingredients in list_of_lists:
    print('For this drink I need the following ingredients:')
    print(", ".join(ingredients), end = ', ')
    print('and that was it!\n')