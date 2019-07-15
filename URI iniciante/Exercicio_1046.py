h = input().split(" ")
i, f = h

i = int(i)
f = int(f)
d = 0
horas = 0

if ((i and f) <= 24) and ((i and f) >= 0):
    if i > f:
        d = 24 - i
        horas = d + f
        print("O JOGO DUROU %d HORA(S)"% horas)
    elif i < f:
        horas = f - i
        print("O JOGO DUROU %d HORA(S)"% horas)
    else:
        print("O JOGO DUROU 24 HORA(S)")
