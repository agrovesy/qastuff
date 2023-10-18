

#class Dog:
#    energy = "high"
    
#    def speak(self):
#        print("bark")

#fido = Dog()

#fido.energy = "low"

#print(fido.energy)

#fido.speak()

#class Students:
#    pass

#student_1 = Students()
#student_2 = Students()

#print(student_1)


#student_1.first = "john"
#student_1.last = "smith"
#student_1.age = 10

#print(student_1.first, student_1.last)

#student_2.first = "jo"
#student_2.last = "mamma"
#student_2.age = 99

#print(student_2.first, student_2.last)

### method

#class Student:
#    def __init__(self, first, last, age):
#        self.first = first
#        self.last = last
#        self.age = age
        
#        self.full = first + " " + last

#    def fullName(self):
#        return(self.first + " " + self.last)
#    
#    def change_age(self):
#        self.age = int(self.age + 1)
        
        
#student_1 = Student("john", "smith", 10)
#student_2 = Student("jo", "momma", 99)

#print(student_2.fullName())
#print(Student.fullName(student_2))

#print(student_1.age, student_2.age)

#student_1.change_age()
#student_2.change_age()

#print(student_1.age, student_2.age)


#class Student:
    
#    age_increase = 25
    
#    def __init__(self, first, last, age):
#        self.first = first
#        self.last = last
#        self.age = age
        
#        self.full = first + " " + last

#    def fullName(self):
#        return(self.first + " " + self.last)
#    
#    def change_age(self):
#        self.age = int(self.age + self.age_increase)
        
        
#student_1 = Student("john", "smith", 10)
#student_2 = Student("jo", "momma", 99)


#print(student_1.age, student_2.age)

#student_1.change_age()
#student_2.change_age()

#print(student_1.age)

#print(student_1.__dict__)
#print(student_2.__dict__)
#print(Student.__dict__)

#Student.age_increase = 20

#print(Student.__dict__)

#student_1.age_increase = 10
#student_1.change_age()

#print(student_1.age)
#print(student_1.__dict__)

#class Student:
    
#    age_increase = 25
#    num_of_students = 0
    
#    def __init__(self, first, last, age):
#        self.first = first
#        self.last = last
#        self.age = age
#        Student.num_of_students += 1#

#    def fullName(self):
#        return(self.first + " " + self.last)
    
#    def change_age(self):
#        self.age = int(self.age + self.age_increase)
        
#print(Student.num_of_students)
        
#student_1 = Student("john", "smith", 10)
#student_2 = Student("jo", "momma", 99)

#print(Student.num_of_students)

##parent class

#class Animal:
#    def __init__(self, name, species):
#        self.name = name
#        self.species = species
        
#    def eat(self):
#        print(f"{self.name} is eating")
        
## child class

#class Dog(Animal):
#    def __init__(self, name, species, breed):
#        super().__init__(name, species)
#        self.breed = breed
        
#    def woof(self):
#        print("woof")
        
        
#my_dog = Dog("my biggles", "border collie", "yes")       

#my_dog.woof()
#my_dog.eat()

#print(my_dog)

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def __str__(self):
        return f"{self.name} {self.species}"
    
class Cat(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed
        
    def meow(self):
        print("meow")
        
    def __str__(self):
        return f"{self.name} {self.species} {self.breed}"
    
    

my_cat = Cat("wiggles", "cat", "no")   
 
print(my_cat) 


class Feline:
    __family = "something"
    
cat3 = Feline()

print(cat3._Feline__family)



