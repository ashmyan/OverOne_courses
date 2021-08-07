class Group:

    def __init__(self, group, students):
        self.__group = group
        self.__students = ['Sasha Ashmyan', 'Oleg Tinkof']
        self.__students.append(students)

    def get_group(self):
        return self.__group

    def get_students(self):
        return self.__students

    def add_student(self):
        self.__students.append(input('Ф И'))

    def remove_student(self):
        remove_st = input('Введите Фамилию и Имя')
        if remove_st in self.__students:
            index_st = self.__students.index(remove_st)
            del self.__students[index_st]


class Student:
    dict_result = {}

    def __init__(self, name, surrname, marks, lessons, group):
        self.__name = name
        self.__surrname = surrname
        self.__marks = []
        self.__marks.append(marks)
        self.__lessons = ['IT', 'Math', 'Geometry']
        self.__lessons.append(lessons)

    def get_name(self):
        return self.__name

    def get_surrname(self):
        return self.__surrname

    def get_marks(self):
        return self.__marks

    def get_lessons(self):
        return self.__lessons

    def add_lesson(self):
        self.__lessons.append(input('Введите предмет.'))
        return self.__lessons

    def add_marks(self):
        self.__marks.append(input('Введите оценку.'))


class Teacher:
    lst_lessons = []

    def __init__(self, name, surname, group):
        self.__name = name
        self.__surname = surname
        self.__group = group

    def give_lessons(self):
        stud = input('Введите Ф И')
        if stud in self.__group.get_students():
            Student.dict_result[stud] = Teacher.lst_lessons
            lesson = input('Предмет')
            if lesson not in Teacher.lst_lessons:
                Student.dict_result[stud].append({lesson: input('Введите оценку:')})
            elif lesson in Student.dict_result[stud]:
                stud[lesson] += input('Введите оценку:')
        else:
            return 'Такого студента нет.'

        return Student.dict_result


all_stud = Group('OverOne', 'Goga Ginaev')
# print(all_stud.get_students())
# print(all_stud.remove_student())
# print(all_stud.get_students())

student_one = Student('Jack', 'Lol', 5, 'IT', all_stud)
# print(student_one.get_marks())
# print(student_one.get_lessons())
# print(student_one.add_marks())
# print(student_one.add_lesson())
# print(student_one.get_marks())
# print(student_one.get_lessons())

teacher = Teacher('Olga', 'Popova', all_stud)

print(teacher.give_lessons())
print(student_one.get_lessons())
print(teacher.give_lessons())
print(student_one.get_lessons())
