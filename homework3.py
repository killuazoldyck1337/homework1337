class ComparableByAverageGrade:
    
    def _get_overall_average_grade(self):
        raise NotImplementedError("Метод _get_overall_average_grade должен быть реализован в подклассе")

    def __eq__(self, other):
        if not isinstance(other, ComparableByAverageGrade):
            return NotImplemented
        return self._get_overall_average_grade() == other._get_overall_average_grade()

    def __lt__(self, other):
        if not isinstance(other, ComparableByAverageGrade):
            return NotImplemented
        return self._get_overall_average_grade() < other._get_overall_average_grade()

    def __gt__(self, other):
        if not isinstance(other, ComparableByAverageGrade):
            return NotImplemented
        return self._get_overall_average_grade() > other._get_overall_average_grade()

    def __le__(self, other):
        if not isinstance(other, ComparableByAverageGrade):
            return NotImplemented
        return self._get_overall_average_grade() <= other._get_overall_average_grade()

    def __ge__(self, other):
        if not isinstance(other, ComparableByAverageGrade):
            return NotImplemented
        return self._get_overall_average_grade() >= other._get_overall_average_grade()

class Lecturer(ComparableByAverageGrade):
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
    
    def __str__(self):
        average_grades = ', '.join([f'{k}: {v:.1f}' for k, v in self.grades.items()])
        return f'Имя: {self.name}\nСредние оценки за лекции: {average_grades}'
    
    def _get_overall_average_grade(self):
        total_sum = sum(sum(v) for v in self.grades.values())
        total_count = sum(len(v) for v in self.grades.values())
        if total_count == 0:
            return None
        return total_sum / total_count

class Student(ComparableByAverageGrade):
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
    
    def __str__(self):
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        average_grades = sum(sum(v) / len(v) for v in self.grades.values()) / len(self.grades)
        return f'Имя: {self.name}\nСредняя оценка за домашние задания: {average_grades:.1f}\n' \
               f'Курсы в процессе изучения: {courses_in_progress_str}\n' \
               f'Завершенные курсы: {finished_courses_str}'
    
    def _get_overall_average_grade(self):
        total_sum = sum(sum(v) for v in self.grades.values())
        total_count = sum(len(v) for v in self.grades.values())
        if total_count == 0:
            return None
        return total_sum / total_count

class Reviewer(ComparableByAverageGrade):
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
    
    def __str__(self):
        return f'Имя: {self.name}'