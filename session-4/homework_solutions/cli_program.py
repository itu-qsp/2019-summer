"""
Adapted from: https://wiki.python.org/moin/Powerful%20Python%20One-Liners
"""

#What does sys.argv[1] mean?
#sys.argv is a list of command line arguments. sys.argv[1] is the second item in it (index 1)

#What does line.replace(...) mean?
#it replaces a substring (pattern) within a line with a specified string (substitution)

import sys

#a variable called pattern with value (index 1) from the command line
pattern = sys.argv[1]

#a variable called substitution with value (index 2) from the command line
substitution = sys.argv[2]

#a variable called line with a string in it
line = 'My cat looks weirdly. The neighbours cat too...'

#print the string line but replace the word saved in pattern with the word in substitution
print(line.replace(pattern, substitution))
