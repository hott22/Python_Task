# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

N = int(input('Введи число: '))
data = [1]
for i in range(1,N+1):
    data.append(data[i-1]*i)
del data[0]
print(data)