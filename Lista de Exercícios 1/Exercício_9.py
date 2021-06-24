'Exercício 9 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado'
km = float(input('Informe a quantidade de kms percorridos: '))
dia = int(input('Informe a quantidade de dias pelo qual o carro foi alugado: '))

preco = ((60 * dia) + (0.15 * km))

print(f'O preço é pagar é de R$ {preco:.2f}')