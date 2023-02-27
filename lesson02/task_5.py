my_list = [7, 5, 3, 3, 2]
my_el = int(input("Введите число рейтинга:"))
for element in range(len(my_list)):
    if my_list[element] == my_el:
        my_list.insert(element + 1, my_el)
        break
    elif my_list[0] < my_el:
        my_list.insert(0, my_el)
    elif my_list[-1] > my_el:
        my_list.append(my_el)
    elif my_list[element] > my_el and my_list[element + 1] < my_el:
        my_list.insert(element + 1, my_el)
print(f"Рейтинг = {my_list}")
