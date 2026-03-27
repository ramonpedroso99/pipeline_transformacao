from database.connection import get_connection

async def load(df):
    conn = await get_connection()

    for _, row in df.iterrows():
        await conn.execute("""
            INSERT INTO atendimentos (nome, status, inicio, fim, tempo_atendimento)
            VALUES ($1, $2, $3, $4, $5)
        """,
        row["nome"],
        row["status"],
        row["inicio"],
        row["fim"],
        row["tempo_atendimento"]
        )

    await conn.close()
    print("📦 Dados carregados no banco!")