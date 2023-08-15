### SCRIPT PARA CRIACAO DO DATAFRAME ###

#importar bibliotecas
import pandas as pd
import logging

from acessando_apis.infra.criar_conexao import CriarConexao


class RecebendoDados:
    def __init__(self) -> None:
        pass

    def do_banco_de_dados(self, host, usuario, senha, database, query):
        try:
            #informações dos banco de dados:
            host = host
            usuario = usuario
            senha = senha
            database = database

            #Conectando o script ao banco de dados
            self.conexao, self.cursor = CriarConexao().no_msql(host, usuario, senha)

            #Criando query
            query = query

            #Selecionando o database
            self.cursor.execute(f"USE {database}")
            
            #Executando a query
            self.cursor.execute(query)
            results = self.cursor.fetchall()

            #Obter os nomes das colunas
            column_names = [desc[0] for desc in self.cursor.description]

            #Fechando a conexão
            self.conexao.close()

            #Criando um dataframe
            df = pd.DataFrame(results, columns=column_names)
            logging.info(f'Importação e criação do dataframe com sucesso.')
            return df
        except ZeroDivisionError as error:
            logging.info(f'Erro na importação e criação do dataframe. Segue o erro: {error}')


    def de_um_arquivo_csv(self, caminho, separdor):
        try:
            df = pd.read_csv(caminho, sep= separdor)
            logging.info(f'Importação e criação do dataframe com sucesso.')
            return df
        except ZeroDivisionError as error:
            logging.info(f'Erro na importação e criação do dataframe. Segue o erro: {error}')
    
    def de_um_arquivo_excel(self, caminho):
        try:
            df = pd.read_excel(caminho)
            logging.info(f'Importação e criação do dataframe com sucesso.')
            return df

        except ZeroDivisionError as error:
            logging.info(f'Erro na importação e criação do dataframe. Segue o erro: {error}')