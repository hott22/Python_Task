                        # тип данных и переменные
value = None  # временное значение переменной
a = 123
b = 1.23
print(a)
print(b)
value = 12345
print(value)
print(type(a))  # type - Тип данных
print(type(b))
print(type(value))
s = 'hello world'
print(s)  # вывод строки
print(type(s))
d = 'hello \nworld'  # \n - переход на новую строку
print(d)
print(a, b, s)
print(a, '-', b, '-', s)
print('{2} - {1} - {0}'.format(a, s, b))  # порядок выводы
print(f'{a} - {b} - {d}')

f = True  # логическая переменная
print(f)

                           # списки, массивы

list = [1, 2, 3]
print(list)
list2 = ['1','2', '3', 'hello world', 1, 2, 3, 1,23, True]
print(list2)

                       # ввод и вывод данных 
print('введите a')
a = input()
print('введите b')
b = input()
print(a,b)
print('{} {}'.format(a,b))
print(f'{a} {b}')
print(a, '+',b, '=', a+b) # результат 20 + 23 = 2023

print('введите с')
c = int(input())
print('введите d')
d = int(input())
print(c, '+',d, '=', c+d) # результат 20 + 23 = 43

                   # арифметические операции
g = 12
h = 8
j = g / h # // - целое численное деление, ** - возведение в степень
print(j)
k = 1.3
l = 3
m = round(k * l, 3) # round() - округление 
print(m)

x = 5
x = x + 3 # или x += 3

                   # логичесие операции
a = 3 > 4 and 4 < 5
print(a) # false
func = [1,2,3,4]
print(func)
print( 2 in func) # true

                    # if, else
a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

username = input('введите имя: ')
if username == 'Маша':
    print('Ура, это же Маша!')
elif username == 'Коля':
    print('Здорова Коля!')
else:
    print('Привет, ', username)

                    # циклы while , for

original = 23
inverted = 0
while original !=0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('ПоЖалуй хватит')
print(inverted)  

for i in 1,2,3,4,5:
    print(i**2) # демонтарция квадратов чисел

list = [1,2,3,4,5]
for i in list:
    print(i) # демонстрация списка
    
r = range(9)
for i in r:
    print(i) # демонастрация от 0 до 8

for i in range(1, 5):
    print(i) # печать от 1 до 4

for i in range(1, 10, 2):
    print(i) # печать от 1 до 9 с шагом 2

for i in 'qwert - y':
    print(i) # печать посимвольно

                     # строки

text = 'съешь этих мягких французских булок'
print(len(text)) # количество символов - 39
print('еще' in text) # True
print(text.isdigit()) # False
print(text.replace('еще','ЕЩЕ')) # замена слова
print(text[0]) # с
print(text[-5]) # б
print(text[:]) # весь текст
print(text[:2]) # съ
print(text[2:5]) # ешь

ran = range(1,6)
numbers = list(ran)
print(numbers) # 1 2 3 4 5
numbers[0] = 10 # присваиваем 0 элементту 10
print(len(numbers))  # 5

colors = ['red', 'blue', 'green']
for e in colors:
    print(e*2) # redred blueblue greengreen


                         # функции
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
arg = 1
print(f(arg))