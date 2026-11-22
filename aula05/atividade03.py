valor_compra = float(input('Digite o valor da compra: '))
programa_fidelidade = (input('Você é cadastrado no programa de fidelidade? [S/N]: ')).lower()[0]

FRETE = 25

if valor_compra > 200 or programa_fidelidade == 's':
    valor_final = valor_compra
    print(f'Frete grátis!\n Valor final: R$ {valor_final}')
    

else:
    valor_final = valor_compra + FRETE
    print(f'Frete de R$25.')
    print(f'Valor final: {valor_final}')
    