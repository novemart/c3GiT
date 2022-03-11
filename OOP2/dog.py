from animal import Animal


class Dog(Animal):

    def __init__(self, str, colour):
        self._name = str
        self._colour = colour

    def run(self):
        #calling the parent class's run method
        super().run()
        print("I'm faaaaaaast")

    def __str__(self):
        return "Hi, my name is " + self._name

    # @property
    # def my_name(self):
    #     return self._name
    #
    # @my_name.setter
    # def my_name(self, newName):
    #     self._name = newName
