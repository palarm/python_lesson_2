# Математические операции

# Пользовательский ввод

a = int(input('First number: '))
b = int(input('Second number: '))

'''
(?)с точки зрения грамматики и читабельности кода имеет смысл целочисленное присвоение типа переменной 
выводить в одтельную строку или можно собрать в одну? (блок "Пользовательский ввод")
'''

print (a+b)
print (a-b)
print (a*b)
result = a/b

print (type(result))
print (result)

print(a**2)


# Логические операции

a = True
b = False

# Отрицание
print(not a)

# Логическое И
print (a and b)

# Логическое ИЛИ
print (a or b)

# Сравнение
# a = 10
print ('a>100', a>100)
print ('a<100', a<100)
print ('a<=100',a<=100)
print ('a>=100', a>=100)
print ('a==100', a==100)
print ('a!=100', a!=100)
print (a, b)

'''
(?)откуда в блоке "Сравнение" взялось целочисленное значение переменной "а" если 
в блоке "Логические операции" мы присвоили ей булевое значение? 
если содержимое переменной "а" булевое, тогда откуда такие результаты при сравнении со 100?

'''