class Dog:
    name = ''
    colour = ''

    def __init__(self, str, colour):
        self.name = str
        self.colour = colour

    def run(self):
        print("I'm faaaaaaast")