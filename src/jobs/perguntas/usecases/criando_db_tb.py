### SCRIPT PARA CRIAÇÃO DO BANCO DE DADOS E TABELAS ###

import sys, os
sys.path.insert(0, '{}/src/jobs'.format(os.getcwd()))

#Importando as bibliotecas
from perguntas.infra.criar_conexao import CriarConexao
import logging


class Criando:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

    def banco_de_dados(self, database):
        try:
            #Criando a query para criação do database
            query_criacao_do_db = f''' CREATE DATABASE {database} '''

            #Conectando o script ao banco de dados
            conexao, cursor = CriarConexao().no_msql(self.host, self.user, self.password)

            #Executando a criação do database
            cursor.execute(query_criacao_do_db)

            # Commit as alterações no banco de dados
            conexao.commit()

            logging.info(f"O banco de dados {database} foi criado com sucesso.")

            # Fechando a conexão
            conexao.close()

            return 1
        
        except ZeroDivisionError as error:
            logging.info(f'O banco de dados {database}, não foi criado por causa do erro: {error}.')

            return 1
    
    def tabelas(self, database, table_name, colums_name_type_primary_key): #Para o funcionamento da função devera ser enviado o nome da tabela 'Tabela1' / nome das colunas tipo "name VARCHAR(255)"/ 
        try:
            database = database
            table_name = table_name
            colums_info= []

            for x in colums_name_type_primary_key:
                colums_info.append(x)
            
            separador = ", "
            columns = separador.join(colums_info)
            
            #Criando a query para criação das tabelas
            query_criacao_da_tabela = f'''CREATE TABLE {table_name} ({columns});'''

            #Conectando o script ao banco de dados
            conexao, cursor = CriarConexao().no_msql(self.host, self.user, self.password)

            #Selecionando o banco que sera usado
            cursor.execute(f"USE {database}")

            #Executando a query para a criação da tabela
            cursor.execute(query_criacao_da_tabela)

            # Commit as alterações no banco de dados
            conexao.commit()

            logging.info(f"A tabela {table_name} foi criado com sucesso.")
            
            # Fechando a conexão
            conexao.close()

            return 1
        
        except ZeroDivisionError as error:
            logging.info(f'A tabela {table_name}, não foi criado por causa do erro: {error}.')

            return 1