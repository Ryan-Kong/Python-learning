# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
class Animal(object):   # 定义单一主父继承
    class Mammal(Animal):
        class Dog(Mammal):
        class Bat(Mammal):
    class Bird(Animal):
        class Parrot(Bird):
        class Ostrich(Bird):



class Animal(object):   # 定义多重继承,同时继承多个关系
class RunnableMixIn(object):
        def run(self):
            print('Running')
class FlyableMixIn(object):
    def fly(self):
        print('Flying')
    class Mammal(Animal):
    class Bird(Animal):
        class Dog(Mammal,RunnableMixIn)
        class Parrot(Bird,FlyableMixIn)

