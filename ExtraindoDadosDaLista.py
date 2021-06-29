lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print(lista)
print(f'Você digitou {cont} elementos.')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse = True)}')
if 5 in lista:
    print(f'O valor {5} faz parte da lista!')
else:
    print(f'O valor {5} não foi encontrado na lista!')
