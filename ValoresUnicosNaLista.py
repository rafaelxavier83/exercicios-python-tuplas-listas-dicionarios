lista = []
while True:
    n = int(int(input('Digite um valor: ')))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')    
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print('='*30)
print(f'Você digitou os valores {sorted(lista)}')
