# 2. Dog과 Bird는 Animal이다
class Animal:
    def __init__(self, name):
        self.name = name
    
    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        print(f'{self.name}! 달린다!')

    def bark(self):
        print(f'{self.name}! 짖는다!')


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def fly(self):
        print(f'{self.name}! 푸드덕!')


if __name__ == "__main__":
    dog = Dog('멍멍이')
    dog.walk()
    dog.bark()

    bird = Bird('구구')
    bird.walk()
    bird.eat()
    bird.fly()