class Animal(object):

    def run(self):
        print('Animal is running...')

    def eat(self):
        print('Eating meat...')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
dog.run()
