import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

def get_engine(db_file: str) -> Engine:
    """
    Essa função tem como objetivo criar e retornar uma engine de conexão do SQLAlchemy para um banco de dados SQLite.
    """
    connection_string = f"sqlite:///{db_file}"
    engine = create_engine(connection_string)
    print(f"Engine para o banco de dados '{db_file}' criada.")
    return engine

def save_dataframe(df: pd.DataFrame, table_name: str, engine: Engine, if_exists: str = "replace"):
    """
    Essa função tem como objetivo salvar um DataFrame em uma tabela de banco de dados usando uma engine do SQLAlchemy.
    """
    if df.empty:
        print(f"DataFrame para a tabela '{table_name}' está vazio, ou seja, nada foi salvo")
        return

    try:
        print(f"Salvando {len(df)} registros na tabela '{table_name}'.")
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists=if_exists,
            index=False
        )
        print(f"Dados salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar DataFrame: {e}")
    finally:
        engine.dispose()
        print("Conexão com o banco de dados encerrada.")