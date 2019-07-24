class ColourChanger:
    def __init__(self):
        self.colour_replacement = {'red': 'black', 'green': 'white'}

    def retain_caps(self, source, target):
        if source[0].isupper():
            return target[0].upper() + target[1:]
        else:
            return target

    def make_readable(self, colours):
        result = []
        for col in colours:
            key = col.lower()
            if key in self.colour_replacement:
                replacement = self.retain_caps(
                    col, self.colour_replacement[key])
                result.append(replacement)
            else:
                result.append(col)
        return result


c = ColourChanger()
print(c.make_readable(['Red', 'Green', 'white', 'pink', 'yellow', 'red']))
