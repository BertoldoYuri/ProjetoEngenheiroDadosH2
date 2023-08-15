# Introdução  
Escreva um script em Python que lê os dados de uma tabela num banco MySQL, consolida os dados e salva numa outra tabela de um banco local MySQL. Para a tarefa de read, iremos passar o acesso a um banco de dados. Para o write, queremos que você suba um banco localmente para testar o script.

Acesso ao banco de dados:

* Banco: a4f2b49a_sample_database
* Host:40b8f30251.nxcli.io
* User: a4f2b49a_padawan
* Password: KaratFlanksUgliedSpinal
* Port: 3306

Para acessar o banco de dados você precisará ter o seu IP liberado. Para isso, mande o seu número de IP para o email william.westrup@h2grupo.com. 
Utilize esse site para buscar o seu ip externo.

Os dados estão presentes na tabela raw_data. Essa tabela contém as colunas:
* datahora_acesso: o timestamp em que o jogador realizou a ação
* modalidade: o tipo de jogo, podendo ser Cash Game ou Torneio
* rake: o lucro gerado por esse jogador
* clientes_id: id do jogador

Queremos que você consolide os resultados por mês, sendo que a tabela consolidada terá as seguintes colunas:

* mes: o mês em que os jogadores realizaram a ação
* rake: a soma total do rake no mês
* jogadores: a quantidade distinta de jogadores que jogaram cash game ou torneio
* rake_cash_game: a soma do rake da modalidade cash game gerado no mês
* rake_torneio: a soma do rake da modalidade torneio gerado no mês
* jogadores_cash_game: a quantidade distinta de jogadores que jogaram cash game no mês
* jogadores_torneio: a quantidade distinta de jogadores que jogaram torneio no mês


O script fará a seguinte sequência:
Ler os dados no banco MySQL -> Consolidar os dados -> Salvar os dados consolidados numa nova tabela. Utilize as bibliotecas que você se sentir mais confortável.


## Estrutura do projeto 
Para essa entrada estruturamos o jobs "modulo" em 4 partes. 
``` 
|-- jobs 
|-- |-- manipulando_dados 
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
1. [respondendo_a_segunda_parte.py](usecases/respondendo_a_segunda_parte.py) 
    * aqui temos um script que recebe os dados de uma função, transforma os dados e depois salva usando o script que está na infra. 

### cross 
A pasta cross é usado para montar scripts que são usados em vários locais dentro do modulo. Para a resolução desse exercício não usamos. 

### app  
A pasta app é usada para chamar todos os scripts e fazer com que tudo funcione. 

### main.py 
Arquivo que chama o app. 