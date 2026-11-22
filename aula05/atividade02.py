nota_final = float(input('Digite sua nota: '))
Frequencia = float(input('Digite sua frequência: '))
mensalidade = float(input('Digite o valor da sua mensalidade: '))

desconto = mensalidade * 0.20
Frequencia * 0.75
valor_final = mensalidade - desconto

if Frequencia >= 75 or nota_final >= 7:
    print('Você ganhou bolsa de 20%!')
    print(f'Valor a pagar: {valor_final}')


else:
    print('Você não ganhou bolsa de 20%.')





