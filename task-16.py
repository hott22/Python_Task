# Задать список из n чисел последовательности (1+1/n)**n и 
# вывести на экран их сумму
n = int(input('Введи число:'))
data = list(range(1,n+1))
for i in data:
    data[i-1] = (1 + 1/data[i-1])**data[i-1]
    
print(data)

print(round(sum(data), 3))