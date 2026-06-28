import pandas as pd

# ==================================================
# ETAPA 2 - Carregamento do Dataset
# ==================================================

#carregar o arquivo dataset
df = pd.read_csv('data/hotel_bookings.csv')

# Carrega o arquivo CSV contendo os dados das reservas
print(df.head())

