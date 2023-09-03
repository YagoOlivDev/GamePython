from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
while True:
    print('\033[1;30m=-\033[m' *20 )
    print ('\033[1;38mSuas opções: ')
    print ('\033[1;38m[ 0 ] Pedra')
    print ('\033[1;38m[ 1 ] Papel')
    print ('\033[1;38m[ 2 ] Tesoura')
    print('\033[1;30m=-\033[m' *20 )
    j = int(input('\033[1;38mQual é sua jogada?'))
    while j != 1 and j != 2 and j != 3:
        print('Opção Inválida!')
        print('\033[1;38mSuas opções: ')
        print('\033[1;38m[ 0 ] Pedra')
        print('\033[1;38m[ 1 ] Papel')
        print('\033[1;38m[ 2 ] Tesoura')
        j = int(input('\033[1;38mQual é sua jogada?'))
    print('\033[1;30m=-\033[m' *20 )
    print('\033[1;38mJogador jogou {}'.format(itens[j]))
    sleep(1)
    print('\033[1;38mJo')
    sleep(1)
    print('\033[1;38mKen')
    sleep(1)
    print('\033[1;38mPo!!')
    sleep(1)
    print('\033[1;38mComputador jogou {}'.format(itens[computador]))
    print('\033[1;30m=-\033[m' *20 )
    if computador == 0:
        if j == 0:
            print('\033[1;38mDeu empate!')
        elif j == 1:
            print('\033[1;38mJogador vence!')
        elif j == 2:
            print('\033[1;38mComputador Vence!')
        else:
            print('\033[1;38mJogada invalida!')
    elif computador == 1:
        if j == 0:
            print('\033[1;38mComputador vence!')
        elif j == 1:
            print('\033[1;38mDeu empate!')
        elif j == 2:
            print('\033[1;38mJogador Vence!')
        else:
            print('\033[1;38mJogada invalidada!')
    elif computador == 2:
        if j == 0:
            print ('\033[1;38mJogador Vence!')
        elif j == 1:
            print ('\033[1;38mComputador Vence!')
        elif j == 2:
            print ('\033[1;38mDeu empate!')
        else:
            print('\033[1;38mJogada invalida!')
    cont = str(input('\033[1;38mQuer jogar novamente? [S/N] ').upper())
    while cont != 'S' and cont != 'N':
        cont = str(input('\033[1;38mQuer jogar novamente? [S/N] ').upper())
    if cont == 'S':
        continue
    elif cont == 'N':
        exit()
print('\033[1;38mFim De Jogo!')
print('\033[1;30m=-\033[m' *20 )