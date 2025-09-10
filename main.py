import config
import extracao_api
import processamento_banco_dados
import manipulacao_banco_dados

def run_pipeline():
    """
    Essa função tem como objetivo executar toda a pipeline, isto é, ela orquestra os outros scripts para que: se extraiam os dados da API, se transformem os dados brutos extraídos e se carreguem os dados em um banco, sendo que o escolhido foi o SQLite.
    """
    print("Extração iniciada - Início do pipeline")
    
    # Primeiro passo - Extração
    client = extracao_api.CoinCapAPI()
    raw_assets_data = client.get_assets()
    
    if raw_assets_data is None:
        print("Extração encerrada - Fim do pipeline")
        return

    # Segundo passo - Transformação
    processed_assets_df = processamento_banco_dados.process_assets_data(raw_assets_data)

    # Terceiro passo - Manipulação
    db_engine = manipulacao_banco_dados.get_engine(config.DATABASE_FILE)
    manipulacao_banco_dados.save_dataframe(
        df=processed_assets_df,
        table_name="assets",
        engine=db_engine
    )

    print("O pipeline foi concluído com sucesso!")

if __name__ == "__main__":
    # Verifica se a API_KEY foi configurada
    if config.API_KEY == "INSIRA_AQUI_SUA_CHAVE" or not config.API_KEY:
        print("Erro: Necessita-se da sua chave de API adicionada no arquivo config.py")
    else:
        run_pipeline()