minuto = 0
hora = 0
segundo = 0
n = int(input())
while True:
    if n >= 60:
        n -=60
        minuto += 1
    elif minuto >= 60:
        minuto -= 60
        hora += 1
    else:
        segundo = n
        break
print("%d:%d:%d"%(hora,minuto,segundo))
