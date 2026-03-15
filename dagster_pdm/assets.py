import os

import psycopg2
from dagster import asset

DEFAULT_DATABASE_URL = "postgres://postgres:postgres@db:5432/codata_db"


@asset
def atualizar_indicadores_frota():
    database_url = os.getenv("DATABASE_URL", DEFAULT_DATABASE_URL)

    with psycopg2.connect(database_url) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                UPDATE frota_monitoramentofrota
                SET eletricos = 950,
                    co2_evitado = 2000.0
                """
            )
            cursor.execute(
                """
                SELECT eletricos, co2_evitado
                FROM frota_monitoramentofrota
                LIMIT 1
                """
            )
            row = cursor.fetchone()

    return {
        "eletricos": row[0] if row else 0,
        "co2_evitado": float(row[1]) if row else 0.0,
    }
