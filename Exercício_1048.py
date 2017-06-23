sal = float(input())

if sal <= 400.00 and sal >= 0:
    r = 15
    Nsal = sal * (r/100)
elif sal <= 800.00:
    r = 12
    Nsal = sal * (r/100)
elif sal <= 1200.00:
    r = 10
    Nsal = sal * (r/100)
elif sal <= 2000.00:
    r = 7
    Nsal = sal * (r/100)
elif sal > 2000.00:
    r = 4
    Nsal = sal * (r/100)

print("Novo salario: %.2f"% (Nsal+sal))
print("Reajuste ganho: %.2f"% Nsal)
print("Em percentual: %d %%"% r)
