#1 case (v1)
value = 426.569456546456
print(round(value,3))
#1case (v2)
value = 426.569456546456
new_value = round(value,3)
print(new_value)

#2 case
value = 775
a = hex(value)
print(a)

#3 case (v1)
first_name = 'Michael'
last_name = 'Jackson'
middle_name = 'Joseph'
total = len(first_name),len(last_name),len(middle_name)
print(sum(total))
#3 case (v2)
first_name = 'Michael'
last_name = 'Jackson'
middle_name = 'Joseph'
print(len(first_name)+len(last_name)+len(middle_name))

#4 case
value = 3.66
upd_value = str(value)
print(upd_value, type(upd_value))

#5 case (v1)
a = '15024'
a1 = int(a)
print(a1, type(a1))
print(bin(a1))
#5 case (v2)
def my_prog1():
    a = '15024'
    a1 = int(a)
    a2 = a1, type(a1)
    print(a2)
    return bin(a1)
print(my_prog1())
#5 case (v3)
def my_prog2():
    a = '15024'
    a1 = int(a)
    print(a1, type(a1))
    return bin(a1)
print(my_prog2())
#5 case (v4)
def my_prog3():
    a = '15024'
    a1 = int(a)
    a2 = type(a1)
    a3 = bin(a1)
    a_total = str(a1) +', ' + str(a2) + ', ' + a3
    return a_total
print(my_prog3())

#6 case
text = 'Bilbo Baggins'
print(text[::-1])

#7 case
x = min(5, 7, 0, 3, 5, 9)
x1 = str(x)
print(x1, ', ', type(x1))

def eastern_wisdom():
    text1 = '"Test it, or die trying"'
    text2 = 'Eastern wisdom: '
    return text2+text1
print(eastern_wisdom())