"""Задание 2"""

m = int(input("Введите число: "))

def fun(n=m, even=0, odd=0):
    if n == 0:
        return even, odd
    else:
        c_n = n % 10
        n = n // 10
        if c_n % 2 == 0:
            even += 1
        else:
            odd += 1
        return fun(n, even, odd)

print(fun(m))
