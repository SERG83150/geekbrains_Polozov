n = int(input("Введите целое положительное число:"))
max1 = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max1:
        max1 = n % 10
    elif n > 9:
        pass
print("Максимальное цифра в числе ", max1)

