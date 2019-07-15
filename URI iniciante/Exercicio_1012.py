ABC = input().split(" ")
a, b, c = ABC
tri = (float(a) * float(c))/2
cir = 3.14159 * (float(c))**2
tra = (float(c)*(float(a)+float(b)))/2
qua = (float(b)**2)
ret = float(a)*float(b)

print("TRIANGULO: %.3f"% tri)
print("CIRCULO: %.3f"% cir)
print("TRAPEZIO: %.3f"% tra)
print("QUADRADO: %.3f"% qua)
print("RETANGULO: %.3f"% ret)
