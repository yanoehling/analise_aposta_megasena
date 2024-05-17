jogos = open('jogos.txt')
numeros = jogos.read().replace('\n', ' ').split()

acertos = [0, 0, 0, 0, 0, 0, 0]

aposta = []

quantidade = str(input('Quantos números vc quer apostar? ')).strip()

while not quantidade.isnumeric() or int(quantidade) not in range(6, 16):
    quantidade = str(input('\033[31mDigite uma quantidade válida: \033[m')).strip()

for c in range(0, int(quantidade)):
    num = str(input(f'{c + 1}º número: ')).strip()

    while not num.isnumeric() or int(num) not in range(1, 61) or num in aposta:
        num = str(input(f'\033[31mDigite um {c + 1}º número válido: \033[m')).strip()
    aposta.append(num)
print()

for c in range(len(numeros)):
    cont = 0
    if c % 6 == 0:
        jogo = numeros[c - 5:c + 1]
        if len(jogo) > 0:
            for ap in aposta:
                for jg in jogo:
                    if ap == jg:
                        cont += 1
            acertos[cont] += 1

print(f'Seu jogo: ', end='')
for x in aposta:
    print(x, end=' ')
print()
print(f'Em {(len(numeros) - 1) / 6:.0f} jogos, você conseguiria:')
print('-'*32)

nomes = ['Nenhum acerto', '1 acerto', '2 acertos', '3 acertos', 'Quadra', 'Quina', 'Sena']
print('Você conseguiria ->')
for c in range(0, 7):
    print(f'{nomes[c]}: {acertos[c]} vezes')
