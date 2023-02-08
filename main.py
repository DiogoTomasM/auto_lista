import csv
import listador

'''lê nomes.csv
carrega os valores em dicionario
manda pro listador.py'''

galera = []
galera = [*csv.DictReader(open('nomes.csv', encoding='utf-8'))]
cod = listador.licodificador(galera)
#loop
cod = listador.avaliar(cod,galera)