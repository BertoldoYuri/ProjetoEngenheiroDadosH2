### SCRIPT PARA ETL RECEBENDO DADOS DO MYSQL E SALVANDO NO MYSQL ###

import sys, os
sys.path.insert(0, '{}/src/jobs'.format(os.getcwd()))

#Importando as bibliotecas
import pandas as pd
import logging

from manipulando_dados.infra.recebendo_dados import RecebendoDados
from manipulando_dados.infra.salvando_dados import SalvandoDados
from manipulando_dados.infra.criando_db_tb import Criando
from manipulando_dados.usecases.respondendo_a_segunda_parte import Respondendo

class DisponibilizandoSegundaParteDoTeste:
    def __init__(self) -> None:
        pass
    
    def banco_de_dados(self):
        try:
            #Informações do banco de dados
            host = "localhost"
            usuario = "root"
            senha = "123456" 
            database = "TESTE_2"
            #Executando o criador de banco de dados
            Criando(host, usuario, senha).banco_de_dados(database)

            logging.info("Banco de dados criado com sucesso.")

            return 1
        
        except ZeroDivisionError as error:
            logging.info(f'Problemas na hora de disponibilizar o banco de dados.')
    
    def a_criacao_de_tabela(self):
        try:
            #Informações do banco de dados
            host = "localhost"
            usuario = "root"
            senha = "123456" 
            database = "TESTE_2"

            table_name = "consolidacao"
            informacoes = ["mes varchar(255)", "rake varchar(255)", "jogadores varchar(255)", "rake_cash_game varchar(255)", "rake_torneio varchar(255)", "jogadores_cash_game varchar(255)", "jogadores_torneio varchar(255)"]
            Criando(host, usuario, senha).tabelas(database, table_name, informacoes)

            return 1
        
        except ZeroDivisionError as error:
            logging.info(f'Problemas na hora de disponibilizar a tabela {table_name}.')


    def exercicio(self):
        try:
            #Informações do bando de dados de onde vira as informações
            database_r = "a4f2b49a_sample_database"
            host_r = "40b8f30251.nxcli.io"
            user_r = "a4f2b49a_padawan"
            password_r = "KaratFlanksUgliedSpinal"
            query_r = '''SELECT * FROM  raw_data;'''

            #Informações do banco de dados onde sera salvo
            host = "localhost"
            usuario = "root"
            senha = "123456" 
            database = "TESTE_2"

            #Imprtando os dados
            df = RecebendoDados().do_banco_de_dados(host_r, user_r, password_r, database_r, query_r)

            #Executando função para criar o dataframe calculado
            df = Respondendo().criando_primeiro(df)

            #Salvando os dados em um banco de dados
            nome_das_colunas = ["mes", "rake", "jogadores", "rake_cash_game", "rake_torneio", "jogadores_cash_game", "jogadores_torneio"]
            table_name = "consolidacao"
            SalvandoDados().no_banco_de_dados(host, usuario, senha, database, table_name, nome_das_colunas, df)

            logging.info("Informarções salvas com sucesso")

            return 1

        except ZeroDivisionError as error:
            logging.info(f'Problemas na hora de salvar os arquivos.')

    