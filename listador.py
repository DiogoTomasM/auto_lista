import requests
import smtplib
import csv
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from datetime import timedelta
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
        '''######################################## TESTE
        if str(new_cod[i]) != '0':
            match = f_match(galera[i]['ID'])
            f_email(galera[i],match)
        ######################################## TESTE'''
        if str(new_cod[i]) != '0' and str(new_cod[i]) != str(cod[i]):
            with open("heroes.json", "r", encoding='utf-8') as json_file:
            # Carrega o conteúdo do arquivo como dicionário
                heroi = json.load(json_file) 
            match = f_match(galera[i]['ID'])
            print(f"{galera[i]['Nick']} acabou de terminar uma partida jogando de {heroi[str(match['hero_id'])]['localized_name']}!\nTeremos lista?" )
            
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
    nome = [*csv.DictReader(open('nomes.csv', encoding='utf-8'))]
    copia = []
    for j in nome:
        copia.append(j['e-mail'])
    lst = []
    td = str(timedelta(seconds=match['duration']))
    lst = td.split(':')
    td = f'{lst[1]}m{lst[2]}s'

    to = f"{artista['e-mail']}"
    subject = f"""Parabéns {artista['Nick']}! É Listaaaaa!!"""
    body = f"""\
        <html>
            <head>
                <style>
                    p {{
                        font-size: 16px;
                        color: #333;
                    
                    }}
                </style>
            </head>
            <body>
                <p style = "font-size: 22px;"> 

                Parabéns {artista['Nome']}!</p>
                <p>Você foi devidamente listado pelo seu desempenho brilhante na partida!</p>
                <p>Aqui está sua obra jogando de {heroi[str(match['hero_id'])]['localized_name']}:</p>
                <ul>
                    <li>Kills: {match['kills']}</li>
                    <li>Mortes: {match['deaths']}</li>
                    <li>Assists: {match['assists']}</li>
                    <li>Duração: {td}</li>
                    <li>Dano: {match['hero_damage']}</li>
                </ul>
                <p>Que {heroi[str(match['hero_id'])]['localized_name']} horroroso!!</p>
                <img src= "https://1drv.ms/u/s!Amhfkuy5Ge5pgfIzSfVRsWxagJUKSQ?e=VeUcqd">
                <p>Caso acredita que essa lista é injusta, primeiramente foda-se, segundamete, você tem direito de até 2 audiências por semestre</p>
            </body>
        </html>"""


    #msg = MIMEText(body.encode('utf-8'), 'plain', 'utf-8')
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sent_from
    msg['Cc'] = ', '.join(copia)
    msg['To'] = to
    text = MIMEText(body, 'html')
    msg.attach(text)

    with open(f"{heroi[str(match['hero_id'])]['name']}", 'rb') as f:
        image = MIMEImage(f.read())
        msg.attach(image)


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
