"""задание 4"""
def fun(h):
    k = h - 1
    if h == 0:
        return []
    return fun(k) + [(-1) ** (k % 2) / (1 << k)]


n = int(input())
print(fun(n))
print(sum(fun(n)))
