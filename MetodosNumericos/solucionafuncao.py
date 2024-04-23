def funcao (x):
    return (-43.44*10**-5)*x**11 + (1.43*10**-2)*x**10 - 0.2*x**9 + 1.71*x**8 - 9.12*x**7 + 31.85*x**6 - 74.58*x**5 + 115.35*x**4 - 113.16*x**3 + 64.41*x**2 - 18.3*x + 2.59

value = float(input("Entre o numero da funcao\n"))

print(funcao(value))