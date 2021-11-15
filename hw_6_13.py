ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(*ten)

evens = []
for i in ten:
    if i % 2 == 0:
        evens.append(i)
print(*evens)

evens2 = []
for i in evens:
    a = i ** 2
    evens2.append(a)
print(*evens2)

def x(ten):
    while 1:
        a = int(input('Команда для выхода [99]!\nВведите индекс:'))
        if a == 99:
           break
        if a >= len(ten):
            print('Введи правилньный индекс!\nИндекс: от 0 до 9\n')
        else:
            print(ten[a])
x(ten)

while True:
     try:
        ten = int(input('введите первое число :'))
        answer = input('введите знак: + - * / : ')
        second_number = int(input('введите второе  число :'))
     except:
        print('вводите числа !')
        continue
