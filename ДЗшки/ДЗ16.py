#1 case
def is_even(n):
    if n % 2:
        return False
    else:
        return True
print(is_even(4))      

#2 case (v1)
def square(x):
    if x & (x - 1) :
        return False
    else:
        return True
print(square(64))   

#2 case (v2)
def square_2(x):
    if x <= 0: 
        return False
    if x == 1: 
        return True
    return x & 1 == 0 and square_2(x // 2)
print(square_2(120)) 

def square_3(x):
    if x == 1:
        return True
    if x & 1:
        return False
    return square_3(x >> 1)
print(square_3(256))
