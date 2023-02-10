import requests
import smtplib
import csv
import json
from email.mime.text import MIMEText
#conferir game_mode 1,2 ou 22

def licodificador(galera):
    codiguin = []
    for i in galera:
        url = f"https://api.opendota.com/api/players/{i['ID']}/recentMatches?limit=1"
        response = requests.get(url)
        data = response.json()
        try:
            ultimo_game = data[0]
            codiguin.append(ultimo_game['match_id'])
        except:
            ultimo_game = 0
            codiguin.append(0)
    return codiguin


def avaliar(cod, galera):
    new_cod = licodificador(galera)
    for i in range(len(cod)):
        if str(new_cod[i]) != '0' and str(new_cod[i]) != str(cod[i]):
            
            match = f_match(galera[i]['ID'])
            print(f"{galera[i]['Nick']} acabou de terminar uma partida!\nTeremos lista?" )
            if str(match['game_mode']) == "1" or str(match['game_mode']) == "2" or str(match['game_mode']) == "22":
                cod[i] = new_cod[i]
                if int(match['deaths']) - int(match['kills']) >= 10:
                    print('é listaaaa')
                    f_email(galera[i],match)
            else:
                print("Infelizmente não foi dessa vez...")
    return cod


def f_match(sujeito):
    url = f"https://api.opendota.com/api/players/{sujeito}/recentMatches?limit=1"
    response = requests.get(url)
    data = response.json()
    return data[0]


def f_email(artista,match):
    cred = [*csv.DictReader(open('cred.csv', encoding='utf-8'))]
    with open("heroes.json", "r", encoding='utf-8') as json_file:
    # Carrega o conteúdo do arquivo como dicionário
        heroi = json.load(json_file) 
    user = cred[0]['login']
    password = cred[0]['senha']
    sent_from = user
    
    copia = []
    for j in cred:
        copia.appendj['e-mail']

    to = f"{artista['e-mail']}"
    subject = f"""Parabéns {artista['Nick']}! É Listaaaaa!!"""
    body = f"""\
        Parabéns {artista['Nome']}!\n
        Você foi devidamente listado pelo seu desempenho brilhante na partida!\n\n
        Aqui está sua obra jogando de {heroi[str(match['hero_id'])]['localized_name']}:\n
        \tKills: {match['kills']}\n
        \tMortes: {match['deaths']}\n
        \tAssists: {match['assists']}\n
        \tDuração: {match['duration']/60} minutos\n
        \tDano: {match['hero_damage']}\n\n
        \t\tCaso acredita que essa lista é injusta, primeiramente foda-se,\n
        \t\tsegundamete, você tem direito de até 2 audiências por semestre"""


    msg = MIMEText(body.encode('utf-8'), 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = sent_from
    msg['Cc'] = copia
    msg['To'] = to

    with smtplib.SMTP('smtp-mail.outlook.com', 587) as server:
        try:
            server.ehlo()
            server.starttls()
            server.login(user, password)
            server.sendmail(sent_from, to, msg.as_string())
            #server.send_message(msg)
            server.quit()
            print ('Email enviado!')
        except Exception as e:
            print ('Algo deu errado...')
            print (e)
