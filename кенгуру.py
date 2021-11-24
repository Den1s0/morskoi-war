m=int(input ('Введите длину дороги n:'))
def f(n):
    if n==0:
        return 1
    if n<0:
        return 0
    return f(n-1) + f(n-2) + f(n-3) + f(n-4) + f (n-5)
print(f (m))
