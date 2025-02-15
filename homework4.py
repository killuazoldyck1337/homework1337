lektor1 = Lecturer("Иван Иванов")
lektor2 = Lecturer("Алексей Алексеев")

student1 = Student("Анна Андреева")
student2 = Student("Ольга Васильевна")

reviewer1 = Reviewer("Сергей Сергеев")
reviewer2 = Reviewer("Николай Николаев")

lektor1.add_course("Курс 1")
lektor1.get_average_grade("Курс 1")  # 5.0
lektor1.__str__()

lektor2.add_course("Курс 2")
lektor2.get_average_grade("Курс 2")  # 7.5
lektor2.__str__()

student1.add_course("Курс 1")
student1.rate_lecturer("Курс 1", 6)
student1.__str__()

student2.add_course("Курс 2")
student2.rate_lecturer("Курс 2", 9)
student2.__str__()

reviewer1.check_homework(student1, "Курс 1", 8)
reviewer1.__str__()

reviewer2.check_homework(student2, "Курс 2", 9)
reviewer2.__str__()

def average_grade_students(courses, students):
    if not courses or not students:
        return None
    total_sum = 0
    total_count = 0
    for student in students:
        for course in courses:
            if course in student.grades:
                total_sum += sum(student.grades[course])
                total_count += len(student.grades[course])
    if total_count == 0:
        return None
    return total_sum / total_count

def average_grade_lectors(courses, lecturers):
    if not courses or not lecturers:
        return None
    total_sum = 0
    total_count = 0
    for lecturer in lecturers:
        for course in courses:
            if course in lecturer.grades:
                total_sum += sum(lecturer.grades[course])
                total_count += len(lecturer.grades[course])
    if total_count == 0:
        return None
    return total_sum / total_count

students = [student1, student2]
courses = ["Курс 1"]
avg_grade_students = average_grade_students(courses, students)
print(f"Средняя оценка за домашние задания по курсу 'Курс 1' составляет: {avg_grade_students:.1f}")

lectors = [lektor1, lecturer2]
courses = ["Курс 1"]
avg_grade_lectors = average_grade_lectors(courses, lectors)
print(f"Средняя оценка за лекции по курсу 'Курс 1' составляет: {avg_grade_lectors:.1f}")