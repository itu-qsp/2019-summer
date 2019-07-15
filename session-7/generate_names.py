
import random
import us_names

def generate_names(gender, number):
    """Generates a list of names, which are randomly created out
    of names from the US census 1990.
    
    :param gender: str
        The gender of the name. Can be 'female' or 'male'
    :param number: int
        Amount of names in the returned list
    
    :return: list
        A list of strings with either female or male US names.
    """   
    all_names = []
    if gender == 'female':
        names = us_names.FEMALE_NAMES
    elif gender == 'male':
        names = us_names.MALE_NAMES
    else:
        print("Error: Gender should be either 'female' or 'male'")
    for _ in range(number):
        name = random.choice(names)
        surname = random.choice(us_names.SURNAMES)
        fullname = name + ' ' + surname
        all_names.append(fullname)
    return all_names
