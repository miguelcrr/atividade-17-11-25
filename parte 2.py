def validar_resposta(pergunta):
    while True:
        resposta = input(pergunta)
        if resposta.upper() == 'S':
            return True
        elif resposta.upper() == 'N':
            return False
        else:
            print('Resposta invalida')

with open('pessoas.txt','r') as arquivo:
    nomes=arquivo.readlines()
    for nome in nomes:
        presente=validar_resposta(f'{nome.strip()} esta presente?')
        if presente:
            with open('presente.txt','w') as arquivo:
                arquivo.write(nome)
        else:
            with open('faltantes.txt','w') as arquivo:
                arquivo.write(nome)