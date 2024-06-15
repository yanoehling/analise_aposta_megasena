import pandas 


todos_jogos = pandas.read_excel('historico_jogos_ms.xlsx')
acertos = [0, 0, 0, 0, 0, 0, 0]
aposta = []

quant_aposta = input('Quantos números vc quer apostar? ')
while not quant_aposta.isnumeric() or int(quant_aposta) not in range(6, 16):
    quant_aposta = input('Digite uma quantidade válida: ')

for cont in range(int(quant_aposta)):
    num = input(f'{cont+1}º número: ')
    while not num.isnumeric() or int(num) not in range(1, 61) or num in aposta:
        num = str(input(f'Digite um {cont+1}º número válido: '))

    aposta.append(int(num))

for linha in range(len(todos_jogos)):
    nivel = 0
    for bola in todos_jogos.iloc[linha][1:]:
        for num in aposta:
            if num == bola:
                nivel += 1
    if nivel == 6:
        dia = todos_jogos.iloc[linha][0]

    acertos[nivel] += 1

print()
nomes = ['Nenhum acerto', '1 acerto', '2 acertos', '3 acertos', 'Quadra', 'Quina', 'Sena']
print(f'Em {len(todos_jogos)} jogos, você conseguiria:')
print('-'*32)
for c in range(7):
    print(f'{nomes[c]}: {acertos[c]} vezes')
if acertos[6] >= 1:
    print(f'-- Com essa combinação, você ganharia na megasena dia {dia}! --')
print()
