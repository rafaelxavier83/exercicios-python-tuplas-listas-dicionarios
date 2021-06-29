lista = []
listaPar = []
listaImpar = []
while True:
    lista.append(int(input('Digite um numero: ')))   
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        listaPar.append(v)
    elif v % 2 == 1:
        listaImpar.append(v)   
print('-='*30)
print(f'A lista completa é {sorted(lista)}')
print(f'A lista de pares é {sorted(listaPar)}')
print(f'A lista de impares é {sorted(listaImpar)}')
