print('Hello, motherfucker!')
#что-то странное
print('QA is the best')  #but it's not 100%
print("I'm")
print('QA-ing')
#так не надо, лучше в разных строках
print(10 + 18.6)
# 154 + 12.97  #он посчитает, но не отобразит в консоли без print
print((5 * 456 - 1546) * 0.2)
print(156 / 15.6)
print('-How are you?\n-Good')
print('hello,' + ' my friend')
print('"I\'m your father"')
print(chr(37))  #эта команда chr выдает знаки из таблицы Ascii

test = "QA Engineer"  #создали переменную test со значением QA Engineer
print(test)  # функцией print вывели значение переменной на экран

a = (10)
b = (20)
print(a + b)

name = 'Marina'
lastname = 'Ivanova'
print(name + ' ' + lastname)
lastname = 'Tatarova'
print(name + ' ' + lastname)

euro_count = 100
usd = euro_count / 1.25
rub = usd * 81
print(usd)
print(rub)

a = str(0.346)
print((a), (type(a)))

city = 'Saint-Petersburg'
adress = f'{city}, Russia'
print(adress)

my_name = 'Kirill Poteryashin'
fact = f'{my_name}, The Best'
print(fact)

name = 'Michael'
last_name = 'Jackson'
middle_name = 'Joseph'
mjj = f'Dear {name} {middle_name[0]}. {last_name[0]}.'
print(mjj)

a = pow(2,5)
print(a)

x = round(5.76543, 2)
print(x)

a = 1
b = 3
c = 5
print(max(a, b, c))

my_name = 'Kirill'
print(my_name.upper(), '- The Best')

def show_name():
    name = 'Kirill'
    last_name = 'Poteryashin'
    full_name = name + ' ' + last_name
    return full_name
print(show_name())

def show_upper_name(name):
    return name.upper()
print(show_upper_name('Kirill'))

#программа посчитает длину заданной строки(text)
def string_len(text):
    return len(text)
print(string_len('abracadabra'))

def show_lower_name(name, last_name):
    return name.lower(),last_name.lower()
print(show_lower_name('KIRILL', 'POTERYASHIN'))

def pow(x,y,a):
    return x ** y + a
print(pow(2,5,8))

#функция принимает на вход 5 аргументов, 
#первые два обязательные, остальные -нет.
def func (a, b, c=150, d=500, e=125) :
    return a * b + c + d + e
print(func(5,85))

#тут что-то пошло не так, надо разбираться
def power(a: str, b: str):
    return a+b
print(power('5','6'))

#проверяет возраст
def show_age(age):
    return age>=18
print(show_age(18))

def test_func(a):
    if a>10:
        return a+100
    else:
        return a-50
print(test_func(40)) 
