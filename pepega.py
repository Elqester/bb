print("Введите количество строк и столбцов в прямоугольнике (Через пробел)")
a, b = list(map(int, input().split()))

for m in range(a):
    for n in range(b):
        print('A', sep = '', end = '')
    print()
