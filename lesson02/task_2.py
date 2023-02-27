my_list = []
quantity = int(input("Введите количество элементов:"))
index = 0
while index < quantity:
    my_list.append(input("Введите значение элемента:"))
    index = index + 1
print(my_list)
element = 0
for elements in range(int(len(my_list)/2)):
        my_list[element], my_list[element + 1] = my_list [element + 1], my_list[element]
        element = element + 2
print(my_list)
