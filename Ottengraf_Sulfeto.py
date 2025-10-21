import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy

# === Constantes ===
Cin = 0.069
As = 0.125
K0 = 0.4677
diff = 9.2 * (10**-9)
m = 1 * (10**-3)  
fXv = 0.25

b = As * np.sqrt((K0 * fXv * diff) / 2 * m)
df = pd.read_csv("Nitratodados0_7l.csv")

df.columns = ['Tempo de Residência', 'Concentração']

# === Cout ===
def calculate_cout(ebrt):
    term = 1 - b * (ebrt / np.sqrt(Cin))
    return Cin * (term**2)

df['Cout'] = df.apply(lambda row: calculate_cout(row['Tempo de Residência']),
                      axis=1)

print("# === Cout ===")
print(df)

# ===  Ordem 0 ===
x = df['Tempo de Residência']
# y = df['Concentração']
y = df['Cout']

# === Regressão e R ===
print("\n # === Regressão/R ===  ")
plt.figure(figsize=(7, 7))
plt.scatter(x, y)
plt.text(0.0,
         0.0683,
         "-1.121*10^-5 x + 0.069 \n R² = 0.9999",
         size='medium',
         bbox={
             'facecolor': 'none',
             'edgecolor': 'k',
             'boxstyle': 'round, pad=1'
         })

z = np.polyfit(x, y, 1)
p = np.poly1d(z)

print("Função ordem 0")
print(p)

# === Cálculo R quadrado ===
slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

print("\nValor de R quadrado para ordem 0")
print(r_value)

# === Plot gráfico ===
plt.plot(x, p(x), "r--")
plt.xlabel('Tempo de Residência')
plt.ylabel('Concentração')
plt.title('Função Ordem 0')
plt.show()

# === MSE ===
print("\n # === MSE === ")

def calculateTudo(ordem, x, y, quantidade):
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)

    y_previsto = p(x)

    print("Lista do y previsto", y_previsto)

    j = [(a - b)**2 for a, b in zip(y, y_previsto)]
    print("\nDiferença entre as somas: ", j)

    dp = sum(j)
    print("\nSoma das diferenças", dp)

    MSE = dp / quantidade
    print("\nMSE para ordem " + ordem + ":", MSE)

calculateTudo('0', x, y, len(y))