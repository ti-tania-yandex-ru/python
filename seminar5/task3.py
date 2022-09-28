# Создайте программу для игры в ""Крестики-нолики"".


cells = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

game_over = False

for line in cells:
    print(f'{line}')

is_x = False
sign = '0'

while not game_over:
    if is_x:
        print('Ставим крестик: ')
        sign = 'X'
    else:
        print('Ставим нолик: ')
        sign = '0'
    line = int(input('Введите номер ряда: '))
    column = int(input('Введите номер колонки: '))

    for i in range(1, 4):
        for j in range(1, 4):
            if i == line and j == column:
                cells[i - 1][j - 1] = sign

    for arr in cells:
        print(f'{arr}')

    # проверяем комбинации выйгрышей по горизонтали:
    for line in cells:
        game_over = all(line[i] == line[i+1] and line[i] != ' ' for i in range(len(line)-1))
        if game_over:
            break
    if game_over:
        break

    # проверяем комбинации выйгрышей по вертикали:
    for i in range(0, 3):
        game_over = all(cells[j][i] == cells[j+1][i] and cells[j][i] != ' ' for j in range(0, 2))
    if game_over:
        break

    # проверяем комбинации выйгрышей по диагоналям:
    game_over = all(cells[i][i] == cells[i + 1][i + 1] and cells[i][i] != ' ' for i in range(2))
    if game_over:
        break

    game_over = cells[0][2] == cells[1][1] and cells[1][1] == cells[2][0] and cells[1][1] != ' '
    if game_over:
        break

    # проверяем если все поля заполнены, но никто не выйграл:
    full_board = True
    for i in range(3):
        for j in range(3):
            if cells[i][j] == ' ':
                full_board = False
    game_over = full_board

    is_x = not is_x

print('Игра окончена')
