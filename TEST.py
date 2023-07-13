#https://docs.google.com/forms/d/e/1FAIpQLSc59EboXcmq5Hfp1ERJkCVURy1vYS1zKvEEGSb03uWdbiHq4Q/viewform

# Перед вами таблица с результатами экзамена для 6-х студентов.
# Первая строка - название столбцов. Последующие содержат данные.
grades = [
    ['Студент', 'Предм_1', 'Предм_2', 'Предм_3'],
    ['Максим', '100', '90', '80'],
    ['Елена', '88', '99', '111'],
    ['Петр', '45', '56', '67'],
    ['Феврония', '59', '61', '67'],
    ['Владимир', '73', '79', '83'],
    ['Евгения', '89', '97', '101']
]

# В переменную students запишите новый список с именами студентов,
# как они находятся в таблице сверху-вниз.
students = []
for i in grades[1:]:
    students.append(i[0])
print(students)


# В переменную assignments запишите новый список с названиями предметов,
# что содержатся в первой строке.
assignments = grades[0][1:]
print(assignments)


# В переменную grade_lists запишите новый словарь, который будет
# хранить по именам студентов списки их оценок. Оценки должны быть числами.
# Например grade_lists['Максим'] == [100, 90, 80].
grade_lists = {}
for i in grades[1:]:
    grade_lists[i[0]] = list(map(int, i[1:]))
print(grade_lists)



# В переменную avg_grades_by_student запишите новый словарь, который будет
# хранить по именам студентов среднюю оценку за все предметы.
# Например avg_grades_by_student['Максим'] == 90.
avg_grades_by_student = {}
for key, res in grade_lists.items():
    avg_grades_by_student[key] = sum(res)/len(res)

print(avg_grades_by_student)


#Напишите функцию, которая принимала бы имя и оценки по всем трем предметам для нового студента и
# добавляла бы эту информацию в список grades
def add_new_student(lst, name, grade1, grade2, grade3):
    lst.append([name, grade1, grade2, grade3])


add_new_student(grades, 'Григорий', 100, 100, 100)
print(grades)
