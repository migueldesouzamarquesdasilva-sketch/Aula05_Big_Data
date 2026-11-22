print('''
[1] - Sul
[2] - Norte
[3] - Leste
[4] - Oeste
[5 ou 6] - Noroeste
[7 a 9] - Sudeste
[10] - Centro - Oeste
[11] - Noroeste
''')

opcao = int(input('Escolha uma opção: '))

match opcao:
    case 1:
        print('Sul')

match opcao:
    case 2:
        print('Norte')

match opcao:
    case 3:
        print('Leste')

match opcao:
    case 4:
        print('Oeste')

match opcao:
    case 5 | 6:
        print('Noroeste')

match opcao:
    case 7 | 8 | 9:
        print('Sudeste')

match opcao:
    case 10:
        print('Centro-Oeste')

match opcao:
    case 11:
        print('Noroeste')









