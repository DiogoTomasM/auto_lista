import csv
import listador
import time

'''lê nomes.csv
carrega os valores em dicionario
manda pro listador.py'''

galera = []
galera = [*csv.DictReader(open('nomes.csv', encoding='utf-8'))]
cod = listador.licodificador(galera)
print(cod)
while True:
    cod = listador.avaliar(cod,galera)
    print(cod)
    time.sleep(10)
