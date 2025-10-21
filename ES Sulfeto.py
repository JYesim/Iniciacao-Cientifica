import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
import seaborn as se

#Dados Sulfeto
dse = pd.read_csv("Dinâmica Sulfeto.csv", decimal=",")

for series_name, series in dse.items():
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

plt.title('Frequências Relativas Sulfeto')
plt.xlabel('mg/L')
plt.ylabel('Porcentagem')

plt.show()

#Dados de Treinamento 
dtse = pd.read_csv("Dados de Treinamento Sulfeto.csv", decimal=",")

for series_name, series in dtse.items():
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

plt.title('Frequências Relativas Sulfeto Treinamento')
plt.xlabel('mg/L')
plt.ylabel('Porcentagem')

plt.show()

#Dados de Validação
dvse = pd.read_csv("Dados de Validação Sulfeto.csv", decimal=",")

for series_name, series in dvse.items():
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

plt.title('Frequências Relativas Sulfeto Validação')
plt.xlabel('mg/L')
plt.ylabel('Porcentagem')

plt.show()
