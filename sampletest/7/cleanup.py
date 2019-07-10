class Cleaner:
    def __init__(self, forbidden_word = "frack"):
        """ Set the forbidden word """
        self.word = forbidden_word

    def clean_line(self, line):
        """Clean up a single string, replacing the forbidden word by *beep!*"""
        found = line.find(self.word)
        if found != -1:
            return line[:found] + "*beep!*" + line[found+len(self.word):]
        return line

    def clean(self, text):
        for i in range(len(text)):
            text[i] = self.clean_line(text[i])


example_text = [
        "What the frack! I am not going",
        "to honour that question with a response.",
        "In fact, I think you should",
        "get the fracking frack out of here!",
        "Frack you!"
        ]

clean_text = Cleaner().clean(example_text)

for line in example_text: print line

