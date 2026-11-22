nota01 = float(input('Digite sua nota 01: '))
nota02 = float(input('Digite sua nota 02:'))
nota03 = float(input('Digite sua nota 03:'))
nota04 = float(input('Digite sua nota 04:'))

media = (nota01 + nota02 + nota03 + nota04)/4

if media>= 7:
    print('Aprovado!')

elif media>= 5:
    print('Em recuperação!')

else:
    print('Reprovado!')

print(f'Média: {media}')



    

    


