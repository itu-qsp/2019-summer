# Read the code below. What is it doing?
## It defines a function augment()
## augment() takes a string as input and adds " really" to the end
## then returns an augmented string
## The rest of the code starts by creating an initial string ("I")
## Then it calls augment() twice, first on "I" and then on output of first call
## This is then printed
## Then it calls augment() again but only on the the output of second_variable
## So third_variable and fourth_variable contain the same data
## Finally we concatenate the twice augmented string with " like icecream" and print

# And what will it print when it's run?
## "I really really"
## "I really really like icecream"

# How many times is the second line (augmented_string = input_string + " really") run?
## 3 times

# What is the value of second_variable?
## second_variable contains the string "I really"

def augment(input_string):
    augmented_string = input_string + " really"
    return augmented_string

initial_variable = "I"
second_variable = augment(initial_variable)
third_variable = augment(second_variable)
print(third_variable)
fourth_variable = augment(second_variable)
fifth_variable = fourth_variable + " like icecream"
print(fifth_variable)