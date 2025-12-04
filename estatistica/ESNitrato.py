import statistics as st

import matplotlib.pyplot as plt
import pandas as pd

#Dados Nitrato
dn = pd.read_csv("./data/ESNitrato.csv", decimal=",")
dtn = pd.read_csv("./data/ESNitrato_Treinamento.csv", decimal=",")
dvn = pd.read_csv("./data/ESNitrato_Validacao.csv", decimal=",")

def calculateTudo(data, label = ''):
  for series_name, series in data.items():
    if series_name == "Medição":
      continue

    desvio_padrao = st.stdev(series)
    media = st.mean(series)
    mediana = st.median(series)
    moda = st.mode(series)
    variancia = st.variance(series)
    max = series.max()
    min = series.min()
    frequencia_abs = series.value_counts()
    frequencia_rel = frequencia_abs/series.count()*100

    print ('''[{0}]:
    - Média: {1}
    - Mediana: {2}
    - Moda: {3}
    - Desvio Padrão: {4}
    - Variancia: {5}
    - Máximo: {6}
    - Mínimo: {7}'''.format(series_name, media, mediana, moda, desvio_padrao, variancia, max, min))

    print("\u0020- Frequência Absoluta")
    print(frequencia_abs)
    print()
    print("\u0020- Frequência Relativa")
    print(frequencia_rel)
    print()

    #Gráfico Frequência Relativa
    frequencia_rel.plot(kind='bar')

    plt.title('Frequências Relativas Sulfato ' + label)
    plt.xlabel('mg/L')
    plt.ylabel('Porcentagem')

    plt.show()

calculateTudo(dn)
calculateTudo(dtn, 'Treinamento')
calculateTudo(dvn, 'Validação')
