import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as scipy

csv_0 = pd.read_csv('./data/MSENitrato_7l_0.csv', sep=",")
csv_1 = pd.read_csv('./data/MSENitrato_7l_1.csv', sep=",")
csv_2 = pd.read_csv('./data/MSENitrato_7l_2.csv', sep=",")

#Ordem 0

x = csv_0['Tempo de Residência']
y = csv_0['Concentração']

plt.figure(figsize=(40, 25))
plt.scatter(x, y)
plt.text(2.5,2,"-0.3736 x + 24.16 R² = 0.9319", size='medium', bbox={'facecolor': 'none', 'edgecolor': 'k', 'boxstyle': 'round, pad=1'})

z = np.polyfit(x, y, 1)
p = np.poly1d(z)

print("Função ordem 0")
print(p)

#Cálculo R quadrado
slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

print("Valor de R quadrado para ordem 0")
print (r_value)

#Plot gráfico
plt.plot(x,p(x),"r--")
plt.xlabel('Tempo de Residência')
plt.ylabel('Concentração')
plt.title('Função Ordem 0')
plt.show()

#Ordem 1

x = csv_1['Tempo de Residência']
y = csv_1['ln [C]']

plt.figure(figsize=(10, 10))
plt.scatter(x, y)
plt.text(0.3,0.8,"-0.03813 x + 3.348 R² = 0.9623", size='medium', bbox={'facecolor': 'none', 'edgecolor': 'k', 'boxstyle': 'round, pad=1'})

z = np.polyfit(x, y, 1)
p = np.poly1d(z)

print("Função ordem 1")
print(p)

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

print("Valor de R quadrado para ordem 1")
print (r_value)

plt.plot(x,p(x),"r--")
plt.xlabel('Tempo de Residência')
plt.ylabel('ln [C]')
plt.title('Função Ordem 1')
plt.show()

#Ordem 2 - Linear

x = csv_2['Tempo de Residência']
y = csv_2['1/Ct']

plt.figure(figsize=(0.7, 0.5))
plt.scatter(x, y)
plt.text(0,0.45,"0.006653 x - 0.02546 R² = 0.8625", size='medium', bbox={'facecolor': 'none', 'edgecolor': 'k', 'boxstyle': 'round, pad=1'})

z = np.polyfit(x, y, 1)
p = np.poly1d(z)

print("Função ordem 2")
print(p)

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

print("Valor de R quadrado para ordem 2")
print (r_value)

plt.plot(x,p(x),"r--")
plt.xlabel('Tempo de Residência')
plt.ylabel('1/Ct')
plt.title('Função Ordem 2')
plt.show()
