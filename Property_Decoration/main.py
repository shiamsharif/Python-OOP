class Student:
    def __init__(self, name, marks):
        self.name = name  # Instance Variable
        self._marks = marks  # Private Variable (convention: _marks)

    @property
    def marks(self):  # Getter method
        return self._marks

    @marks.setter
    def marks(self, new_marks):  # Setter method
        if 0 <= new_marks <= 100:
            self._marks = new_marks
        else:
            print("Invalid marks! Must be between 0 and 100.")

    @marks.deleter
    def marks(self):  # Deleter method
        print("Deleting marks...")
        del self._marks


# Creating an object
s1 = Student("Shiam", 85)

# Accessing marks like an attribute (getter method)
print(s1.marks)  # Output: 85

# Modifying marks using the setter method
s1.marks = 95
print(s1.marks)  # Output: 95

# Trying to set invalid marks
s1.marks = 110  # Output: Invalid marks! Must be between 0 and 100.

# Deleting marks using the deleter method
del s1.marks  # Output: Deleting marks...
