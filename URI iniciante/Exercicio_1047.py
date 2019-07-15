h = input().split(" ")
i, mi, f, mf = h

i = int(i) #Transforma hora inicial em inteiro
f = int(f) #Transforma hora final em inteiro
d = 0
horas = 0

if ((i and f) <= 24) and ((i and f) >= 0):
    if i > f:
        d = 24 - i
        horas = d + f
        HORA = ("O JOGO DUROU %d HORA(S)"% horas)
    elif i < f:
        horas = f - i
        HORA = ("O JOGO DUROU %d HORA(S)"% horas) #Armazena
    else:
        HORA = ("O JOGO DUROU 24 HORA(S)") # 24 HORAS

if (i == f) and not (mi == mf):
    horas = 0
    HORA = ("O JOGO DUROU %d HORA(S)"% horas)


mi = int(mi) #Transforma minuto inicial em inteiro
mf = int(mf) #Transforma minuto final em inteiro

controlador = 0
if mi <= mf:
    controlador += 1
    minutos = mf - mi
    MINUTO = ("E %d MINUTO(S)"% minutos)
else:
    horas -= 1
    minutos = 60 - (mi - mf)
    MINUTO = ("E %d MINUTO(S)"% minutos)
    HORA = ("O JOGO DUROU %d HORA(S)"% horas)

if (mi > mf) and (i < f) and controlador == 1:
    horas = 0
    HORA = ("O JOGO DUROU %d HORA(S)"% horas)

print("%s %s"%(HORA, MINUTO))
