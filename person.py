from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

#person = Person('Adam', 19)
#person.display()

#person1 = Person.fromBirthYear('John',  1985)
#person1.display()
    
####### #######################
#p1 = Person('ben', 23)
#p1.display()
#p1.__repr__()

###########################

class Etudiant(Person):
    def __init__(self, name, age, matricule, classe):
        super().__init__(name, age)
        self.matricule = matricule
        self.classe = classe

E1 = Etudiant("ben", 23, "DSXRE2024", "M3")
E1.display()