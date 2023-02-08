import requests
import smtplib
import csv
import json
#conferir game_mode


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
            cod[i] = new_cod[i]
            if int(match['deaths']) - int(match['kills']) >= 10:
                print('é listaaaa')
                f_email(galera[i],match)
    return cod


def f_match(sujeito):
    url = f"https://api.opendota.com/api/players/{sujeito}/recentMatches?limit=1"
    response = requests.get(url)
    data = response.json()
    return data[0]


def f_email(artista,match):
    cred = [*csv.DictReader(open('cred.csv', encoding='utf-8'))]
    with open("dados.json", "r") as json_file:
    # Carrega o conteúdo do arquivo como dicionário
        heroi = json.load(json_file) 



    user = cred['login']
    password = cred['senha']

    sent_from = user
    to = to
    subject = f"Parabéns {artista['ID']}! É Listaaaaa!!"
    body = f"Parabéns {artista['Nome']}!\n\nVocê foi devidamente listado pelo seu desempenho incrível na partida brilhante!",
    f"\nAqui está sua obra jogando de {heroi['name']}",
    f"\n\nKills: {match['kills']}\nMortes: {match['deaths']}"

    email_text = f"""\
    From: {sent_from}
    To: {to}
    Subject: {subject}

    {body}
    """

    try:
        server = smtplib.SMTP('smtp.gmail.com', 465)
        server.ehlo()
        server.starttls()
        server.login(user, password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print ('Email enviado!')
    except Exception as e:
        print ('Algo deu errado...')
        print (e)