class Student:
    
    age_increase = 25
    num_of_students = 0
    average = 0

    
    def __init__(self, first, last, age, class_, math1, math2, math3):
        self.first = first
        self.last = last
        self.age = age
        self.class_ = class_
        self.math1 = math1
        self.math2 = math2
        self.math3 = math3
        Student.average
        Student.num_of_students += 1

    def fullName(self):
        return(self.first + " " + self.last)
    
    def change_age(self):
        self.age = int(self.age + self.age_increase)
        
    def score(self):
        Student.average = int( self.math1 + self.math2 + self.math3) // 3
        
student_1 = Student("john", "smith", 10, "maths", 30, 30, 30)
student_2 = Student("jo", "momma", 99, "english", 10, 20, 30)

#print(Student.num_of_students)

student_1.score()
print(student_1.average)

student_2.score()
print(student_2.average)

