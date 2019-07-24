my_list = [4, 2, 8, 1, 9, -1, 8]

smallest_number = 1000000     # we initiate smallest_number to a very high value, so that it is most likely larger than any integer in our list.
for number in my_list:   #
    if number < smallest_number:
        smallest_number = number
print('I found the smallest number: ' + str(smallest_number))
