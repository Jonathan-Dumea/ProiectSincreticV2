# Relatie de recurenta numere fibonacci:
# F0 = 0, F1 = 1, Fi = Fi-1 + Fi-2, pentru i >= 2

# Acest program afiseaza numerele fibonacci mai mici sau egale cu N
def fib(n):
    f1 = 0
    f2 = 1

    if n < 0:
        print("Nu exista numere mai mici decat 0 in sirul fibonacii.")
        return

    print(f1, end=" ")

    while f2 <= n:
        print(f2, end=" ")
        f3 = f1 + f2
        f1 = f2
        f2 = f3

n = int(input('Introduceti un numar: '))

fib(n)


