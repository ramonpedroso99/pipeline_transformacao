import pandas as pd

def transform(df):
    print("\n🔄 Iniciando transformação...")

    
    df = df[df["status"] == "concluido"]

    
    df["inicio"] = pd.to_datetime(df["inicio"])
    df["fim"] = pd.to_datetime(df["fim"])

    
    df["tempo_atendimento"] = (df["fim"] - df["inicio"]).dt.total_seconds() / 60

    print("✅ Transformação concluída:")
    print(df)

    return df