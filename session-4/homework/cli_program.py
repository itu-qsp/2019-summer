"""
Adapted from: https://wiki.python.org/moin/Powerful%20Python%20One-Liners
"""
import sys

pattern = sys.argv[1]
substitution = sys.argv[2]
line = 'My cat looks weirdly. The neighbours cat too...'
print(line.replace(pattern, substitution))
