a = int(input("Сколько километров пробежали сегодня в км:"))
b = int(input("Цель в км."))
day = 1
result = a
while result < b:
    print(f"{day}-й день = {result} км.")
    day = day + 1
    result = round(result + result * 0.1, 2)
print(f"Цель будет достигнута на {day} день")
