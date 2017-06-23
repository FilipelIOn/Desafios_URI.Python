x = input().split(" ")
c, v = x

cod = int(c)
valor = int(v)

if cod == 1:
    print("Total: R$ %.2f"% (valor * 4.0))
elif cod == 2:
    print("Total: R$ %.2f"% (valor * 4.5))
elif cod == 3:
    print("Total: R$ %.2f"% (valor * 5.0))
elif cod == 4:
    print("Total: R$ %.2f"% (valor * 2.0))
elif cod == 5:
    print("Total: R$ %.2f"% (valor * 1.5))
