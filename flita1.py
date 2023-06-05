def converse(array):
    array2 = []
    for elem in array:
        if elem < 0:
            array2.append(bin(elem)[0] + bin(elem)[3:])
        else:
            array2.append(bin(elem)[2:])
    return array2

try:
    print("Введите массив десятичных чисел")
    array = list(map(int, input().split()))
    print("Массив двоичных чисел:")
    print(*converse(array))
except:
    print("Вводите только числа!")