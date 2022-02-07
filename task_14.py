# Подсчитать сумму цифр в вещественном числе

a = input('Введи вещественное число: ')
data = list(a)
for i in data:
    if i == '.':
        data.remove(".")
    elif i == "-":
        data.remove("-")
result = [int(i) for i in data]
print('сумма цифр числа', a, '=',sum(result))