#parent class
class Person():
    def __init__(self ,name):
        self.name = name
 # child class
class Teacher(Person):       #inherit from parent'class
    def __init__(self ,name ,subject):
        super().__init__(name)
        self.subject =  subject
 # Display
    def display(self):
        print(f'name :{self.name}, subject : {self.subject}')  
if __name__ == "__main__":
    teacher = Teacher("Sir Ameen" , "Statistics")    
    teacher.display()
