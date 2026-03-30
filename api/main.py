from fastapi import FastAPI
import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

async def get_connection():
    return await asyncpg.connect(
        user=os.getenv("USUARIO"),
        password=os.getenv("SENHA"),
        database=os.getenv("DATABASE"),
        host=os.getenv("HOST"),
        port=int(os.getenv("PORT"))
    )

@app.get("/atendimentos")
async def listar_atendimentos():
    conn = await get_connection()

    rows = await conn.fetch("SELECT * FROM atendimentos")

    await conn.close()

    return [dict(row) for row in rows]