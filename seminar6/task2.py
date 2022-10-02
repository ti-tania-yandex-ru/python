# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

search_text = 'абв'
some_text = 'Фыв ава ввабвм рраббб, раб. Аб в и овалз тьллл ыкку аабввв.'
final_text = ''

# Старое решение -

words = some_text.split()
for word in words:
    if search_text not in word:
        final_text = f'{final_text}{word} '

print(some_text)
print(final_text)

# Новое решение с использованием filter и lambda

print(' '.join(filter(lambda txt: 'абв' not in txt, words)))
