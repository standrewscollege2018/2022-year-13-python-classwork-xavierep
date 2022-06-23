''' This is a Student Management System using object orientation'''

class Student:
    ''' Student objects have a name, age, phone number, enrolment status
        and a list of their classes '''

    def __init__(self, name, age, phone, classes):
        ''' Set up new student object '''

        self._name = name
        self._age = age
        self._phone = phone
        self._classes = classes
        self._enrolled = True

        # Append to student_list
        student_list.append(self)

    def get_name(self):
        ''' Return student name'''

        return self._name

    def get_age(self):
        ''' Return student age'''

        return self._age

    def get_phone(self):
        ''' Return student phone number'''

        return self._phone

    def get_enrolled(self):
        ''' Return student enrolment status'''

        return self._enrolled

    def get_classes(self):
        ''' Display a list of classes student is enrolled in '''

        class_list = ""
        for c in self._classes:
            class_list += c + " "
        return class_list
    
# List to store students
student_list = []

#Create students
Student("Riley", 18, 9696,["MATH", "DIGI"])
Student("Harry", 18, 420, ["DIGI", "PHYS", "BIOL"])

def display_students():
    ''' Display names of all students '''
    for s in student_list:
        print(f"{s.get_name()}")

def display_student(name):
    ''' Display details of selected student '''
    for s in student_list:
        if name in s.get_name():
            print("=" * 30)
            print(f"Name: {s.get_name()}")
            print(f"Age: {s.get_age()}")
            print(f"Phone: {s.get_phone()}")
            print(f"Classes: {s.get_classes()}")
            print("=" * 30)
            print("")


display_students()

student_name = input("Enter name of student:")
display_student(student_name)