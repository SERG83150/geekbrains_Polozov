revenue = int(input("Введите сумму выручки в рублях:"))
costs = int(input("Введите сумму издержек в рублях:"))
if revenue > costs:
    profit = revenue - costs
    print(f"Вы получили прибыль в размере {profit} рублей.")
elif revenue == costs:
    print(f"Вы не получили ни прибыли, ни убытка")
else:
    loss = costs - revenue
    print(f"Вы получили убыток в размере {loss} рублей")
