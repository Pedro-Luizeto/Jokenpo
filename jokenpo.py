
def espaçamento():
    print('=====================')

while True:
    print('=== J O K Ê N P O ===')
    espaçamento()
    print('Escolha uma opção:')
    print('1 - Jogar')
    print('2 - Sair')
    escolha = input('Digite sua escolha: ')
    espaçamento()

    if escolha == '1':
        import random

        opcoes = ['pedra', 'papel', 'tesoura']
        computador = random.choice(opcoes)

        jogador = input('Escolha pedra, papel ou tesoura: ').lower()

        if jogador not in opcoes:
            print('Opção inválida. Tente novamente.')
            continue

        print(f'Computador escolheu: {computador}')
        print(f'Jogador escolheu: {jogador}')

        if jogador == computador:
            print('Empate!')
        elif (jogador == 'pedra' and computador == 'tesoura') or (jogador == 'papel' and computador == 'pedra') or (jogador == 'tesoura' and computador == 'papel'):
            print('Você venceu!')

        else:
            print('Você perdeu!')

    elif escolha == '2':
        print('Saindo do jogo...')
        break