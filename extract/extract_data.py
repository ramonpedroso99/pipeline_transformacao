import pandas as pd
import logging

def extract():
    df = pd.read_csv("data/dados.csv")
    logging.info("📥 Dados extraídos:")
    logging.info(df.head())
    return df