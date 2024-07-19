#!/usr/bin/python3
is_same_class = __import__('2-is_same_class').is_same_class

class MyClass:
    pass

class AnotherClass:
    pass

obj1 = MyClass()
obj2 = AnotherClass()

print(is_same_class(obj1, MyClass))        # Should print: True
print(is_same_class(obj2, MyClass))        # Should print: False
print(is_same_class(obj1, AnotherClass))   # Should print: False
print(is_same_class(obj2, AnotherClass))   # Should print: True
print(is_same_class(42, int))              # Should print: True
print(is_same_class(42, str))              # Should print: False

