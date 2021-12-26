# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
# номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.

name = 'название'
price = 'цена'
amount = 'количество'
unit = 'единица изм'
products = []

number = int(input('Введите число товаров в каталоге: '))

for i in range(number):
    product_dict = {}
    prod_name = input(f'Введите {name} товара: ')
    product_dict.update({name: prod_name})
    prod_price = input(f'Введите {price} товара: ')
    product_dict.update({price: prod_price})
    prod_amount = input(f'Введите {amount} товара: ')
    product_dict.update({amount: prod_amount})
    prod_unit = input(f'Введите {unit} товара: ')
    product_dict.update({unit: prod_unit})
    prod_tuple = (i + 1, product_dict)
    products.append(prod_tuple)

print(products)

statistics = {}
names_list = []
prices_list = []
amounts_list = []
units_list = []

for item in products:
    names_list.append(item[-1].get(name))
    prices_list.append(item[-1].get(price))
    amounts_list.append(item[-1].get(amount))
    units_list.append(item[-1].get(unit))

statistics.update({name: names_list})
statistics.update({price: prices_list})
statistics.update({amount: amounts_list})
statistics.update({unit: units_list})

print(statistics)
