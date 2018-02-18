import pickle

class Fonts:
    def __init__(self, name, d):
        self.name = name
        self.d = d

f = open("savedFonts", 'r')
l = pickle.load(f)

print l[0].d