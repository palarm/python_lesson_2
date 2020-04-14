# Динамическая типизация

# temp_var_1 = input('Input something')
# print ('temp_var_1', temp_var_1, type(temp_var_1), id(temp_var_1))
#
# temp_var_2 = input('Input something again')
# print ('temp_var_2', temp_var_2, type(temp_var_2), id(temp_var_2))
#
# temp_var_1 = temp_var_2
#
# print ('temp_var_1', temp_var_1, type(temp_var_1), id(temp_var_1))
# print ('temp_var_2', temp_var_2, type(temp_var_2), id(temp_var_2))

# Приведение типов

temp_float = input('Input float number')
print ('temp_float', temp_float, type(temp_float), id(temp_float))

try:
    temp_float = float(temp_float)
# except TypeError:
#     print('Wrong type!')
except ValueError:
    print('Wrong type!')
else:
    print('temp_float', temp_float, type(temp_float), id(temp_float))
finally:
    print('ok')

'''
(?) насколько корректен такой подход в обработке ошибки?
'''

# if temp_float:
#     temp_float = float(temp_float)
#     print('temp_float', temp_float, type(temp_float), id(temp_float))
# else: print('Wrong type!')


