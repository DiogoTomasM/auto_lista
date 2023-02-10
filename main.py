import csv
import listador
import time

'''lê nomes.csv
carrega os valores em dicionario
manda pro listador.py'''

galera = []
galera = [*csv.DictReader(open('nomes.csv', encoding='utf-8'))]
cod = listador.licodificador(galera)
i = 50
while True:
    if i/50 == 1:
        print("Ainda estou vivo")
        i = 50
    cod = listador.avaliar(cod,galera)
    time.sleep(10)
