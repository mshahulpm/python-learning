class Rect:
    # this is a constructor
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


a = Rect(1, 2)
print(a)

# everything in python is an instance of a class or an object
print(type(a))
print(type(1))
print(type(""))
print(type(True))
print(type(1.6))

# concatenating 2 strings
s = "Mohammed"
s2 = "Shahul"
# both of them are same. first one use the second one under them hood
print(s + s2)
print(s.__add__(s2))
# check length
print(len(s))
print(s.__len__())


# creating custom __add__ function
class Counter:
    def __init__(self):
        self.value = 1

    def count_up(self):
        self.value += 1

    def count_down(self):
        self.value -= 1

    """ Method to print the object in human readable form """
    def __str__(self):
        return f"Count {self.value}"
    
    """ Method to add two class """
    def __add__(self,other):
        return self.value +other.value


count_1 = Counter()
count_2 = Counter()
count_1.count_up()

print(count_1,count_2)
print(count_1+count_2) # possible due to __add__ function in Counter class

# __str__ and __repr__ methods
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    # __str__ for user friendly output
    def __str__(self):
        return f"{self.make} {self.model} {self.year}"
    
    # __repr__ more detailed unambiguous 
    def __repr__(self):
        return f"Car(make='{self.make}', model='{self.model}', year='{self.year}')"
    
car = Car("Benz","BM12",205)
print(str(car))
print(repr(car))