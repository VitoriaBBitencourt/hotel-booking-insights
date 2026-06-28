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

# ==================================================
# ETAPA 3.2 - Análise da coluna 'country'
# ==================================================

# Exibe a quantidade de valores ausentes da coluna 'country'
print("Valores ausentes em 'country':")
print(df["country"].isnull().sum())

print("\n" + "=" * 60)

# Exibe os países mais frequentes na base
print("Países mais frequentes:")
print(df["country"].value_counts().head(10))

# ==================================================
# ETAPA 3.2 - Tratamento da coluna 'country'
# ==================================================

# Preenche valores ausentes da coluna 'country' com "Unknown".
# Essa abordagem preserva todos os registros da base sem atribuir
# incorretamente um país aos hóspedes.
df["country"] = df["country"].fillna("Unknown")

print(df["country"].isnull().sum())

# ==================================================
# ETAPA 4.1 - Total de noites da hospedagem
# ==================================================

# Calcula o número total de noites da reserva
df["total_nights"] = (
    df["stays_in_weekend_nights"] +
    df["stays_in_week_nights"]
)

print(df[[
    "stays_in_weekend_nights",
    "stays_in_week_nights",
    "total_nights"
]].head())

# ==================================================
# ETAPA 4.2 - Total de hóspedes
# ==================================================

# Calcula o número total de hóspedes por reserva
df["total_guests"] = (
    df["adults"] +
    df["children"]
)

print(df[[
    "adults",
    "children",
    "total_guests"
]].head())

# ==================================================
# ETAPA 5 - Análise Exploratória dos Dados (EDA)
# ==================================================

# ==================================================
# ETAPA 5.1 - Reservas por hotel
# ==================================================

# Conta a quantidade de reservas por tipo de hotel
bookings_by_hotel = df["hotel"].value_counts()

print(bookings_by_hotel)

# ==================================================
# ETAPA 5.2 - Taxa de cancelamento
# ==================================================

# Calcula a porcentagem de reservas canceladas
cancellation_rate = df["is_canceled"].mean() * 100

print(f"Cancellation Rate: {cancellation_rate:.2f}%")

# ==================================================
# ETAPA 5.3 - Diária média (ADR)
# ==================================================

# Calcula a diária média das reservas
average_adr = df["adr"].mean()

print(f"Average Daily Rate (ADR): {average_adr:.2f}")

# ==================================================
# ETAPA 5.3.1 - Comparação do ADR por hotel
# ==================================================

# Calcula a diária média de cada hotel
adr_by_hotel = df.groupby("hotel")["adr"].mean()

print(adr_by_hotel)

# ==================================================
# ETAPA 5.5 - Reservas por mês
# ==================================================

# Conta a quantidade de reservas em cada mês
# Ordem cronológica dos meses
month_order = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

# Conta as reservas e organiza os meses em ordem cronológica
bookings_by_month = (
    df["arrival_date_month"]
    .value_counts()
    .reindex(month_order)
)

print(bookings_by_month)
