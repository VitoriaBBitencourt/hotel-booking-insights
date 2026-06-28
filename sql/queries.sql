-- ==================================================
-- HOTEL BOOKING INSIGHTS
-- SQL QUERIES
-- ==================================================

-- Projeto:
-- Hotel Booking Insights

-- Objetivo:
-- Reproduzir em SQL os principais indicadores obtidos
-- durante a análise exploratória realizada em Python.

-- Banco:
-- SQLite

-- Tabela:
-- hotel_bookings

-- ==================================================
-- ETAPA 6.2 - Reservas por hotel
-- ==================================================

-- Pergunta de negócio:
-- Qual hotel recebeu o maior número de reservas?

SELECT
    hotel,
    COUNT(*) AS total_bookings
FROM hotel_bookings
GROUP BY hotel
ORDER BY total_bookings DESC;

-- ==================================================
-- ETAPA 6.2 - Reservas por hotel
-- ==================================================

-- Pergunta de negócio:
-- Qual hotel recebeu o maior número de reservas?

SELECT
    hotel,
    COUNT(*) AS total_bookings
FROM hotel_bookings
GROUP BY hotel
ORDER BY total_bookings DESC;

-- ==================================================
-- ETAPA 6.4 - ADR médio por hotel
-- ==================================================

-- Pergunta de negócio:
-- Existe diferença na diária média entre os hotéis?

SELECT
    hotel,
    ROUND(AVG(adr), 2) AS average_adr
FROM hotel_bookings
GROUP BY hotel
ORDER BY average_adr DESC;

-- ==================================================
-- ETAPA 6.5 - Reservas por mês
-- ==================================================

-- Pergunta de negócio:
-- Como as reservas estão distribuídas ao longo do ano?

SELECT
    arrival_date_month,
    COUNT(*) AS total_bookings
FROM hotel_bookings
GROUP BY arrival_date_month
ORDER BY
CASE arrival_date_month
    WHEN 'January' THEN 1
    WHEN 'February' THEN 2
    WHEN 'March' THEN 3
    WHEN 'April' THEN 4
    WHEN 'May' THEN 5
    WHEN 'June' THEN 6
    WHEN 'July' THEN 7
    WHEN 'August' THEN 8
    WHEN 'September' THEN 9
    WHEN 'October' THEN 10
    WHEN 'November' THEN 11
    WHEN 'December' THEN 12
END;

-- ==================================================
-- ETAPA 6.6 - Países com maior número de reservas
-- ==================================================

-- Pergunta de negócio:
-- Quais países concentram o maior número de reservas?

SELECT
    country,
    COUNT(*) AS total_bookings
FROM hotel_bookings
GROUP BY country
ORDER BY total_bookings DESC
LIMIT 10;

-- ==================================================
-- ETAPA 6.7 - Reservas por segmento de mercado
-- ==================================================

-- Pergunta de negócio:
-- Qual segmento de mercado gera mais reservas?

SELECT
    market_segment,
    COUNT(*) AS total_bookings
FROM hotel_bookings
GROUP BY market_segment
ORDER BY total_bookings DESC;