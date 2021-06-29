valores = []
menor = 0
maior = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        maior = valores[c]
        menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('-='*50)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior}. Na posição ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end=' ')
print() 
print(f'O menor valor digitado foi {menor}. Na posição ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
print()
