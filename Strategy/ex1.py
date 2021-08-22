from abc import ABC, abstractmethod

# sperate the behaviour from implemintation
# strategy pattern


class FlyBehavior(ABC):
    @abstractmethod
    def fly():
        pass


class QuackBehavior(ABC):
    @abstractmethod
    def quack():
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("FlyWithWings")


class FlyWithoutWings(FlyBehavior):
    def fly(self):
        print("FlyWithoutWings")


class Quack(QuackBehavior):
    def quack(self):
        print("quack")


class Silent(QuackBehavior):
    def quack(self):
        print("Silent i dont quack you idot")


class Duck:
    flybehavior = None
    quackbehavior = None

    def performfly(self):
        self.flybehavior.fly()

    def performquack(self):
        self.quackbehavior.quack()

    def setflybehavior(self, fb):
        self.flybehavior = fb

    def setquackbehavior(self, qb):
        self.quackbehavior = qb

    def swim(self):
        print("every duck can swim")


class MallarDuck(Duck):
    def __init__(self):
        self.flybehavior = FlyWithWings()
        self.quackbehavior = Quack()


m = MallarDuck()
m.performquack()
m.performfly()
m.setflybehavior(FlyWithoutWings())
m.performfly()
