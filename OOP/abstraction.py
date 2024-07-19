from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def make_sound(self):
        print('sound')
class bird(animal):
    def fly(self):
        print('fly')
    def make_sound(self):
        print('bird_sound')

class cat(animal):
    def run(self):
        print('run')
    def make_sound(self):
        print('cat sound')

b1=bird()
b1.make_sound()
b1.fly()

c=cat()
c.run()

