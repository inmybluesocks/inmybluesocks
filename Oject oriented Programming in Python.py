# Oject oriented Programming in Python

class Student:
    def_init_(self, name, age, grade):
    self.name = __name__
    self.age = age
    self.grade = grade # 0 - 100

    def get_grade(self):
        return self.get_grade
    
    class Course:
        def _init_(self, name, max_studnet):
            self.name = name
            self.max_students = max_students
            seld.students = []

        def add_student(self. student):
            if len(self.students) < self.max_students:
                self.students.append(Student)
                return True
            return False
        
        def get_average_grade(self):
            value = 0
            for student in self.students:
                value += student.get.grade()

            returnvlue/ len(self.students)


s1 = Student("tim", 19, 95)
s2 = Student("bill", 19 75)
s3 = Student("Jill", 19,65)

vourse = Course("Science", 2)
course.add.student(s1)
course.add.student(s2)
print(course.get_average_grade())




        

