a = open('jogos.txt')
numeros = a.read().replace('\n', ' ').split()

acertos = [0, 0, 0, 0, 0, 0, 0]

aposta = []

n = str(input('Quantos números vc quer apostar? ')).strip()

while not n.isnumeric() or int(n) not in range(6, 16):
    n = str(input('\033[31mDigite uma quantidade válida: \033[m')).strip()

for y in range(0, int(n)):
    x = str(input(f'{y + 1}º número: ')).strip()

    while not x.isnumeric() or int(x) not in range(1, 61) or x in aposta:
        x = str(input(f'\033[31mDigite um {y + 1}º número válido: \033[m')).strip()

    aposta.append(x)
print()

for c, v in enumerate(numeros):
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
for c in range(0, 7):
    print(f'{nomes[c]}: {acertos[c]} vezes')
