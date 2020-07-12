class Mammal:
    def walk(self):
        print('walk')

class Dog(Mammal):
    pass

dog=Dog();
print(dog.walk());