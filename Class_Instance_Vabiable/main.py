class School:
    School_name = "B A F Shaheen College, Jashore" # Class Variable.

    def __init__(self):
        self.name = "shiam" # Instance Variable


a1 = School()
a1.name = "Rakib"
print(a1.name)
print(a1.School_name)

a2 = School()
a2.name = "Zarifah"
print(a2.name)
print(a2.School_name)

a3 = School()
a3.name = "Sumu"
a3.School_name = "Army school"
print(a3.name)
print(a3.School_name)