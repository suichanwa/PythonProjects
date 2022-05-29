class mainClass():
    name = 'name from mainClass'


class anoth:
    def __init__(self, name):
        self.name = name
        self.age = 23
        self.email = 'someemail'

        @property
        def age(self):
            return self.age
        
        @age.setter
        def age(self, age):
            if age < 0:
                raise ValueError("Age must be positive")
            self.age = age
    
class anthh(anoth):
    #change email name from anoth class
    def __init__(self, name):
        super().__init__(name)
        self.email = 'is she changed?'



class Example:
    def __init__(self):
        print('testng')

    def returnnum(self):
        return 0
    
    def say_something(self):
        print("Hello")

class Persons:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Name: {0}, Age: {1}".format(self.name, self.age)

exa = Example()
exa.say_something()
exa.returnnum()

person = Persons("John", "25")
print(person)


class testing:
    def testing_AnotherPerson(name):
        name = "John"
        assert person.name == name
        assert person.age == 1
        person.display()

class atributes(mainClass):
    type = 'something'
    des = 'another'
    default_name = 'somename'

    def __init__(self, name):
        if name:
            self.name = name
        else:
            self.name = atributes.default_name
    @staticmethod
    def static_method():
        print(atributes.name)

class obj:
    def __init__(self, name ,age):
        self.name = name
        self.age = age
    
    def display(self):
        print(self.name, self.age)
    
    def __str__(self):
        return "Name: {0}, Age: {1}".format(self.name, self.age)

class codeWars:
    
    arr = [1,2,3,4,5,6,7,8,9,10]

    def sum_array(arr):
        sum = 0
        for i in arr:
            sum += i
        return sum

    def greeting(name):
        return "Hello, {0} how are you doing today?".format(name)

    #We need a function that counts the number of sheep present in the array
    def count_sheep(sheep):
        return sum([1 for s in sheep if s == True])



if __name__ == '__main__':
    enter = anthh("name")
    enter.age = -1

    print(enter.email)
    classExample = atributes("name")
    classExample.static_method()
    obc = obj("name", 3)
    obc.display()
