class ColourChanger:
    def __init__(self):
        self.colour_replacement = {'red': 'black', 'green': 'white'}

    def retain_caps(self, source, target):
        if source[0].isupper():
            return target[0].upper() + target[1:]
        else:
            return target

    def make_readable(self, colours):
        has_red = False
        has_green = False

        result = []
        for col in colours:
            key = col.lower()

            if key == 'red':
                has_red = True
            elif key == 'green':
                has_green = True

            if key in self.colour_replacement:
                replacement = self.retain_caps(
                    col, self.colour_replacement[key])
                result.append(replacement)
            else:
                result.append(col)

        if has_red and has_green:
            return result
        else:
            return colours


c = ColourChanger()
print(c.make_readable(['Red', 'Green', 'white', 'pink', 'yellow', 'red']))
