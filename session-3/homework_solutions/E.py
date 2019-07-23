from random import randint
from us_names import SURNAMES, FEMALE_NAMES, MALE_NAMES

#Option 1: for-loop
for i in range(0,2):
    random_nr_surnames = randint(0, len(SURNAMES)-1)
    random_nr_females = randint(0, len(FEMALE_NAMES)-1)
    print(FEMALE_NAMES[random_nr_females] + ' ' + SURNAMES[random_nr_surnames])


#Option 2: while-loop
counter = 2
while counter > 0:
    random_nr_surnames = randint(0, len(SURNAMES)-1)
    random_nr_males = randint(0, len(MALE_NAMES)-1)
    print(MALE_NAMES[random_nr_males] + ' ' + SURNAMES[random_nr_surnames])
    counter -= 1
