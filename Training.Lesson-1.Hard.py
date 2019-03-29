# print('Задание Hard: Медицинская Анкета')
# Запрашиваю входящие данные
name = str(input('1. Ваше имя:'))
surname = str(input('2. Фамилия:'))
age = int(input('3. Возраст:'))
weight = int(input('4. Вес:'))
height = int(input('5. Рост в сантиметрах:'))
#
# Рассчитываю индекс массы тела (ИМТ)
bmi = weight / ((height / 100) ** 2)
bmi = round(bmi, 2)

# По уровню bmi делаю базовый вывод, без учета возраста
if bmi <= 16:
    conclusion = 0
elif bmi <= 18.5:
    conclusion = 1
elif bmi <= 25:
    conclusion = 2
elif bmi <= 30:
    conclusion = 3
elif bmi <= 35:
    conclusion = 4
elif bmi <= 40:
    conclusion = 5
else:
    conclusion = 6


# Сдвигаю результат относительно возраста
# Т.е. чем старше человек, темы выше нормальный индекс массы тела
if age < 30:
    conclusion = conclusion + 0
elif age < 40:
    conclusion = conclusion + 1
elif age < 50:
    conclusion = conclusion + 2
else:
    conclusion = conclusion + 3

# Создаю список с выводами
conclusion_list = ['Дрыщ', 'Надо больше есть', 'Все в норме', 'Толстый', 'Очень толстый', 'Жиртрест', 'Мегажиртрес', 'Пиши завещание']

# Конечный вывод
print(name, surname)
print('Индекс Массы Вашего тела:', bmi)
print('Для Вашего возраста:', age)
print('Это означает:', conclusion_list[conclusion])
