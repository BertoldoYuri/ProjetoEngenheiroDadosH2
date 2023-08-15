### SCRIPT PARA CHAMAR UMA API COM INFORMAÇÕES DO CAMPEONATO BRASILEIRO ###

import requests
import pandas as pd
import logging

class Chamando:
    def __init__(self) -> None:
        pass
    
    def __api(self):
        try:
            url = "https://odds.p.rapidapi.com/v4/sports/soccer_brazil_campeonato/scores"

            querystring = {"daysFrom":"3"}

            headers = {
                "X-RapidAPI-Key": "757fa5aff1msha5be5e6faafa65ep181a16jsn54aa04924afe",
                "X-RapidAPI-Host": "odds.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers, params=querystring)

            logging.info(f'Api {url}, chamada com sucesso.')
            df = pd.DataFrame(response.json())

            df_filtrado = df[df.completed == True]

            if len(df_filtrado) > 0:
                logging.info('Temos informações na api.')
            else:
                logging.info('Não tivemos jogos nos ultimos 3 dias.')

            return df_filtrado
        
        except ZeroDivisionError as error:
            logging.info(f'Tivemos problemas para chamar a api {url}, obtivemos o codigo {response.status_code}. Segue o erro:{error}.')
    
    def ajustes_nas_colunas(self):
        try:
            #Carregando o dataframe
            df = self.__api()

            if len(df) > 0:

                #Transformando o dataframe inicial no dataframe que sera salvo.
                c = []
                for x in df[['scores', 'commence_time']].values:
                    q = dict({'datahora_partida':x[1], "data_partida":x[1][:10] ,'time_casa':x[0][0]['name'], 'time_fora':x[0][1]['name'], "gols_time_casa": x[0][0]['score'],"gols_time_fora":x[0][1]['score']})
                    c.append(q)
                
                xx = pd.DataFrame(c)
                
                logging.info(f'Dataframe transformado com sucesso.')

                return xx
            
            else:
                logging.info('Não tivemos nenhum jogo nos ultimos 3 dias.')

                return df

        except ZeroDivisionError as error:
            logging.info(f'Probelam na transformação do dataframe.')