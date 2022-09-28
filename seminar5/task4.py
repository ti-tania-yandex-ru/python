# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def encoder(some_list):
    str_rle = ''
    a = some_list[0]
    k = 0
    for i in range(len(some_list)):
        if some_list[i] == a:
            k += 1
        else:
            str_rle += f'{k}{a}'
            a = some_list[i]
            k = 1
    str_rle += f'{k}{some_list[len(some_list) - 1]}'
    return str_rle


def decoder(some_list):
    normal_str = ''
    i = 0
    while i < len(some_list):
        normal_str += f'{some_list[i + 1] * int(some_list[i])}'
        i += 2
    return normal_str


with open('testfile.txt', 'r', encoding='utf-8') as Str:
    my_list = [i for i in Str.read()]

print(my_list)

print(encoder(my_list))

with open('testfile_encoded.txt', 'w') as data:
    data.write(encoder(my_list))

with open('testfile_encoded.txt') as Str:
    my_list = [i for i in Str.read()]

print(decoder(my_list))
