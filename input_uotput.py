# использование оператора print с дополнительными параметрами

print('Тестовая', 'строка', 'с', 'разделителем', 'и', 'финалом', sep='_', end='!\n')
print('Test', 'line', 'with', 'separator', '&', 'final char', sep='_', end='!\n\n')

'''
(?)почему второй print при отладке не выводится с новой строки? в видео автор не добавлял служебных символов, 
тем не менее каждый новый принт у него начинался с новой строки. где подвох?  

(!) решение: \n 
    набор служебных символов https://pythonworld.ru/tipy-dannyx-v-python/stroki-literaly-strok.html
'''


# Ввод текста

name = input('Input your name: ')
print (name)

age = input('Input your age: ')
print (int(age), type(int(age)))
print (type(age))

'''
(?)получается присвоение нового типа переменной условно? 22 строка (последняя строка кода) возвращает str!  

'''