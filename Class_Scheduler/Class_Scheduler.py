class Student:
    def __init__(self, name):
        self.name = name
        self.classes = []

    def add_class(self, class_name):
        self.classes.append(class_name)

    def get_classes(self):
        return self.classes


class Subject:
    def __init__(self, name):
        self.name = name
        self.classes= []

    def add_class(self, class_name):
        self.classes.append(class_name) 
        
    def get_classed(self):
        return self.classes


class Class:
    def __init__(self, name, subject, time):
        self.name = name
        self.subject = subject
        self.time = time


class Scheduler:
    def __init__(self):
        self.students = []
        self.subjects = []
        self.classes = []

    def add_student(self, student):
        self.students.append(student)

    def add_subject(self, subject):
        self.classes.append(subject)

    def add_class(self, class_name):
        self.append(class_name)

    def assign_classes(self):
        for student in self.students:
            chosen_classes = student.get_classes()
            for class_name in chosen_classes:
                if not self.is_class_available(class_name):
                    print(f"Class conflict: {student.name} cannot attend {class_name}") 
                else:
                    self.enroll_student(student, class_name) 

    def is_class_available(self, class_name):
        for enrolled_class in self.classes:
            if enrolled_class.name == class_name:
                return True
            return False

    def enroll_student(self, student, class_name):
        for enrolled_class in self.classes:
            if enrolled_class.name == class_name:
                student.add_class(enrolled_class)
                enrolled_class.subject.add_class(enrolled_class) 
                print(f"{student.name} enrolled in {class_name}") 
                break

# Creating students, subjects, and classes
student1 = Student("Tayler")
student2 = Student("Chris")
student3 = Student("Steve")

subject1 = Subject("Math")
subject2 = Subject("Science")
subject3 = Subject("English")

class1 = Class("Math Class A", subject1, "10:00 AM")
class2 = Class("Math Class B", subject1, "2:00 PM")
class3 = Class("Science Class A", subject2, "11:00 AM")
class4 = Class("English Class A", subject3, "1:00 PM")

# Adding students, subjects, and classes to the scheduler
scheduler = Scheduler()
scheduler.add_student(student1)
scheduler.add_student(student2)
scheduler.add_student(student3)

scheduler.add_subject(subject1)
scheduler.add_subject(subject2)
scheduler.add_subject(subject3)

scheduler.add_class(class1)
scheduler.add_class(class2)
scheduler.add_class(class3)
scheduler.add_class(class4)

# Assign Classes to Students
student1.add_class("Math Class A")
student2.add_class("Math Class B")
student3.add_class("Science Class A")
student3.add_class("English Class A")

# Running the scheduler
scheduler.assign_classes()