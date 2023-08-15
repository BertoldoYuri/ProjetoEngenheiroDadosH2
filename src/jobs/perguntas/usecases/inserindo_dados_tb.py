### SCRIPT PARA INSERÇÃO DE DADOS NO BANCO DE DADOS ###

import sys, os
sys.path.insert(0, '{}/src/jobs'.format(os.getcwd()))

#Importando as bibliotecas 
from perguntas.infra.criar_conexao import CriarConexao

import logging
import pandas as pd

class Inserindo:
    def __init__(self, host, usuario, senha):
        self.host = host
        self.usuario = usuario
        self.senha = senha

    def dados_no_banco_via_csv(self, caminho_do_arquivo, database, table_name, nome_das_colunas):
        try:
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
            df = pd.read_csv(caminho_do_arquivo, sep=",")

            table_name = table_name

            #conectando ao banco de dados
            conexao, cursor = CriarConexao().no_msql(self.host, self.usuario, self.senha)
            
            cursor.execute(f"USE {database}")

            # Executar a consulta para inserir os dados do DataFrame na tabela
            cursor.executemany(f"INSERT INTO {table_name} ({colunas_query}) VALUES ({values_query})", df.values.tolist())

            # Commit as alterações no banco de dados
            conexao.commit()

            logging.info(f'A tabela {table_name}, teve o arquivo {caminho_do_arquivo} inserido na tabela com sucesso.')

            # Fechando a conexão
            conexao.close()

            return 1
        
        except ZeroDivisionError as error:
            logging.info(f'Ocorreu um erro na inserção do arquivo {caminho_do_arquivo} na tabela {table_name}. Segue o erro: {error}')

            return 1