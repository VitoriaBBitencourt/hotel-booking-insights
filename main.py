import pandas as pd

# ==================================================
# ETAPA 3 - Limpeza dos Dados
# ==================================================

# Carrega o arquivo CSV contendo os dados das reservas
df = pd.read_csv("data/hotel_bookings.csv")

# Mantemos apenas as colunas relevantes para os indicadores
# definidos no escopo do projeto.
columns = [
    "hotel",
    "is_canceled",
    "arrival_date_year",
    "arrival_date_month",
    "stays_in_weekend_nights",
    "stays_in_week_nights",
    "adults",
    "children",
    "country",
    "market_segment",
    "reserved_room_type",
    "adr"
]

# Criamos uma cópia para trabalhar apenas com os dados
# necessários para a análise.
df = df[columns].copy()

# ==================================================
# ETAPA 3.1 - Tratamento da coluna 'children'
# ==================================================

# Preenche valores ausentes da coluna 'children' com 0.
# Como existem apenas 4 registros ausentes, essa abordagem preserva
# as demais informações da reserva sem impactar significativamente a análise.
df["children"] = df["children"].fillna(0)

print(df["children"].isnull().sum())