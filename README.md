# Introdução 
Teste para a vaga de engenheiro de dados na H2 Grupo. 

## Dependencias 
Para esse teste será necessária a instalação do python e docker. 
* [Python](#https://www.python.org/) 
* [Docker](#https://www.docker.com/) 
* [Banco de dados MySql](#https://www.mysql.com/downloads/) 

 
## Estrutura do projeto 
Para esse projeto estou usando uma estrutura básica de clean architecture. 

Exemplo:
``` 
root/ 
|-- resources 
|-- src/ 
|-- config/ 
|   |-- environments 
|   |-- |-- values.yaml 
|   |-- jobs/ 
|   |-- |-- job_module_1 
|   |-- |-- |-- my_job_1.py 
|   |-- |-- |-- main.py
|   |-- |-- |-- README.md
| |-- |-- job_module_2 
| |-- |-- |-- my_job_2.py 
|   |-- |-- |-- main.py 
|   |-- |-- |-- README.md
|-- tests/ 
| |-- jobs/ 
| |-- |-- job_module_1 
| |-- |-- |-- test_my_job_1.py 
| |-- |-- job_module_2 
| |-- |-- |-- test_my_job_2.py 
| .gitignore 
| README.md 
| requirements.txt 
``` 

### Descrição da estrutura 
Esta seção explicará cada pasta do projeto. 

#### Resource 
Esta pasta será usada para salvar arquivos excel, csv ou parquets. 

#### SRC 
Esta parte é composta por 2 subpastas 
1. config 
2. jobs 

<b>1. config </b><br> 
Nesta pasta temos os arquivos values.yaml, eles serão usados para variáveis de banco de dados e também poderão ser usados para variáveis de ambientes como caminhos ou nome de pastas. 

Exemplo: 
``` 
file-system: 
    my-path-file: "resources/resultados" 
bando-dados: 
    host: ${host} 
    user: ${user} 
    password: ${password} 
``` 

<b>2. jobs </b><br> 
Local principal para a criação do seu trabalho ou aplicativo, você poderá criar subpastas para organizar da maneira que achar melhor. 

 
#### tests 
Nesta pasta estarão as estruturas de teste, que deverão seguir a formar que está no src. 

Exemplo: 
``` 
|-- tests/ 
|   |-- jobs/ 
|   |-- |-- job_module_1 
|   |-- |-- |-- test_my_job_1.py 
|   |-- |-- job_module_2 
|   |-- |-- |-- test_my_job_2.py 

``` 


## Rodando o projeto 

Jobs/App são os módulos necessários para fazer com que o seu projeto funcione.  

Exemplo: 
``` 
|   |-- jobs/ 
|   |-- |-- job_module_1 
|   |-- |-- |-- my_job_1.py 
|   |-- |-- |-- main.py 
| |-- |-- job_module_2 
| |-- |-- |-- my_job_2.py 
|   |-- |-- |-- main.py 
```` 

Para esse projeto temos o arquivo "main.py", este é o ponto de entrada do trabalho/aplicativo que carrega os jobs e o config. 