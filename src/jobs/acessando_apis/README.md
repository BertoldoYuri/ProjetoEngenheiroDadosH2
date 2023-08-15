# Introdução  
Este código irá responder o teste abaixo. 

Para essa atividade queremos que você utilize [essa](#https://rapidapi.com/theoddsapi/api/live-sports-odds/) API. Nela você encontrará resultados de partidas de diversos esportes. Queremos que você utilize o endpoint de scores para buscar determinadas informações do sport soccer_brazil_campeonato na resposta da API e salvar numa tabela chamada partidas_brasileirao_serie_a_2023 contendo as seguintes colunas: 

Tabela: 
```
datahora_partida 
data_partida 
time_casa 
time_fora 
gols_time_casa 
gols_time_fora 
``` 

Obs: trazer apenas os resultados do ano de 2023. 
Essas informações devem ser salvas num banco local em MYSQL, o mesmo utilizado para as outras atividades. 

## Estrutura do projeto 
Para essa entrada estruturamos o jobs "modulo" em 4 partes. 
``` 
|-- jobs 
|-- |-- acessando_apis 
|-- |-- |-- app 
|-- |-- |-- cross 
|-- |-- |-- infra 
|-- |-- |-- usecases 
``` 

### infra 
A pasta de infra é onde ligamos o código ao mundo exterior aqui recebemos os arquivos csv, xlml, parquets, fotos, vídeos e conectamos ao banco de dados. Neste modulo temos 4 arquivos que fazem isso. 

1. [criando_db_tb.py](infra/criando_db_tb.py) 
    * neste arquivo criamos o database no banco e criamos a tabela que depois será populada por outra parte do código. 

2. [criar_conexao.py](infra/criar_conexao.py) 
    * aqui criamos todas as conexão com o banco de dados. 

3. [recebendo_dados.py](infra/recebendo_dados.py) 
    * aqui é quando recebemos os dados que estão fora do nosso arquivo. 

4. [salvando_dados.py](infra/salvando_dados.py) 
    * aqui é quando salvamos os dados que estão sendo entregues em nosso código. 

### usecases 
A pasta de usecase são os scripts que fazem a parte de transformação dos dados, no caso desse exercício e arrumar os dados que estão sendo recebidos pela API. 
1. [respondendo_a_terceira_parte.py](usecases/respondendo_a_terceira_parte.py) 
    * aqui temos um script que recebe os dados de uma função, transforma os dados e depois salva usando o script que está na infra. 

### cross 
A pasta cross é usado para montar scripts que são usados em vários locais dentro do modulo. Para a resolução desse exercício não usamos. 

### app  
A pasta app é usada para chamar todos os scripts e fazer com que tudo funcione. 

### main.py 
Arquivo que chama o app. 