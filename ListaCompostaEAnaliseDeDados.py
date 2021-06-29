temp = []
princ = []

cont = maior = menor = 0
while True:
    temp.append(input('Nome: '))
    cont += 1
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = temp[1]
        menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]').strip().upper()[0]
    if resp == 'N':
        break
print('-='*30)
print(f'Ao todo você cadastrou {cont} pessoas.')
print(f'O maior peso foi de {maior}kg. Peso de ', end= '')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end ='')
print()
print(f'O menor peso foi de {menor}kg. Peso de ', end = '')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end = '')
print()
