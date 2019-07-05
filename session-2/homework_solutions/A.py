# print(
# When this is written in the mu-editor, the print functions documentation pops up


# Print hello world
print('Hello world')

# Alternately
data_variable = 'Hello world'
print(data_variable)


# A variable named first which consists of a string. The string is the word "Hello". (print it!)
first = "Hello"
print(first)

# A variable called second that contains the string "," (print it!)
second = ","
print(second)

# A variable called third that contains the text "you can" as a string. (print it!)
third = "you can"
print(third)

# The string-variable fourth that should contain "code!" (print it!)
fourth = "code!"
print(fourth)

# A variable called last. This should be of the type integer, and contain your favourit number. Print last.
last = 4
print(last)


# So, print() is something called a function in Python (can you recognize the datatype of 'Hello world'?).
# Yes, it is a string. I can see that when I print the type.
print(type("Hello world"))




# Now change the way print(), prints. Instead of ending with a new line, it now should end with a questionmark (?).
# Check the docstring again if this is confusing. Do this for all five lines.

# Open and check the docstring
# print(				
print(first,end = "?")
print(second,end = "?")
print(third,end = "?")
print(fourth,end = "?")
print(last)


# Try to print the first four variables, using just one call with the print()
print(first,second,third,fourth)


# Can you figure out how to make all the variables be separated by a comma instead, or a word
print(first,second,third,fourth, sep = " --ThisIsAnOddSeperator-- ")


# Use all your new-found coding skills, variables and print-knowledge to get precisely this printed:
# Hello, you can code!
print(first,second, sep= "", end = " ")
print(third,fourth)


# Bonus (OPTIONAL)
print(third.title()[0:3], 'r ', 'favourite number is', '+'.join(['1']*last), fourth[-1], sep='')

# third.title()[0:3]	-> prints the first 3 letters of the variable, third,
#							where the first letter is as a capitsl letter
# 'r ' 			 		-> prints r whith a white space afterwards
# 'favourite number is' -> prints favourite number is
# '+'.join(['1']*last)	-> In my case the variable last=4, so this part prints 4*'1' 
#						   but whith a '+' in between. So '1+1+1+1'
# fourth[-1]			-> prints the last letter of the variable, fourth, i.e. 'e'