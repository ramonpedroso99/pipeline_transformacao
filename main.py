import asyncio
from extract.extract_data import extract
from transform.transform_data import transform
from load.load_data import load

async def pipeline():
    df = extract()
    df = transform(df)
    await load(df)

if __name__ == "__main__":
    asyncio.run(pipeline())