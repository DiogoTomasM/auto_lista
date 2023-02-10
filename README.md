# auto_lista
Conferência automática de k/d nas partidas de Dota 2, utilizando a API do OpenDota, dos usuários específicados no arquivo. Caso o valor de D - K sejá igual ou maior que 10, será notificado por e-mail e terá as informações básicas da partidas salvas numa planilha pública

O script precisa dos arquivos:
- cred.csv (arquivo csv que deve conter o formato, contendo obrigatoriamente 1 linha + cabeçalho):
    login,senha
    example@example.com,example123
    
- nomes.csv (arquivo csv que contém os jogadores que deseja incluir no auto_lista, contendo no mínimo 1 linha + cabeçalho [pode conter um número indeterminado de linhas]):
    Nome,ID,e-mail,Nick
    Name,steam32ID,example@example.com,nick


# Próximos updates:
- Editar a planilha de excel com ela estando no OneDrive
- Melhorar a disposição de informações da partida no escopo do email 
- Setar regras específicas para ser incluso na lista (futuramente incluir parte estatística de machine learning)
- Registrar internamente quantas vezes cada pessoa ainda tem direito de contestar a inclusão dela na lista naquele semestre (resetando nos dias 01/01 e 1/07)
