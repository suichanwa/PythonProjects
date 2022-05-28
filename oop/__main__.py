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

#show persons data
person = Persons("John", "25")
print(person)


#test code with pytest
class testing:
    def test_one(self):
        x = "this"
        assert "a" in x

pytest = testing()
pytest.test_one()