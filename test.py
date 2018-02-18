import pickle

class Fonts:
    def __init__(self, name, d):
        self.name = name
        self.d = d

f = open("savedFonts", 'r')
l = pickle.load(f)

for font in l:
    print font.name, ":", font.d, "\n\n\n"