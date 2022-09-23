# s = 'Hello world'
# a = 123 
# b = 1.23

# print(s)
# print(a)
# print(b)

# print(type(s))
# print(type(a))
# print(type(b))

# print (s) # вывод строки
# print (a, '-', b, '-', s) 
# print ('{} - {} - {}'.format(a,b,s))
# print (f'{a} - {b} - {s}')

# f = True
# print(type(f))

# list[1,2,3]
# list=['1','2','3', 'hello']
# print(list)
#  col = [1,3,5] # следи за пробелами
# print(col)

# print('Введите a')
# a = input()
# print('Введите b')
# b = input()
# print (a,b)
# print('{} {}'.format(a,b))
# print(f'{a} {b}')

# print('Введите a')
# a = int(input())           ## или float вместо int, зависит от типизации
# print('Введите b')
# b = int(input())
# print (a,'+', b, '=', a+b)

# a = 2
# b = 3
# c = a*b   ## % - остаток от деления ; // - целочисленное деление
# print (c)

# a = 1.23
# b = 3
# c = round(a*b, 5)   ## round - округление до целого, 5 - до скольки знаков после запятой
# print(c)

# a = 3
# a += 5



ЛОГИЧЕСКИЕ ОПЕРАЦИИ:

# a = 1 > 4
# print(a)

# a = 1 < 3 < 5 < 8
# print(a)

# f = 1>2 or 4<6
# print (f)

# f = [1,2,3,4,]
# print(f)
# print (2 in f) # print (not 2 in f)

# is_odd = f[0] % 2 == 0
# is_odd = not f[0] % 2 # по умолчанию в Python 0 - ложь
# print(is_odd)


IF-ELSE:


# a = int(input())
# b = int(input())
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Это же Марина!')
# elif username == 'Саня':
#     print('Саня - ТОП!')
# else:
#     print('Привет,', username)

WHILE:


# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит')
# print(inverted)

FOR:


# for i in 1,2,3,4,5:
#     print(i**2)

# r = range(10)
# r = range(1, 10)
# r = range(1, 10, 2)
# for i in r:
#     print(i)

# for i in 'qwerty':
#     print(i)


НЕМНОГО о СТРОКАХ:
text = 'съешь ещё этих мягких французских булок'


# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) # 

# for c in text:
    # print (c)

# print(text[0])             # с
# print(text[1])             # ъ
# print(text[len(text)])     # IndexError 
# print(text[len(text)-1])   # к
# print(text[-5])            # б
# print(text[:])             # print(text)
# print(text[:1])            # cъ
# print(text[len(text)-2:])  # ок
# print(text[2:9])           # ешь ещё 
# print(text[6:-18])         # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл  (с шагом 6)
# print(text[::6])           # сеикакл  (с шагом 6)
# text = text[2:9] + text[-6] + text[:2]  # ешь ещё съ
# print(text)     


СПИСКИ: ВВЕДЕНИЕ
# list = list

# numbers = [1,2,3,4,5]
# print(numbers)                   # [1,2,3,4,5]
# ran = range(1,6)
# print(type(ran))                 # <class 'range'>
# numbers = list(ran)
# print(type(numbers))             # <class 'list'>

# print(numbers)                   # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers)                   # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i)                     # [20, 4, 6, 8, 10]
# print(numbers)                   # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e)                       # red green blue

# for e in colors:
#     print(e*2)                     # redred greengreen blueblue

# colors.append('grey')              # Добавить в конец
# print(colors)                      # ['red', 'green', 'blue', 'grey']
# print(colors == ['red', 'green', 'blue', 'grey'])  #True
# colors.remove('red')               # удалить по названию
# del colors[0]                      # удалить по номеру элемента


ФУНКЦИИ:

# def f(x):
#     if x ==1:
#         return 'Целое'
#     elif x == 2:
#         return 2
#     else:
#         return

# arg = 3
# print(f(arg))
# print(type(f(arg)))