""" задание 3"""
number = int(input('Введите число: '))
def rec(n,i):
    return i if (n==0) else rec( n//10, i*10 + n%10 )
print(rec(number, 0))
