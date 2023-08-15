import sys, os
sys.path.insert(0, '{}/src/jobs'.format(os.getcwd()))

from perguntas.app.disponibiliza import DisponibilizandoPrimeiraParteDoTeste

DisponibilizandoPrimeiraParteDoTeste().a_primeira_resposta()
DisponibilizandoPrimeiraParteDoTeste().a_segunda_resposta()
DisponibilizandoPrimeiraParteDoTeste().a_terceira_resposta()