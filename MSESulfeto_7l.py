import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Ordem 0 

csv_0 = pd.read_csv('Sulfetodados0_7l.csv', sep=",")

x = csv_0['Tempo de Residência']
y = csv_0['Concentração']

z = np.polyfit(x, y, 1)
p = np.poly1d(z)

def e_prevista(x, y):
    return p(x)

y_previsto = e_prevista(x, y)
print("Lista do y previsto", y_previsto)

j = [(a - b)**2 for a, b in zip(y, y_previsto)]
print("Diferença entre as somas: ", j)

dp = sum(j)
print("Soma das diferenças", dp)

MSE = dp/4
print("MSE para ordem 0: ", MSE)

#Ordem 1

csv_1 = pd.read_csv('Sulfetodados1_7l.csv', sep=",")

x = csv_1['Tempo de Residência']
y = csv_1['ln [C]']

z = np.polyfit(x, y, 1)
p = np.poly1d(z)

def e_prevista(x, y):
    return p(x)

y_previsto = e_prevista(x, y)
print("Lista y previsto", y_previsto)

j = [(a - b)**2 for a, b in zip(y, y_previsto)]
print("Diferença entre as somas: ", j)

dp = sum(j)
print("Soma das diferenças", dp)

MSE = dp/8
print("MSE para ordem 1: ", MSE)

#Ordem 2

csv_2 = pd.read_csv('Sulfetodados2_7l.csv', sep=",")

x = csv_2['Tempo de Residência']
y = csv_2['1/Ct']

z = np.polyfit(x, y, 1)
p = np.poly1d(z)

def e_prevista(x, y):
    return p(x)

y_previsto = e_prevista(x, y)
print("Lista y previsto", y_previsto)

j = [(a - b)**2 for a, b in zip(y, y_previsto)]
print("Diferença entre as somas: ", j)

dp = sum(j)
print("Soma das diferenças", dp)

MSE = dp/8
print("MSE para ordem 2: ", MSE)
