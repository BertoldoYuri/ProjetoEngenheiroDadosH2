import sys, os
sys.path.insert(0, '{}/src/jobs'.format(os.getcwd()))

from manipulando_dados.app.disponibilizar import DisponibilizandoSegundaParteDoTeste

## CRIANDO O BANCO DE DADOS ##
#DisponibilizandoSegundaParteDoTeste().banco_de_dados()

## CRIANDO AS TABELAS DO BANCO DE DADOS ##
#DisponibilizandoSegundaParteDoTeste().a_criacao_de_tabela()

## TRANSFORMANDO OS DADOS E SALVANDO EM UM BANCO MY SQL ##
DisponibilizandoSegundaParteDoTeste().exercicio()