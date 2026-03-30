import pandas as pd
import logging

def transform(df):
    logging.info("\n🔄 Iniciando transformação...")

    
    df = df[df["status"] == "concluido"]

    
    df["inicio"] = pd.to_datetime(df["inicio"])
    df["fim"] = pd.to_datetime(df["fim"])

    
    df["tempo_atendimento"] = (df["fim"] - df["inicio"]).dt.total_seconds() / 60

    logging.info("✅ Transformação concluída:")
    logging.info(df)

    return df