## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is an object of type Animal with a function __init__ which takes self and name as paramaters
class Dog(Animal):

    def __init__(self, name):
        ## From the self object set the name attribute equal to the passed in name parameter
        self.name = name

class Cat(Animal):

    def __init__(self, name):
        ## From the self object set the name attribute equal to the passed in name parameter
        self.name = name

## Person is-a object and has-a function __init__ with paramaters self and name
class Person(object):

    def __init__(self, name):
        ## From self object set name attribute equal to name paramater
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## 
class Employee(Person):

    def __init__(self, name, salary):
        ## the "super" function is how to reliably run the __init__ method of a parent class
        super(Employee, self).__init__(name)
        ##
        self.salary = salary

## Rover is-a Dog
rover = Dog("Rover")

## 
satan = Cat("Satan")

### Jason did not finish this exercise ###
