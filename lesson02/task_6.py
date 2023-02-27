products = []
features = {'Название': '', 'Цена': '', 'Количество': '', 'Ед.': ''}
analytics = {'Название': [], 'Цена': [], 'Количество': [], 'Ед.': []}
num = 0
feature = None
control = None
while True:
    control = input("Для выхода нажмите 'Q', Дл ввода данных 'Enter', Для вывода данных 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Current analytics \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature = input(f'Input feature "{f}"')
        features[f] = int(feature) if (f == 'price' or f == 'quantity') else feature
        analytics[f].append(features[f])
    products.append((num, features))

products = int(input("Введите количество товара "))
n = 1
my_dict = []
my_list = []
my_analys = {}
while n <= products:
    my_dict = dict({'название': input("введите название "), 'цена': input("Введите цену "),
                    'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
    my_list.append((n, my_dict))
    n += 1
    my_analys = dict(
        {'название': my_dict.get('название'), 'цена': my_dict.get('цена'), 'количество': my_dict.get('количество'),
         'ед': my_dict.get('ед')})
print(my_list)
print(my_analys)