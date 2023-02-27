time = int(input("Введите время в секундах:"))
hour = time // 3600
minutes = (time - hour * 3600) // 60
second = time - (hour * 3600 + minutes * 60)
print(f"Время - {hour}: {minutes}:{second}")
