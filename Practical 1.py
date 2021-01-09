
from abc import ABC,abstractmethod
class  Duck(ABC):
    @abstractmethod
    def duck_walk(self):
        pass
    def duck_swim(self):
        pass
    def duck_quack(self):
        pass
    def duck_eat(self):
        pass
    def duck_drink(self):
        pass
    
class MountainDuck(Duck):
    def duck_walk(self):
        print("Duck can walk")
    def duck_quack(self):
        print("Duck can quack")
    def duck_eat(self):
        print("Duck can eat")
    def duck_drink(self):
        print("Duck can drink")
    def duck_swim(self):
        print("Duck can swim")
        
class DesertDuck(Duck):
    def duck_walk(self):
        print("Duck can walk")
    def duck_quack(self):
        print("Duck can quack")
    def duck_eat(self):
        print("Duck can eat")

class LakeDuck(Duck):
    def duck_quack(self):
        print("Duck can quack")
    def duck_eat(self):
        print("Duck can eat")
    def duck_drink(self):
        print("Duck can drink")

class ToyDuck(Duck):
    def duck_walk(self):
        print("Duck can walk")
    def duck_swim(self):
        print("Duck can swim")
        
class Main():
    def __init__(self,Duck):
        self.Duck = Duck
    def quality(self):
        self.Duck.duck_quack()
        self.Duck.duck_walk()
        self.Duck.duck_swim()
        
if __name__ == "__main__":
    Duck_q = Main(MountainDuck())
    
Duck_q.quality()

