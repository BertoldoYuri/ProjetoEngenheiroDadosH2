#Importando as bibliotecas 
import mysql.connector
import logging

### SCRIPT PARA CONEXÃO COM  BANCO DE DADOS MYSQL ###

class CriarConexao():
    def __init__(self) -> None:
        pass

    def no_msql(self, host, usuario, senha):
        try:
            #Criando a conexão
            conexao = mysql.connector.connect(
                host=host,
                user=usuario,
                password=senha
            )

            db = conexao.cursor()

            logging.info('Conexão com o banco de dados MySql bem sucedida.')
            return conexao, db

        except ZeroDivisionError as error:
            logging.info(f'Conexão com o banco de dados MySql mal sucedida. A mensagem de erro foi: {error}.')

            return 1