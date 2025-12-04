import pandas as pd
import numpy as np
from numpy import linalg 
import matplotlib.pyplot as plt
import scipy as scipy
import scipy.optimize

csv_0 = pd.read_csv('Nitratodados0_td.csv', sep=",")
csv_1 = pd.read_csv('Nitratodados1_td.csv', sep=",")
csv_2 = pd.read_csv('Nitratodados2_td.csv', sep=",")
csv_v0 = pd.read_csv('Nitrato0valtd.csv', sep=",")
csv_v1 = pd.read_csv('Nitrato1valtd.csv', sep=",")
csv_v2 = pd.read_csv('Nitrato2valtd.csv', sep=",")

def calculateMSE(ordem, x, y, quantidade):
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)

    y_previsto = p(x)

    print("Lista do y previsto", y_previsto)

    j = [(a - b)**2 for a, b in zip(y, y_previsto)]
    print("Diferença entre as somas: ", j)

    dp = sum(j)
    print("Soma das diferenças", dp)

    MSE = dp/quantidade
    print("MSE para ordem " + ordem + ":", MSE)

#Ordem 0 

x = csv_0['Tempo de Residência']
y = csv_0['Concentração']

z = np.polyfit(x, y, 1)
p = np.poly1d(z)

print("Função ordem 0")
print(p)

#Cálculo R quadrado
slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

print("Valor de R quadrado para ordem 0")
print (r_value)

calculateMSE('0', x, y, len(y))

plt.figure(figsize=(10, 10))
plt.scatter(x, y, label='Observado', color='green')
#plt.text(6000,30,f"{p} R² = {r_value:.4f}", size='medium', bbox={'facecolor': 'none', 'edgecolor': 'k', 'boxstyle': 'round, pad=1'})

plt.plot(x,p(x), color='black', linestyle='dashed', linewidth=2)
plt.xlabel('Tempo de Residência')
plt.ylabel('Concentração')
plt.title('Função Ordem 0')
#plt.show()

# Pontos validação
x_v = csv_v0['Tempo de Residência']
y_v = -0.002119 * x_v + 22.89
y_cv = csv_v0['Concentração']

#print(y_v)

plt.plot(x_v, y_v, marker='x', linestyle='none', color='red', label='Simulado', markersize=7, mew=3)

plt.title('Validação Nitrato Ordem 0')
plt.xlabel('Tempo de Residência')
plt.ylabel('Concentração')
plt.legend() 

plt.show()

#Cálculo R quadrado
slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x_v, y_v)

print("Valor de R quadrado para ordem 0 - valid")
print (r_value)

calculateMSE('0', x_v, y_cv, len(y_cv))

#Ordem 1

x = csv_1['Tempo de Residência']
y = csv_1['ln[C]']

z = np.polyfit(x, y, 1)
p = np.poly1d(z)

print("Função ordem 1")
print(p)

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

print("Valor de R quadrado para ordem 1")
print (r_value)

calculateMSE('1', x, y, len(y))

plt.figure(figsize=(0.7, 0.5))
plt.scatter(x, y)
#plt.text(0,1,f"{p} R² = {r_value:.4f}", size='medium', bbox={'facecolor': 'none', 'edgecolor': 'k', 'boxstyle': 'round, pad=1'})

plt.plot(x,p(x),"r--")
plt.xlabel('Tempo de Residência')
plt.ylabel('ln [C]')
plt.title('Função Ordem 1')
#plt.show()

x_v = csv_v1['Tempo de Residência']
y_v = -0.0002276 * x_v + 3.276
y_cv = csv_v1['ln[C]']

print(y_v)

plt.plot(x_v, y_v, marker='x', linestyle='none', color='red', label='Simulado', markersize=7, mew=3)

plt.title('Validação Nitrato Ordem 1')
plt.xlabel('Tempo de Residência')
plt.ylabel('ln[C]')
plt.legend() 

plt.show()

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x_v, y_v)

print("Valor de R quadrado para ordem 1 - valid")
print (r_value)

calculateMSE('1', x_v, y_cv, len(y_cv))

#Ordem 2 - Linear

x = csv_2['Tempo de Residência']
y = csv_2['1/Ct']

z = np.polyfit(x, y, 1)
p = np.poly1d(z)

print("Função ordem 2")
print(p)

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

print("Valor de R quadrado para ordem 2")
print (r_value)

calculateMSE('2', x, y, len(y))

plt.figure(figsize=(7, 7))
plt.scatter(x, y)
#plt.text(0,0.6,f"{p} R² = {r_value:.4f}", size='medium', bbox={'facecolor': 'none', 'edgecolor': 'k', 'boxstyle': 'round, pad=1'})

plt.plot(x,p(x),"r--")
plt.xlabel('Tempo de Residência')
plt.ylabel('1/Ct')
plt.title('Função Ordem 2')
#plt.show()

x_v = csv_v2['Tempo de Residência']
y_v = 4.144 * 10**-5 * x_v - 0.02135
y_cv = csv_v2['1/Ct']

print(y_v)

plt.plot(x_v, y_v, marker='x', linestyle='none', color='red', label='Simulado', markersize=7, mew=3)

plt.title('Validação Nitrato Ordem 2')
plt.xlabel('Tempo de Residência')
plt.ylabel('1/Ct')
plt.legend() 

plt.show()

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x_v, y_v)

print("Valor de R quadrado para ordem 2 - valid")
print (r_value)

calculateMSE('2', x_v, y_cv, len(y_cv))