# Run this file through your debugger

list_of_lists = [
    ['Gin', 'Vermouth', 'Campari', 'Orange peel'],
    ['White port', 'Tonic water'],
    ['Vodka', 'Triple sec', 'Cranberry juice', 'Lime juice'],
    ['Vodka', 'Tequila', 'Light rum', 'Triple sec', 'Gin', 'Cola'],
    ['Vodka', 'Tomato juice', 'Worcestershire sauce']
] 

for ingredients in list_of_lists:
    print('For this drink I need the following ingredients:')
    for ingredient in ingredients:
        print(ingredient, end=', ')
    print('and that was it!\n')
