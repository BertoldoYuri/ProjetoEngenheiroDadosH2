### SCRIPT PARA RESPOSTAS DA PRIMEIRA ETAPA DO TESTE ###

import sys, os
sys.path.insert(0, '{}/src/jobs'.format(os.getcwd()))

#Importando as bibliotecas
from perguntas.infra.criar_conexao import CriarConexao

import pandas as pd
import logging

class Respondendo():
    def __init__(self, host, usuario, senha, database) -> None:
        #informações dos banco de dados:
        host = host
        usuario = usuario
        senha = senha
        self.database = database

        #Conectando o script ao banco de dados
        self.conexao, self.cursor = CriarConexao().no_msql(host, usuario, senha)

        

    def a_primeira_pergunta(self):
        #Criando query
        query = """ 
                select CASE
                    WHEN year(C.data_nascimento) BETWEEN '1925' AND '1940' THEN 'Veteranos'
                    WHEN year(C.data_nascimento) BETWEEN '1941' AND '1959' THEN 'Baby Boomers'
                    WHEN year(C.data_nascimento) BETWEEN '1960' AND '1979' THEN 'Geração X'
                    WHEN year(C.data_nascimento) BETWEEN '1980' AND '1995' THEN 'Geração Y'
                    WHEN year(C.data_nascimento) BETWEEN '1996' AND '2009' THEN 'Geração Z'
                    ELSE 'Geração Alpha'
                END AS geracao,
                sum(R.rake) as rake
                from clientes as C
                left join resultado as R on C.id = R.cliente_id
                where R.rake is not null
                group by geracao
        """

        #Selecionando o database
        self.cursor.execute(f"USE {self.database}")
        
        #Executando a query
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        #Obter os nomes das colunas
        column_names = [desc[0] for desc in self.cursor.description]

        #Fechando a conexão
        self.conexao.close()

        #Criando um dataframe
        df = pd.DataFrame(results, columns=column_names)

        caminho = "./resources/Quantidade_Rake_Por_Geracao.csv"

        #Impressão para a resposta
        logging.info(f"Os resultados serão disponibilizados no {caminho} ")

        #Salvando a tabela em CSV
        df.to_csv('resources/resultados/1_Resposta_Quantidade_Rake_Por_Geracao.csv', index=False)

        return 1
    def a_segunda_pergunta(self):
        #Criando query
        query = """ 
                select
                    CASE
                            WHEN MONTH(R.data_acesso) = 1 THEN 'Janeiro'
                            WHEN MONTH(R.data_acesso) = 2 THEN 'Fevereiro'
                            WHEN MONTH(R.data_acesso) = 3 THEN 'Março'
                            WHEN MONTH(R.data_acesso) = 4 THEN 'Abril'
                            WHEN MONTH(R.data_acesso) = 5 THEN 'Maio'
                            WHEN MONTH(R.data_acesso) = 6 THEN 'Junho'
                            WHEN MONTH(R.data_acesso) = 7 THEN 'Julho'
                            WHEN MONTH(R.data_acesso) = 8 THEN 'Agosto'
                            WHEN MONTH(R.data_acesso) = 9 THEN 'Setembro'
                            WHEN MONTH(R.data_acesso) = 10 THEN 'Outubro'
                            WHEN MONTH(R.data_acesso) = 11 THEN 'Novembro'
                            else 'Dezembro'
                        end "Mes_por_escrito",
                    sum(R.rake) as rake
                from clientes as C
                left join resultado as R on C.id = R.cliente_id
                where R.rake is not null
                GROUP BY Mes_por_escrito, MONTH(R.data_acesso)
                ORDER BY MONTH(R.data_acesso)  ASC
        """

        #Selecionando o database
        self.cursor.execute(f"USE {self.database}")
        
        #Executando a query
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        #Obter os nomes das colunas
        column_names = [desc[0] for desc in self.cursor.description]

        #Fechando a conexão
        self.conexao.close()

        #Criando um dataframe
        df = pd.DataFrame(results, columns=column_names)

        caminho = "./resources/Rake_por_mes.csv"

        #Impressão para a resposta
        logging.info(f"Os resultados serão disponibilizados no {caminho} ")


        #Salvando a tabela em CSV
        df.to_csv('resources/resultados/2_Resposta_Rake_por_mes.csv', index=False)

        return 1
    def a_terceira_pergunta(self):
        #Criando query
        query = """ 
                        SELECT
                            sexo,
                            COUNT(*) AS total_jogadores,
                            SUM(CASE WHEN status = 'ganhador' THEN 1 ELSE 0 END) AS total_ganhadores,
                            CAST(
                                SUM(CASE WHEN status = 'ganhador' THEN 1 ELSE 0 END) AS FLOAT) /
                            COUNT(*) * 100 AS ganhadores_porcentagem
                        FROM (
                            SELECT
                                C.sexo AS sexo,
                                CASE
                                    WHEN R.rake > 0 THEN 'ganhador'
                                    ELSE 'perdeu'
                                END AS status
                            FROM clientes AS C
                            LEFT JOIN resultado AS R ON C.id = R.cliente_id
                            WHERE R.rake IS NOT NULL
                            AND C.sexo IS NOT NULL
                            -- Aqui você pode adicionar um filtro adicional, se necessário
                            -- AND outras_colunas = algum_valor
                        ) AS criterio
                        GROUP BY sexo;

                """
        #Selecionando o database
        self.cursor.execute(f"USE {self.database}")
        
        #Executando a query
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        #Obter os nomes das colunas
        column_names = [desc[0] for desc in self.cursor.description]

        #Fechando a conexão
        self.conexao.close()

        #Criando um dataframe
        df = pd.DataFrame(results, columns=column_names)

        #Criando a resposta
        if df['sexo'][0] == "m":
            sexo = "masculino"
        else:
            sexo = "feminino"

        porcentagem_de_ganhadores = df['ganhadores_porcentagem'][0]

        caminho = "./resources/Eficiencia_Dos_Joagores_Por_Sexo.csv"

        #Impressão para a resposta
        logging.info(f"O sexo com maior proporção de ganhadores é o {sexo}, com {porcentagem_de_ganhadores} %. Caso queira conferir os resultados completos conferir no caminho {caminho} ")

        #Salvando a tabela em CSV
        df.to_csv('resources/resultados/3_Resposta_Eficiencia_Dos_Joagores_Por_Sexo.csv', index=False)

        return 1