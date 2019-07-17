def fatorial (n):
    fat = 1;
    i = 2
    while i <= n:
        fat = fat * i
        i += 1
    return fat

while True:
    try:
        num = list(map(int, input().split()))
        resultado = fatorial(num[0]) + fatorial(num[1])
        print(resultado)

    except EOFError:
        break