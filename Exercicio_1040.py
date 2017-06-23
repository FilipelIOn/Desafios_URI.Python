media = input().split(" ")
n1, n2, n3, n4 = media

N1 = float(n1)
N2 = float(n2)
N3 = float(n3)
N4 = float(n4)

MP = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10
print("Media: %.1f"% MP)

if MP >= 7.0:
    print("Aluno aprovado.")
elif MP < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    EX = float(input())
    print("Nota do exame: %.1f"% EX)
    if ((MP + EX)/2) <= 5.0:
        print("Aluno reprovado.")
        print("Media final: %.1f"% ((MP + EX)/2))
    else:
        print("Aluno aprovado.")
        print("Media final: %.1f"% ((MP + EX)/2))
