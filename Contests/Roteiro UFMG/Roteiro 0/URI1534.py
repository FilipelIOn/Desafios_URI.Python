while True:
    try:
        x = 0
        tam = int(input())
        for i in range(tam):
            linha = []
            for j in range(tam):
                if (j == x) and (j == (tam - x - 1)):
                    linha.append(2)
                elif j == x:
                    linha.append(1)
                elif j == (tam - x - 1):
                    linha.append(2)
                else:
                    linha.append(3)
            [print(p, end="") for p in linha]
            print()
            x += 1

    except EOFError:
        break