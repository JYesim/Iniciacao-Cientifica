import pandas as pd
import numpy as np
from numpy import linalg 
import matplotlib.pyplot as plt
import scipy as scipy
import scipy.optimize

csv_0 = pd.read_csv('Sulfetodados0_7l.csv', sep=",")
csv_1 = pd.read_csv('Sulfetodados1_7l.csv', sep=",")
csv_2 = pd.read_csv('Sulfetodados2_7l.csv', sep=",")
csv_v = pd.read_csv('Sulfeto0val.csv', sep=",")

#Ordem 0 

x = csv_0['Tempo de Residência']
y = csv_0['Concentração']

plt.figure(figsize=(10, 10))
plt.scatter(x, y, label='Observado', color='green')
plt.text(0,22,"-0.4677 x + 49.66 R² = 0.9992", size='medium', bbox={'facecolor': 'none', 'edgecolor': 'k', 'boxstyle': 'round, pad=1'})

z = np.polyfit(x, y, 1)
p = np.poly1d(z)

print("Função ordem 0")
print(p)

#Cálculo R quadrado
slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

print("Valor de R quadrado para ordem 0")
print (r_value)

#Plot gráfico
# plt.plot(x,p(x), color='black', linestyle='dashed', linewidth=2)
# plt.xlabel('Tempo de Residência')
# plt.ylabel('Concentração')
# plt.title('Função Ordem 0')
#plt.show()

# Pontos validação
x_v = csv_v['Tempo de Residência']
y_v = -0.4677 * x_v + 49.66

plt.plot(x_v, y_v, marker='x', linestyle='none', color='red', label='Simulado', markersize=7, mew=3)

plt.plot(x_v, y_v, color='black', linestyle='dashed', linewidth=2)
plt.title('Validação Sulfeto Ordem 0')
plt.xlabel('Tempo de Residência')
plt.ylabel('Concentração')
plt.legend() 

# Mostra o gráfico
plt.show()

#Cálculo R quadrado
slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x_v, y_v)

print("Valor de R quadrado para ordem 0 - valid")
print (r_value)

#Ordem 1

# x = csv_1['Tempo de Residência']
# y = csv_1['ln [C]']

# #plt.figure(figsize=(0.7, 0.5))
# #plt.scatter(x, y)
# #plt.text(0,3.1,"-0.01414 x + 3.944 R² = 0.9955", size='medium', bbox={'facecolor': 'none', 'edgecolor': 'k', 'boxstyle': 'round, pad=1'})

# z = np.polyfit(x, y, 1)
# p = np.poly1d(z)

# print("Função ordem 1")
# print(p)

# slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

# print("Valor de R quadrado para ordem 1")
# print (r_value)

# #plt.plot(x,p(x),"r--")
# #plt.xlabel('Tempo de Residência')
# #plt.ylabel('ln [C]')
# #plt.title('Função Ordem 1')
# #plt.show()

# #Ordem 2 - Linear

# x = csv_2['Tempo de Residência']
# y = csv_2['1/Ct']

# plt.figure(figsize=(7, 7))
# plt.scatter(x, y)
# plt.text(1,0.047,"0.000455 x + 0.0177 R² = 0.9754", size='medium', bbox={'facecolor': 'none', 'edgecolor': 'k', 'boxstyle': 'round, pad=1'})

# z = np.polyfit(x, y, 1)
# p = np.poly1d(z)

# print("Função ordem 2")
# print(p)

# slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

# print("Valor de R quadrado para ordem 2")
# print (r_value)

# plt.plot(x,p(x),"r--")
# plt.xlabel('Tempo de Residência')
# plt.ylabel('1/Ct')
# plt.title('Função Ordem 2')
# plt.show()

# # Novos pontos a serem adicionados
# x_v = csv_v['Tempo de Residência']
# y_v = 0.000455 * x_v + 0.0177

# print(y_v)

# # Adiciona os novos pontos ao gráfico
# plt.plot(x_v, y_v, marker='x', linestyle='none', color='red', label='Simulado', markersize=7, mew=3)

# plt.title('Validação Sulfeto Ordem 2')
# plt.xlabel('Tempo de Residência')
# plt.ylabel('1/Concentração')
# plt.legend()

# plt.show()

# slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x_v, y_v)

# print(r_value)

