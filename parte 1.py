def validar_resposta(pergunta):
    while True:
        resposta = input(pergunta)
        if resposta.upper() == 'S':
            return True
        elif resposta.upper() == 'N':
            return False
        else:
            print('Resposta invalida')


with open('pessoas.txt', 'w') as file:
    coletando=True
    while (coletando):
        nome=input('Digite o nome: ')
        file.write(f'{nome}\n')

        if not validar_resposta('Deseja continuar?'):
            coletando=False