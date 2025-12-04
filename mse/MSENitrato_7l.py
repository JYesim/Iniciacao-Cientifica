import numpy as np
import pandas as pd

csv_0 = pd.read_csv('./data/MSENitrato_7l_0.csv', sep=",")
csv_1 = pd.read_csv('./data/MSENitrato_7l_1.csv', sep=",")
csv_2 = pd.read_csv('./data/MSENitrato_7l_2.csv', sep=",")

x0 = csv_0['Tempo de Residência']
y0 = csv_0['Concentração']

x1 = csv_1['Tempo de Residência']
y1 = csv_1['ln [C]']

x2 = csv_2['Tempo de Residência']
y2 = csv_2['1/Ct']

def calculateTudo(ordem, x, y, quantidade):
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

calculateTudo('0', x0, y0, len(y0))
calculateTudo('1', x1, y1, len(y0))
calculateTudo('2', x2, y2, len(y0))
