class Lecturer:
    def __init__(self, name):
        self.name = name
        self.grades = {}
    
    def add_course(self, course_name):
        if course_name not in self.grades:
            self.grades[course_name] = []
    
    def get_average_grade(self, course_name):
        grades = self.grades.get(course_name)
        if grades:
            return sum(grades) / len(grades)
        else:
            return None

class Student:
    def __init__(self, name):
        self.name = name
        self.courses = {}
        self.grades = {}
        self.courses_in_progress = []
        self.finished_courses = []
        
    def add_course(self, course_name, lecturer):
        if course_name not in self.courses:
            self.courses[course_name] = lecturer
            
    def rate_lecturer(self, course_name, grade):
        lecturer = self.courses.get(course_name)
        if lecturer is not None:
            lecturer.grades[course_name].append(grade)

class Reviewer:
    def __init__(self, name):
        self.name = name
    
    def check_homework(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'