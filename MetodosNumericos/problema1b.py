import matplotlib.pyplot as plt
import numpy as np

def function_j(j):
    return (1 - (1 + j) ** -12) / j - 8.498

x_axis = np.linspace(0.001, 12, 200) 

y_axis = function_j(x_axis)

plt.plot(x_axis, y_axis)
plt.xlabel('Mensalidades')
plt.ylabel('Valor')
plt.title('Gráfico da função (1-(1+j)**-12)/j - 8.498')

plt.show()