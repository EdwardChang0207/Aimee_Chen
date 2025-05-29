class Person:
    def __init__(self, name, age, gender): #.->1.對...做... 2.的
        self.name = name
        self.age = age
        self.gender = gender
    def sayHi(self):
        print('hi I am', self.name)

alan = Person('alan', 18, 'male')
print(alan.age)
print(alan.gender)
mary = Person('mary', 20, 'female')
print(mary.name)

alan.sayHi()

#list
l = []
l.append()
