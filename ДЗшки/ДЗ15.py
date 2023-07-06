#1st PART OF HW

#1 case
def count_chars(string, char=None):
    if char != None:
        return string.count(char)
    else:
        return len(string)    
print(count_chars('Hello, bro!','o')) #2

#2 case (v1)
def factorial(n):
    x=1
    for i in range(2,n+1):
        x=x*i
    return x
print(factorial(6)) #720

#2 case (v2)
def factorial_2(n):
    if n == 1:
        return 1
    return factorial_2(n - 1) * n
print(factorial_2(8)) #40320

#3case
def string_manipulation(a:str,reverce=True):
    if reverce == True:
        return a[::-1]
    else:
        return a.upper()
print(string_manipulation('paradox',False)) #PARADOX

#2nd PART OF HW

#1 case
def find_min_max():
    numbers = (150, 400, 800, 555, 145, 815)
    return min(numbers),max(numbers)
print(find_min_max()) #(145, 815) , <class 'tuple'>

#2 case (v1)
def sum_of_digits(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return sum
print(sum_of_digits(1586)) #20
#2 case (v2)
def sum_of_digits2():
    x= 9678
    return sum(map(int,str(x)))
print(sum_of_digits2()) #30

#3 case (v1)
def sum_numbers():
    numbers = (15, 10, 25, 5, 4, 3, 2, 1)
    return sum(numbers)
print(sum_numbers()) #65

#3 case (v2)
def sum_numbers_2(x, y, z, a, b):
    return x + y + z + a + b
print(sum_numbers_2(45, 15, 10, 79, 18)) #167