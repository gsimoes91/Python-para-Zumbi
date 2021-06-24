'Exercicio 5 - Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.'
mercadoria = float(input('O preço da mercadoria é: '))
desconto = float(input('O desconto é de: '))

desconto = mercadoria * (desconto/100)
mercadoria = mercadoria - desconto

print(f'O desconto é de: R${desconto:.2f}',f' e o preço a pagar é de: R${mercadoria:.2f}')