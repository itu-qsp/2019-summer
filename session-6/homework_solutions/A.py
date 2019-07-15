"""
Create a Mad Libs program that reads in text files and lets the user add their own text anywhere
the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
For example, a text file may look like this, see file mad_libs.txt:

The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.

The program would find these occurrences and prompt the user to replace them.
Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck

The following text file would then be created:

The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.

The results should be printed to the screen and saved to a new text file.
"""

# 1. Read in the mad_libs and save it as a list where the words are the items, initialize an empty list for the result
# 2. loop through all of the words.
# 3. check if the words are either ADJECTIVE, NOUN, ADVERB, or VERB
# 4. if they are, then replace them by a input.
# 5. Append all words to the result list
# 6. save result in a new file.

# Opens the mad_libs.txt and saves it as a list where the items are all of the words
with open("/Users/viktortorpthomsen/Desktop/qsp2019/session6_homework/mad_libs.txt", "r") as f:
    words = f.read().split()

# Initializing a new list to store the result in
new_words = []

# Looping through all of the words in the list words
for word in words:
    if "ADJECTIVE" in word:
        # If the string "ADJECTIVE" is in the current word, then replace that part of the word
        word = word.replace("ADJECTIVE", input("Enter an adjective:\n"))
    elif "NOUN" in word:
        # If the string "NOUN" is in the current word, then replace that part of the word
        word = word.replace("NOUN", input("Enter a noun:\n"))
    elif "ADVERB" in word:
        # If the string "ADVERB" is in the current word, then replace that part of the word
        word = word.replace("ADVERB", input("Enter an adverb:\n"))
    elif "VERB" in word:
        # If the string "VERB" is in the current word, then replace that part of the word
        word = word.replace("VERB", input("Enter an verb:\n"))
    # Append the word to the list, whether is was changes or not.
    new_words.append(word)

# Prints the new_words list as a string, where all of the items (the words in the list) are seperated by " " (a white space)
print(" ".join(new_words))

# Write the new file
with open("/Users/viktortorpthomsen/Desktop/qsp2019/session6_homework/mad_libs_result.txt", "w") as f:
    # Write the same string we printed in line 59 in the new file
    f.write(" ".join(new_words))

# Open the new file to check that it was saved as we wanted
with open("/Users/viktortorpthomsen/Desktop/qsp2019/session6_homework/mad_libs_result.txt", "r") as f:
    new_text = f.read()
print(new_text)