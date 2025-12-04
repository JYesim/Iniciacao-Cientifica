import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as scipy

csv = pd.read_csv('./data/Michaellis_Sulfeto_Conferencia.csv', sep=",")

x = csv['c_out']
y = csv['c_out/(c_in_c_out)']

def calculateTudo(x, y, quantidade):
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)

    y_previsto = p(x)

    print("Lista do y previsto", y_previsto)

    j = [(a - b)**2 for a, b in zip(y, y_previsto)]
    print("Diferença entre as somas: ", j)

    dp = sum(j)
    print("Soma das diferenças", dp)

    MSE = dp/quantidade
    print("MSE para Menten do Sulfeto de Hidrogênio", MSE)

calculateTudo(x, y, len(y))

plt.figure(figsize=(5, 5))
plt.scatter(x, y)
plt.text(20.3,3.5,"0.01622 x - 2.865 R² = 0.9673", size='medium', bbox={'facecolor': 'none', 'edgecolor': 'k', 'boxstyle': 'round, pad=1'})

z = np.polyfit(x, y, 1)
p = np.poly1d(z)

print("Função Michaellis Sulfeto: ")
print(p)

#Cálculo R quadrado
slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

print("Valor de R quadrado para Menten Sulfeto")
print (r_value)

#Plot gráfico
plt.plot(x,p(x),"r--")
plt.xlabel('Cout')
plt.ylabel('Cout/(Ci-Cout)')
plt.title('Menten Sulfeto de Hidrogênio')
plt.show()

km = 1/0.01612

ks = 2.865*km

print("Km (taxa máxima de reação): ")
print(km)

print ("Ks (meia saturação): ")
print(ks)
