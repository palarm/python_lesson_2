# Цикл While

i = 0
while i < 10:
    print(i)
    i = i + 1
    if i == 5: break


answer = None
i = -1
while answer!='Volvo':
    i = i + 1
    if i == 0:
        answer = input('Какая лучшая марка автомобиля?')
    elif i == 1:
        answer = input('А если подумать?')
    elif i == 2:
        answer = input('Еще одна попытка:')
    else:
        print('Ну нет же! Давай начнем с начала!')
        i = -1

print('Вы абсолютно правы!')