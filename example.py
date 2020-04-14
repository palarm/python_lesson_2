# Задачи на циклы и оператор условия

'''
Задача 1

Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована
'''

for i in range(5):
    print(i + 1, '0000000000000000000000')

'''
Задача 2

Пользователь в цикле вводит 10 цифр. Найти количество введенных пользователем цифр 5
'''

# Первый вариант

print('Приготовьтесь, будем вводить 10 цифр!')
counter = 0
for i in range(1, 11, 1):
    take_input = input('Введите любую цифру под № '+ str(i) + ': ')
    if int(take_input) == 5: counter += 1
print('Из 10 цифр Вы', counter, 'раз(а) ввели цифру 5!')

# Второй вариант (с обработкой вводимых данных)

print('Приготовьтесь, будем вводить 10 цифр!')
counter = 0
#is_int = False
j = 0
i = 1

#for i in range(1, 11, 1):
while i < 11:
    take_input = input('Введите любую цифру под № '+ str(i) + ': ')

    if len(take_input) > 1:
        print ('Это больше чем цифра! Попробуйте еще раз')
        continue
    elif len(take_input) < 1:
        print('Вы ничего не ввели! Попробуйте еще раз')
        continue
    #elif is_int == False:
    for j in range(11):
        if str(j) == take_input:
            print('Это какая-то цифра')
            i += 1
            #is_int = True
            if int(take_input) == 5: counter += 1
            #print(j, 'before break')
            break
        if j == 10:
            #print(j, 'after break')
            print('Это не цифра, а что-то другое')
            continue

print('Из 10 цифр Вы', counter, 'раз(а) ввели цифру 5!')


'''
(?) получается обязательно выполнять приведение типов, иначе код не будет корректно исполняться?
(?) насколько эффективнен второй вариант кода? можно ли его как-то оптимизировать?
'''

'''
Задача 3

Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран
'''

sum = 0

for i in range(1,101):
    sum += i

print (sum)

'''
Задача 4

Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран
'''
multipl = 1

for i in range(2,10):
    multipl *= i

print (multipl)

'''
Задача 5

Вывести цифры числа на кадой строчке
'''

# Вариант 1

integer_number = int(input('Введите любое целое число: '))

#print (integer_number%10, integer_number//10)

while integer_number > 0:
    print (integer_number%10)
    integer_number = integer_number//10

# Вариант 2 (обратное выведение. от старшего разряда к младшему)

integer_number = int(input('Введите любое целое число: '))
len_input_num = len(str(integer_number))
num_of_digit = len_input_num - 1

while num_of_digit >= 0:
    a = integer_number//10**num_of_digit
    integer_number = integer_number - a*10**num_of_digit
    #print (integer_number//10**num_of_digit)
    print(a)
    num_of_digit -= 1


# Вариант 3

integer_number = input('Введите любое целое число: ')
len_input_num = len(integer_number)
pos = 0

#while len(integer_number) > pos:
while len_input_num > pos:
    print (integer_number[pos])
    pos += 1

'''
(?) Второй вариант получился какой-то корявый. Как можно упростить?
(?) Если не вводить дополнительную переменную длины строки, то в цикле при каждой итерации будет выполняться
    вычисление длины строки? (Вариант 3)
'''

'''
Задача 6

Найти сумму цифр числа
'''

integer_number = input('Введите любое целое число: ')
len_input_num = len(integer_number)
pos = 0
result = 0

while len_input_num > pos:
    result += int(integer_number[pos])
    pos += 1

print (result)

'''
Задача 7

Найти произведение цифр числа
'''
integer_number = input('Введите любое целое число: ')
len_input_num = len(integer_number)
pos = 0
result = 1

while len_input_num > pos:
    result *= int(integer_number[pos])
    pos += 1

print (result)

'''
Задача 8

Дать ответ на вопрос: если ли среди цифр числа 5?
'''

integer_number = 2153413
while integer_number>0:
    print(integer_number%10)
    if integer_number%10 == 5:
        print(integer_number%10)
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')




'''
Задача 9

Найти максимальную цифру в числе
'''
integer_number = int(input('Введите любое целое число: '))
is_max_num = 0

while integer_number>0:

    if integer_number%10 >= is_max_num:
        is_max_num = integer_number%10

    integer_number = integer_number//10

print ('Максимальная цифра в заданном числе: ', is_max_num)


'''
Задача 10

Найти количество цифр 5 в числе
'''

'''
(!) получается решение этой задачи уже продемонстрировано в задаче 2
'''