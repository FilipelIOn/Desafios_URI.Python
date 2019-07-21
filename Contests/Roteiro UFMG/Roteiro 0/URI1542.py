def qdp(n):
    Q = int(n[0])
    D = int(n[1])
    P = int(n[2])
    return int(((Q * D) / (P - Q))*P)

n = (str(input()).split())
while int(n[0])!=0:
    if qdp(n) == 1:
        print("1 pagina")
    else:
        print(qdp(n), "paginas")
    n = (str(input()).split())