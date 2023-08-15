import sys, os
sys.path.insert(0, '{}/src/jobs'.format(os.getcwd()))

from perguntas.usecases.criando_db_tb import Criando
from perguntas.usecases.inserindo_dados_tb import Inserindo
from perguntas.usecases.respondendo_as_perguntas import Respondendo


class DisponibilizandoPrimeiraParteDoTeste:
    def __init__(self) -> None:
        #informações dos banco de dados:
        self.host = "localhost"
        self.usuario = "root"
        self.senha = "123456" 
        self.database = "Teste1"
        
        #informações das tabelas:
        #self.table_name = "resultado"
        self.table_name = "clientes"

    def a_criacao_do_banco_dados(self):
        Criando(self.host, self.usuario, self.senha).banco_de_dados(self.database)

        return 1

    def a_criacao_de_tabela(self):
        informacoes = ["data_acesso date", "cliente_id varchar(255)", "buyin decimal", "rake decimal", "winning decimal", "FOREIGN KEY (cliente_id) REFERENCES clientes (id)"]
        #informacoes = ["id varchar(255) PRIMARY KEY", "sexo VARCHAR(1)", "data_nascimento date", "data_cadastro datetime", "cidade VARCHAR(255)", "sigla VARCHAR(2)"]

        Criando(self.host, self.usuario, self.senha).tabelas(self.database, self.table_name, informacoes)

        return 1

    def a_insercao_dados_nas_tabelas(self):
        caminho = "/Users/yuribertoldo/Documents/Teste-H2/resources/resultado.csv"
        nome_das_colunas = ["data_acesso", "cliente_id", "buyin", "rake", "winning"]
        #caminho = "/Users/yuribertoldo/Documents/Teste-H2/resources/clientes.csv"
        #nome_das_colunas = ["id", "sexo", "data_nascimento", "data_cadastro"]

        Inserindo(self.host, self.usuario, self.senha).dados_no_banco_via_csv(caminho, self.database, self.table_name, nome_das_colunas)

        return 1
    
    def a_primeira_resposta(self):
        Respondendo(self.host, self.usuario, self.senha, self.database).a_primeira_pergunta()
        return 1
    
    def a_segunda_resposta(self):
        Respondendo(self.host, self.usuario, self.senha, self.database).a_segunda_pergunta()
        return 1 

    def a_terceira_resposta(self):
        Respondendo(self.host, self.usuario, self.senha, self.database).a_terceira_pergunta()
        return 1 