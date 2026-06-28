import pandas as pd

import pandas as pd

# ==================================================
# ETAPA 2.3 - Definição do Escopo da Análise
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

print(df.info())