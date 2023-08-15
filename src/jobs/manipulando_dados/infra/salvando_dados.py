### SCRIPT PARA SALVAR DATAFRAME ###

#importar bibliotecas
import pandas as pd
import logging

from manipulando_dados.infra.criar_conexao import CriarConexao

class SalvandoDados():
    def __init__(self) -> None:
        pass

    def no_banco_de_dados(self, host, usuario, senha, database, table_name,nome_das_colunas, dataframe):
        try:
            
            #informações dos banco de dados:
            host = host
            usuario = usuario
            senha = senha
            database = database

            #ajustando as colunas para colocar na query
            colunas_info = []
            values_info = []
            for x in nome_das_colunas:
                colunas_info.append(x)
                values_info.append("%s")

            separador = ", "
            colunas_query = separador.join(colunas_info)
            values_query = separador.join(values_info)

            #importando o arquivo de csv
            df = dataframe

            table_name = table_name

            #conectando ao banco de dados
            conexao, cursor = CriarConexao().no_msql(host, usuario, senha)
            
            cursor.execute(f"USE {database}")

            # Executar a consulta para inserir os dados do DataFrame na tabela
            cursor.executemany(f"INSERT INTO {table_name} ({colunas_query}) VALUES ({values_query})", df.values.tolist())

            # Commit as alterações no banco de dados
            conexao.commit()

            logging.info(f'Foram inseridos com sucesso os valores na tabela {table_name}.')

            # Fechando a conexão
            conexao.close()

            return 1
        
        except ZeroDivisionError as error:
            logging.info(f'Tivemos problemas para salvar os valores na tabela {table_name}.')

            return 1
    
    def em_csv(self, caminho, dataframe):
        try:
            dataframe = dataframe
            dataframe.to_csv(caminho, index=False)
            logging.info(f'Dataframe salvo com sucesso no {caminho} em csv.')
            return 1
        
        except ZeroDivisionError as error:
            logging.info(f'Problemas na hora de salvar o dataframe no {caminho} em csv.')

            return 1

    def em_excel(self, caminho, dataframe):
        try:
            dataframe = dataframe
            dataframe.to_excel(caminho, index=False)
            logging.info(f'Dataframe salvo com sucesso no {caminho} em excel.')
            return 1
        
        except ZeroDivisionError as error:
            logging.info(f'Problemas na hora de salvar o dataframe no {caminho} em excel.')

            return 1