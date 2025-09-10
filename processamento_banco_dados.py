import pandas as pd
from typing import List, Dict
import json

def process_assets_data(raw_data: List[Dict]) -> pd.DataFrame:
    """
    Essa função tem como objetivo transformar os dados brutos em um dataframe em Pandas, limpo e formatado
    """
    if not raw_data:
        print("Não possui dado bruto para trabalhar")
        return pd.DataFrame()

    df = pd.DataFrame(raw_data)
    
    df.columns = df.columns.str.replace(r'(?<!^)(?=[A-Z])', '_', regex=True).str.lower()
    
    numeric_cols = [
        "rank", "supply", "max_supply", "market_cap_usd", "volume_usd24_hr",
        "price_usd", "change_percent24_hr", "vwap24_hr"
    ]
    
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            
    # Converte colunas que contêm dicionários (como 'tokens') para string JSON
    if 'tokens' in df.columns:
        # A função .apply() passa por cada valor na coluna 'tokens'.
        # json.dumps() converte o dicionário em uma string de texto.
        # O 'None' é retornado se o valor já for nulo (NaN).
        df['tokens'] = df['tokens'].apply(
            lambda d: json.dumps(d) if isinstance(d, dict) else None
        )
    # ------------------------------------------------

    df = df.drop_duplicates(subset=['id'])

    print(f"Dados processados. DataFrame final com {len(df)} linhas e {len(df.columns)} colunas.")
    return df