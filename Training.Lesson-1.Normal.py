print('Задание Normal:')

print('Задача 1')
x = 5
y = int(input('Я загадал число от 0 до 10, отгадай какое:'))
while y != x:
    y = int(input('Не угадал, попробуй еще раз, число от 0 до 10:'))
x = x ** 2
print('Молодец')
print('Вот твой подарок:')
print('5 в степени 2 =', x)
print('')

print('Задача 2. Замена значений переменных')
x = int(input('Введите x:'))
y = int(input('Введите y:'))

print('Исходные данные переменных:')
print('x = ', x)
print('y =', y)

x = x * y
y = x // y
x = x // y

print('Поменять местами:')
print('x = ', x)
print('y =', y)
