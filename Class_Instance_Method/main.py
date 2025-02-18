class School:
    School_name = "B A F Shaheen College, Jashore"  # Class Variable.

    def __init__(self):
        self.name = "shiam"  # Instance Variable

    @classmethod
    def Change_school_name(cls, new_name):
        cls.School_name = new_name  # Modifies class variable

    def set_name(self, new_name):  # Instance method
        self.name = new_name  # Modifies instance variable


a1 = School()
a1.set_name("Tuly")  # Calls instance method
School.Change_school_name("Army school")  # Calls class method

print(a1.name)  # Output: Tuly
print(a1.School_name)  # Output: Army school
