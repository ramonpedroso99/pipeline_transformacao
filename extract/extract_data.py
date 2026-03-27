import pandas as pd

def extract():
    df = pd.read_csv("data/dados.csv")
    print("📥 Dados extraídos:")
    print(df.head())
    return df