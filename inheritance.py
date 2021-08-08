class Animal:
    def __init__(self):
        self.legs = 4

    def breathe(self):
        print('Animal is breathing using lungs')

class Land_Mammal(Animal):
    def __init__(self):
        super().__init__()

    # override
    def breathe(self):
        print('Mammal is breathing using lungs')

cow = Animal()
zebra = Land_Mammal()

cow.breathe()
zebra.breathe()