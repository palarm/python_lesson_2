# Оператор условия

brand = 'Volvo'     # бренд
engine_volume = 1.5 # объем двигателя
horsepower = 279     # мощность двигателя
sunroof = False     # наличие люка

# Проверка условия if

if horsepower < 80:
    print ('No tax')

# Проверка условия if/else

if horsepower < 80:
    print('No tax')
else:
    print('Tax')

    # "Короткая однострочная запись"
a = horsepower < 80
b = print ('No tax')
c = print ('Tax')

b if a else c


'''
(?) Как корректно оформить короткую однострочную запись для текущей задачи 
(блок "Проверка условия if/else" -> "Короткая однострочная запись")
 

'''

# Проверка условия if/elif/elif/else

tax = 0

if horsepower < 80:
    tax = 0
elif horsepower < 100:
    tax = 10000
elif horsepower < 150:
    tax = 20000
else:
    tax = 50000
print(tax)

# Проверка условия if для присваивания

cool_car = 0

cool_car = 1 if sunroof == 1 else 0
print (cool_car)
