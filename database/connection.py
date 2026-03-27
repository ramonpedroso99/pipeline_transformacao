import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

async def get_connection():
    return await asyncpg.connect(
        user=os.getenv("USER"),
        password=os.getenv("SENHA"),
        database=os.getenv("DATABASE"),
        host=os.getenv("HOST"),
        port=int(os.getenv("PORT"))
    )