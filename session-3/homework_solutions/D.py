from us_names import SURNAMES, FEMALE_NAMES, MALE_NAMES

#Option 1: for-loop

for i in range(0,2):
    print(FEMALE_NAMES[i] + ' ' + SURNAMES[i])


#Option 2: while-loop
counter = 2
while counter > 0:
    print(MALE_NAMES[counter] + ' ' + SURNAMES[counter])
    counter -= 1
