# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

size = int(input('Введите размер списка: '))
items = []
last_item = None

for x in range(size):
    item = int(input('Введите целое число: '))
    items.append(item)

print(f'Список в первоначальном виде: {items}')

if size % 2 == 1:
    last_item = items.pop()

for i in range(0, len(items), 2):
    item = items[i]
    items[i] = items[i + 1]
    items[i + 1] = item

if last_item:
    items.append(last_item)

print(f'Список в измененном виде: {items}')
