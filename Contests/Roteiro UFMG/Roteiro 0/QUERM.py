def sorteio(lista):
    for num, elem in enumerate(lista):
        #print(elem, num)
        if elem == num + 1:
            return elem

teste = 1
while True:
    n = int(input())
    if n == 0:
        break
    l = list(map(int, input().split()))
    print("Teste %d" % teste)
    if n == l[-1]:
        print(n)
    else:
        print(sorteio(l))
    teste += 1