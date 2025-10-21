import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics as st

#Dados Sulfato
dsa = pd.read_csv("Dinâmica Sulfato.csv", decimal=",")

for series_name, series in dsa.items():
    if series_name == "Medição": continue

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
  - Mínimo: {7}'''
  .format(series_name, media, mediana, moda, desvio_padrao, variancia, max, min))
    
    print("\u0020- Frequência Absoluta")
    print(frequencia_abs)
    print()
    print("\u0020- Frequência Relativa")
    print(frequencia_rel)
    print()

#Gráfico Frequência Relativa 
frequencia_rel.plot(kind='bar')
]
plt.title('Frequências Relativas Sulfato')
plt.xlabel('mg/L')
plt.ylabel('Porcentagem')

plt.show()

#Dados de Treinamento 
dtsa = pd.read_csv("Dados de Treinamento Sulfato.csv", decimal=",")

for series_name, series in dtsa.items():
    if series_name == "Medição": continue

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
  - Mínimo: {7}'''
  .format(series_name, media, mediana, moda, desvio_padrao, variancia, max, min))
    
    print("\u0020- Frequência Absoluta")
    print(frequencia_abs)
    print()
    print("\u0020- Frequência Relativa")
    print(frequencia_rel)
    print()

#Gráfico Frequência Relativa 
frequencia_rel.plot(kind='bar')

plt.title('Frequências Relativas Sulfato Treinamento')
plt.xlabel('mg/L')
plt.ylabel('Porcentagem')

plt.show()

#Dados de Validação
dvsa = pd.read_csv("Dados de Validação Sulfato.csv", decimal=",")

for series_name, series in dvsa.items():
    if series_name == "Medição": continue

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
  - Mínimo: {7}'''
  .format(series_name, media, mediana, moda, desvio_padrao, variancia, max, min))
    
    print("\u0020- Frequência Absoluta")
    print(frequencia_abs)
    print()
    print("\u0020- Frequência Relativa")
    print(frequencia_rel)
    print()

#Gráfico Frequência Relativa 
frequencia_rel.plot(kind='bar')

plt.title('Frequências Relativas Sulfato Validação')
plt.xlabel('mg/L')
plt.ylabel('Porcentagem')

plt.show()