import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as scipy

csv = pd.read_csv('./data/Michaellis_Sulfato.csv', sep=",")

x = csv['Cout']
y = csv['Cout/(Ci-Cout)']

plt.figure(figsize=(5, 5))
plt.scatter(x, y)
plt.text(122,-6,"0.8307x - 119.7 R² = 0.9392", size='medium', bbox={'facecolor': 'none', 'edgecolor': 'k', 'boxstyle': 'round, pad=1'})

z = np.polyfit(x, y, 1)
p = np.poly1d(z)

print("Função Michaellis Sulfato: ")
print(p)

#Cálculo R quadrado
slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

print("Valor de R quadrado para Menten Sulfeto")
print (r_value)

#Plot gráfico
plt.plot(x,p(x),"r--")
plt.xlabel('Cout')
plt.ylabel('Cout/(Ci-Cout)')
plt.title('Menten Sulfato')
plt.show()

km = 1/0.8307

ks = 119.7*km

print("Km (taxa máxima de reação): ")
print(km)

print ("Ks (meia saturação): ")
print(ks)
