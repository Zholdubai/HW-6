class Dog:
    def __init__(self,name, weight, height, color, voice):
        self.name = name
        self.weight = weight
        self.height = height
        self.color = color
        self.voice = voice

    def name_golos(self):
        print(f'{self.name}: {self.voice}')

dog= Dog('Avcharka',40, 1,'Black', 'ay-ay')
dog.name_golos()

class Cat:
    def __init__(self,name, weight, height, color, voice):
        self.name = name
        self.weight = weight
        self.height = height
        self.color = color
        self.voice = voice


    def name_golos(self):
        print(f'{self.name}: {self.voice}')

cat = Cat('Kiskis',3, 1,'Black', 'miau-miau')
cat.name_golos()


class Cow:
    def __init__(self,name, weight, height, color, voice):
        self.name = name
        self.weight = weight
        self.height = height
        self.color = color
        self.voice = voice

    def name_golos(self):
        print(f'{self.name}: {self.voice}')

cow = Cow('Alabash',100, 1.5,'black and white', 'muu-muu')
cow.name_golos()

class Bear:
    def __init__(self,name, weight, height, color, voice):
        self.name = name
        self.weight = weight
        self.height = height
        self.color = color
        self.voice = voice

    def name_golos(self):
        print(f'{self.name}: {self.voice}')

bear = Bear('Wildbear',900, 1.5,'brown', 'roar- roar')
print(bear)
bear.name_golos()