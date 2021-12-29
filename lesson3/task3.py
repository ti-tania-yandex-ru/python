# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

def my_func(x, y, z):
    my_list = [x, y, z]
    my_list.sort(reverse=True)
    return my_list[0] + my_list[1]


print(my_func(1, 2, 3))
print(my_func(18, 2, 4))
print(my_func(18.1, 19.3, 4))
