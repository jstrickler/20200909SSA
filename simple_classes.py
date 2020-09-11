
class Animal:
    def move(self):
        print("moving...")

class Widget:
    def toast(self):
        print("toasty!")

class Dog(Animal, Widget):

    def move(self):
#         super().move()
        print("dog is moving")

    def bark(self):  #  self is same as 'this' in C++/Java/C#
        x = 5
        self.x = 5
        Animal.spam = 'wombat'
        print("woof! woof!")

d1 = Dog()   #  Dog d1 = new Dog();
d2 = Dog()
d3 = Dog()

d1.bark()
d3.bark()

d2.move()
d1.toast()


