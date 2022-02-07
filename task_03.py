# Вывести на экран числа от -N до N

N = int(input('Введи число: '))
r = range(-N, N+1)
# for i in r:
#      print(i*2) # умножение кажждого элемента на 2


numbers = list(r)
print(numbers)