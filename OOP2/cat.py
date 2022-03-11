from animal import Animal
class Cat(Animal):
    #private
    _name = ''

    def __init__(self, name, colour):
        self._name = name
        self._colour = colour

    def purr(self):
        print('Purr purr', self._name)

    #read -> getter
    def sayYourName(self):
        print("My name is", self._name)

    #change -> setter
    def rename(self, newName):
        if len(newName) > 4:
            self._name = newName

    def getColour(self):
        print("My colur is", self._colour)

    def __str__(self):
        return "My name is "+self._name +". And I'm " + self._colour