from database.connection import get_connection
import logging

async def load(df):
    conn = await get_connection()

    for _, row in df.iterrows():
        await conn.execute("""
            INSERT INTO atendimentos (nome, status, inicio, fim, tempo_atendimento)
            VALUES ($1, $2, $3, $4, $5)
            ON CONFLICT (nome, inicio, fim) DO NOTHING
        """,
        row["nome"],
        row["status"],
        row["inicio"],
        row["fim"],
        row["tempo_atendimento"]
        )

    await conn.close()
    logging.info("📦 Dados carregados no banco!")