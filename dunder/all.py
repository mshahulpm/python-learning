class MyClass:
    # Called when a new instance is created
    # Common & Important: typically used to initialize instance attributes
    def __init__(self, value):
        self.value = value

    # Called when an object is converted to a string (e.g., with str())
    # Important: used for readable, user-friendly string representation
    def __str__(self):
        return f"MyClass with value: {self.value}"

    # Called when an object is converted to a developer-friendly string (e.g., with repr())
    # Important for debugging
    def __repr__(self):
        return f"MyClass({self.value})"

    # Called when using len() on the object
    def __len__(self):
        return len(str(self.value))

    # Called when the object is deleted with del
    def __del__(self):
        print("Object is being destroyed")

    # Called when using object[key]
    def __getitem__(self, key):
        return f"Getting item at {key}"

    # Called when setting object[key] = value
    def __setitem__(self, key, value):
        print(f"Setting item at {key} to {value}")

    # Called when deleting object[key]
    def __delitem__(self, key):
        print(f"Deleting item at {key}")

    # Called when using 'in' keyword
    def __contains__(self, item):
        return str(item) in str(self.value)

    # Called when iterating over the object
    def __iter__(self):
        return iter(str(self.value))

    # Called to get the next item during iteration
    def __next__(self):
        raise StopIteration

    # Called when calling the object like a function
    def __call__(self, *args, **kwargs):
        print(f"Called with args: {args} and kwargs: {kwargs}")

    # Arithmetic operators
    def __add__(self, other):
        return self.value + other

    def __sub__(self, other):
        return self.value - other

    def __mul__(self, other):
        return self.value * other

    def __truediv__(self, other):
        return self.value / other

    # Comparison operators
    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return self.value != other

    def __lt__(self, other):
        return self.value < other

    def __le__(self, other):
        return self.value <= other

    def __gt__(self, other):
        return self.value > other

    def __ge__(self, other):
        return self.value >= other

    # Context Manager Methods (with statement support)
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")

    # Hashing method, allows using the object as a dict key or set member
    def __hash__(self):
        return hash(self.value)

    # Boolean conversion (if obj: ...)
    def __bool__(self):
        return bool(self.value)

    # Returns class name when type() is called
    def __class__(self):
        return type(self)

# Example Usage
obj = MyClass(10)
print(obj)                 # __str__
print(repr(obj))           # __repr__
print(len(obj))            # __len__
obj("Hello")               # __call__
print(obj + 5)             # __add__
print(obj == 10)           # __eq__

with MyClass(5) as o:      # __enter__, __exit__
    print("Inside with block")
