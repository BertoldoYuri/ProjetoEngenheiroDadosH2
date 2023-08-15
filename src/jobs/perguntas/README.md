# Introdução  

Id: o id do cliente, pode ser cruzado com a informação de clientes_id na tabela resultado. 

Sexo: sexo do jogador, sendo m=mascluno e f=feminino. 

Data_nascimento: ano, mês e dia de nascimento do jogador. 

Data_cadastro: data e hora de quando o jogador realizou cadastro. 

Cidade: cidade onde mora o jogador. 

Sigla: UF onde mora o jogador. 

Considerando essas tabelas, responda o código em SQL que responde às seguintes perguntas: 

1. Quanto de rake foi gerado por cada Geração* de jogadores? 

2. Qual foi o rake gerado por mês?  

3. Qual sexo tem uma maior proporção de ganhadores**? 

Para essa atividade, considere cada geração tendo o seguinte critério:  
* Veteranos, geração formada por pessoas que nasceram entre 1925 e 1940.  
* Baby Boomers são os nascidos entre 1941 e 1959.  
* Geração X, que compreende o período de 1960 a 1979.  
* Geração Y é composta por indivíduos que nasceram entre 1980 e 1995.  
* Geração Z é composta com os nascidos a partir de 1996 até 2010.  
* Geração Alpha, engloba todos os nascidos a partir de 2010 até a presente data.  

**Como ganhador, considere um jogador com Winning maior que 0 

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

1. [criar_conexao.py](infra/criar_conexao.py)  
    * aqui criamos todas as conexões com o banco de dados. 

### usecases  
A pasta de usecase são os scripts que fazem a parte de transformação dos dados, no caso desse exercício e arrumar os dados que estão sendo recebidos pela API.  

1. [criando_db_tb.py](usecases/criando_db_tb.py)  
    * neste arquivo criamos o database no banco e criamos a tabela que depois será populada por outra parte do código.  

2. [inserindo_dados_tb.py](usecases/inserindo_dados_tb.py)  
    * aqui temos um script que recebe data frames e faz inserção no banco de dados.  

3. [respondendo_as_perguntas.py](usecases/respondendo_as_perguntas.py)  
    * aqui temos um script que recebe os dados de uma função, transforma os dados e depois salva os dataframes na [resources](resources/resultados).  

### cross  
A pasta cross é usado para montar scripts que são usados em vários locais dentro do modulo. Para a resolução desse exercício não usamos.  

### app  
A pasta app é usada para chamar todos os scripts e fazer com que tudo funcione.  

### main.py  
Arquivo que chama o app. 