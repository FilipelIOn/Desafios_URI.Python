anos = 0
meses = 0
dias = 0
n = int(input())
while True:
    if n >= 365:
        n -=365
        anos += 1
    elif n >= 30:
        n -= 30
        meses += 1
    else:
        dias = n
        break
print("%d ano(s)"%anos)
print("%d mes(es)"%meses)
print("%d dia(s)"%dias)
