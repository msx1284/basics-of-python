print('Задание Easy:')

name = str(input('Привет, как тебя зовут?'))
print('Отлично,', name)
choice = str(input('Готов пройти лютейший мини-тест, да/нет?'))
x = 0  # Эта переменная возвращает цикл к началу, пока пользователь не введет корректное значение

while x == 0:
    if choice == 'да':
        print('Огонь, поеееехали!')
        x = 1
    elif choice == 'нет':
        print('Ну нет так нет')
        x = 1
    else:
        print('Ответ не распознан')
        choice = str(input('Напиши строчными буквами "да" или "нет"'))

# Спрашиваем любимое число и возраст
favorite_number = int(input('Твое любимое число?'))
age = int(input('Твой возраст?'))

summing = favorite_number + 2
subtraction = favorite_number - 2
multiplication = favorite_number * 2
division = favorite_number / 2
degree = favorite_number ** 2

# Выводим инфу на экран
print('Если прибавить к твоему любимому числу "2", то получается:', summing)
print('Если отнять "2":', subtraction)
print('Если умножить на "2":', multiplication)
print('Если разделить на "2":', division)
print('Если возвести в квадрат:', degree)

if age < 18:
    print('Да, кстати, твой возраст меньше 18, так что забудь эту инфу')
else:
    print('Тест пройден')
    print('И твой приз... ты не поверишь')
    print('Я его не придумал')

