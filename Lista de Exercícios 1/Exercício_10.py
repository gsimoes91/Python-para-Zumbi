'Exercício 10 - Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias'
qtd = int(input('A quantidade de cigarros fumados por dia é de: '))
anos = int(input('Há quantos anos é fumante? '))

red = ((qtd * 10 * anos * 365) / 60) / 24

print(f'O total de dias perdidos na sua vida já é de {red:.0f} dias')