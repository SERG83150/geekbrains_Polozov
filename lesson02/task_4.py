my_list = []
my_str = input("Введите значение:")
num = 1
for element in range(my_str.count(' ') + 1):
    my_list = my_str.split()
    if len(str(my_list)) <= 10:
        print(f" {num} {my_list[element]}")
        num += 1
    else:
        print(f" {num} {my_list[element][0:10]}")
        num += 1
