import csv
import listador

'''lê nomes.csv
carrega os valores em dicionario
manda pro listador.py'''

galera = []
galera = [*csv.DictReader(open('nomes.csv', encoding='utf-8'))]
cod = listador.licodificador(galera)
cod = [7007028954, 7007124194, 7006833854, 6993480540, 7008135316, 0, 0, 7007028954, 43]
cod = listador.avaliar(cod,galera)