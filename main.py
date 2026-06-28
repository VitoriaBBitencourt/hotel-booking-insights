import pandas as pd

# ==================================================
# ETAPA 2 - Carregamento do Dataset
# ==================================================

#carregar o arquivo dataset
df = pd.read_csv('data/hotel_bookings.csv')

# Carrega o arquivo CSV contendo os dados das reservas
print(df.head())

# Exibe as primeiras linhas da base para conhecer sua estrutura
print(df.head())

print("\n" + "=" * 60)
print("Informações do DataFrame:")
print("=" * 60)

# Exibe informações sobre colunas, tipos de dados e valores não nulos
print(df.info())

print("\n" + "=" * 60)
print("VALORES NULOS")
print("=" * 60)

# Exibe a quantidade de valores ausentes em cada coluna
print(df.isnull().sum())