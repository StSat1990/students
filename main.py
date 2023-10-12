import mydatabase
mydatabase.add_student('Никита', 16, '10А')
mydatabase.add_student('Олег', 17, '11А')
mydatabase.add_student('Ольга', 16, '10А')
mydatabase.add_student('Елена', 14, '8А')

while True:
    print('Вывести список учеников - 1')
    print('Вывести информацию о конкретном ученике - 2')
    print('Перевести ученика в другой класс - 3')
    print('Удалить ученика - 4')
    user = int(input('Выберите дейстие 1, 2, 3, 4: '))
    if user == 1:
        mydatabase.student()
    elif user == 2:
        name = input('Введите имя студента: ')
        mydatabase.get_student_by_name(name)
    elif user == 3:
        name = input('Введите имя ученика: ')
        grade = input('Введите класс в который хотите перевести ученика: ')
        mydatabase.update_student_grade(name, grade)
    elif user == 4:
        name = input('Введите имя ученика: ')
        mydatabase.del_student(name)
    else:
        print('Не верный ввод')

