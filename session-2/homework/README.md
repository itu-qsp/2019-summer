## Assignment 2: Working with code

Hand in three to five files in a single `.zip` file:
1. one `.py` file for each exercise (`A.py`, `B.py`, `C.py`). You make this in Mu. Add a `#` to the beginning of any lines that make your program crash (only the lines you can't fix). Also add `#` to the start of lines where you answer questions in text rather than code.
2. the `eliza_language.py` file, which you need for part B

To make a `.zip` file select the three files (or the directory that you have them in) and choose "Compress" / "Komprimér" in the context menu. On Windows right-click the selection to get the context menu. On Mac either click with two fingers on the touchpad or hold down the ctrl-key while clicking.
Upload the `.zip` file on LearnIT under `Assignment 2: Working with code`.


## Exercise A, Analysis assignment:

In this assignment you will investigate how a specific function works and try out its arguments.

Try to write `print(` in Mu and read the docstring (the information that pops up).

To use the print function you wrap it around what you want to print. Like this:

`print('Hello world')` <- Write and run this code in Mu.

Alternately, you can have your data (`'Hello world'` in this case) inside a variable and feed that to the print function.
```python
data_variable = 'Hello world'
print(data_variable)
```

When you print something using `print()`, like a variable or string, it is automatically followed by a newline.
To test this in Mu create the following five variables and then print them, one at a time:

1. A variable named `first` which consists of a string. The string is the word `'Hello'`.
(print it!)
2. A variable called `second` that contains the string `','`
(print it!)
3. A variable called `third` that contains the text `'you can'` as a string.
(print it!)
4. The string-variable `fourth` that should contain `'code!'`
(print it!)
5. A variable called `last`. This should be of the type integer, and contain your favourite number. Print `last`.

So, `print()` is something called a function in Python (can you recognize the datatype of `'Hello world'`?).

Pssst: If you do not know the type of something, you can always check it with the function `type()`.
(Check out the docstring for type, by writing `type(` in Mu. Then test it out for `Hello world` to check if you were right about the data type. You need to print it to make it show.)

Now print all variables again. This should require only half as many lines of code, since you have already declared the variables. So `print(first)`, `print(second)`, and so on.

Now change the way `print()`, prints. Instead of ending with a new line, it now should end with a questionmark (`?`). Check the docstring again if this is confusing. Do this for all five lines.

Hint: What does `'\n'` mean in Python? Remember, docstrings are your best friend, Google is your second best friend!
Print your first four variables again, this time they should all print on the same line, separated by question marks instead of new lines.

Of course, there is an even better way to print multiple variables. Try to print the first four variables, using just **one** call with the `print()`-function. So the variables from `first` to `fourth` go inside the parenthesis with commas in-between.

When you print multiple variables, they are by default separated by an empty space (in Python this is equivalent to `' '`).
Take a peek at the docstring for `print()` again:
Can you figure out how to make all the variables be separated by a comma instead, or a word?
Print the variables again, this time separated by a comma, not a space.

Use all your new-found coding skills, variables and print-knowledge to get precisely this printed:

`Hello,`
`you can code!`

### Bonus (OPTIONAL)

Run this craziness:

`print()`
`print(third.title()[0:3], 'r ', 'favourite number is', '+'.join(['1']*last), fourth[-1], sep='')`

* What is printed, and why does it do that? Can you explain what the comma-separated parts are doing (`third.title()[0:3], 'r' `, ...)?


## Exercise B, Explicit assignment:

In this exercise you will talk to the famous chatbot Eliza from the 1960's.
We found the code on some old magnetic tapes and put it into the file `B.py` for you. Unfortunately, three code pieces proved unsalvageable. Can you fill in the blanks to make it run?

Note, before you can run the program you need the files `eliza_language.py` and `B.py`. Both of them should be in the same directory. Find them on www.github.com/itu-qsp/2019-summer/. You can download them directly by locating and clicking on the file, clicking the `raw` button in the upper right, and save the file that pops up.


## Exercise C, Implicit assignment:

In this assignment you will translate a human problem into a computer problem (and optionally turn it into code). You may choose to hand-in pseudo-code or working code. Remember to add a `#` to the beginning of each line that isn't functional Python code.

If you don't know what pseudo-code is then check this website: https://sites.google.com/a/ismanila.org/oliverab_cp/python/pseudocode

Use your new skills to make a super-boring game. The user thinks of a number between 1 and 10 and the computer has to guess it. If the computer guesses wrong it should guess again. If it guesses right the computer should say something. To begin with the computer can guess the same thing every time.

Extra hard: Make the game slightly less boring by changing the computer's strategy every time the game starts.

Extra extra hard: Give the computer a hint when it guesses wrong.
