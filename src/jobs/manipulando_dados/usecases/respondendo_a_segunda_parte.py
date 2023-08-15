### SCRIPT PARA ETL RECEBENDO DADOS DO MYSQL E SALVANDO NO MYSQL ###

#Importando as bibliotecas
import pandas as pd
import logging

class Respondendo:
    def __init__(self) -> None:
        pass
    
    def __separando_por_mes(self, dataframe):
        try:
            df = dataframe

            # Converter a coluna 'datahora_acesso' para o tipo de dado de data e hora
            df['datahora_acesso'] = pd.to_datetime(df['datahora_acesso'], errors='coerce', format='mixed')



            # Extrair o mês para uma nova coluna chamada 'mes_acesso'
            df['datahora_acesso'] = df['datahora_acesso'].dt.to_period('M')

            logging.info(f'Dataframe processado criado com sucesso.')

            return dataframe
        
        except ZeroDivisionError as error:
            logging.info(f'Problemas na criação da coluna mes no dataframe. Segue o erro: {error}')
    
    def criando_primeiro(self, dataframe):
        try:
            #Dataframe recebido pela função
            df = dataframe

            #Separando o mês da data.
            xx = self.__separando_por_mes(df)

            # Consolidando os resultados por mês
            consolidando_dataframe = xx.groupby('datahora_acesso').agg(
                rake=pd.NamedAgg(column='rake', aggfunc='sum'),
                jogadores=pd.NamedAgg(column='clientes_id', aggfunc='nunique'),
                rake_cash_game=pd.NamedAgg(column='rake', aggfunc=lambda x: x[xx['modalidade'] == 'Cash Game'].sum()),
                rake_torneio=pd.NamedAgg(column='rake', aggfunc=lambda x: x[xx['modalidade'] == 'Torneio'].sum()),
                jogadores_cash_game=pd.NamedAgg(column='clientes_id', aggfunc=lambda x: x[xx['modalidade'] == 'Cash Game'].nunique()),
                jogadores_torneio=pd.NamedAgg(column='clientes_id', aggfunc=lambda x: x[xx['modalidade'] == 'Torneio'].nunique())
            )

            # Criando um DataFrame a partir da tabela consolidada
            df_consolidado = pd.DataFrame(consolidando_dataframe).reset_index()

            df_consolidado['datahora_acesso'] = df_consolidado['datahora_acesso'].astype(str)

            logging.info(f'Dataframe processado criado com sucesso.')

            return df_consolidado 
        
        except ZeroDivisionError as error:
            logging.info(f'Problemas na criação dos calculos. Segue o erro: {error}')
    

    
