import sys, os
sys.path.insert(0, '{}/src/jobs'.format(os.getcwd()))

import sys, os
sys.path.insert(0, '{}/src/jobs'.format(os.getcwd()))

#Importando as bibliotecas
import pandas as pd
import logging

from acessando_apis.infra.criando_db_tb import Criando
from acessando_apis.usecases.respondendo_a_terceira_parte import Chamando
from acessando_apis.infra.salvando_dados import SalvandoDados

class DisponibilizandoTerceiraParteDoTeste:
    def __init__(self) -> None:
        #informações dos banco de dados:
        self.host = "localhost"
        self.usuario = "root"
        self.senha = "123456" 
        self.database = "Teste_3"
    
    def banco_de_dados(self):
        try:
            #Informações do banco de dados
            host = self.host
            usuario = self.usuario
            senha = self.senha
            database = self.database
            #Executando o criador de banco de dados
            Criando(host, usuario, senha).banco_de_dados(database)

            logging.info("Banco de dados criado com sucesso.")

            return 1
        
        except ZeroDivisionError as error:
            logging.info(f'Problemas na hora de disponibilizar o banco de dados. Segue o erro:{error}.')

    def a_criacao_de_tabela(self):
        try:
            #Informações do banco de dados
            host = self.host
            usuario = self.usuario
            senha = self.senha
            database = self.database

            table_name = "soccer_brazil_campeonato"
            informacoes = ["datahora_partida varchar(50)", "data_partida varchar(10)", "time_casa varchar(255)", "time_fora varchar(255)", "gols_time_casa int", "gols_time_fora int"]
            Criando(host, usuario, senha).tabelas(database, table_name, informacoes)

            return 1
        
        except ZeroDivisionError as error:
            logging.info(f'Problemas na hora de disponibilizar a tabela {table_name}. Segue o erro:{error}.')
    
    def exercicio(self):
        try:
            #execução do ETL
            df = Chamando().ajustes_nas_colunas()
            
            #Salvando os dados em um banco de dados
            nome_das_colunas = ["datahora_partida", "data_partida", "time_casa", "time_fora", "gols_time_casa", "gols_time_fora"]
            table_name = "soccer_brazil_campeonato"
            SalvandoDados().no_banco_de_dados(self.host, self.usuario, self.senha, self.database, table_name, nome_das_colunas, df)

            logging.info('Informações salvas com sucesso.')

            return 1

        except ZeroDivisionError as error:
            logging.info(f'Problemas na hora salvar os arquivos na tabela {table_name}. Segue o erro:{error}.')
        
        

