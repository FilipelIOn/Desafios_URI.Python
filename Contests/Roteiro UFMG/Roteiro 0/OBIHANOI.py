hanoi = lambda a : (2**a) - 1
teste = 1
while True:
    n = int(input())
    if n == 0:
        break
    else:
        print("Teste %d"% teste)
        print(hanoi(n),"\n")
        teste += 1