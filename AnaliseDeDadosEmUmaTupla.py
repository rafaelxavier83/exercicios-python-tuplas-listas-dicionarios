num = (int(input('Informe um numero: ')), int(input('Informe um numero: ')), int(input('Informe um numero: ')), int(input('Informe um numero: ')))
print(f'Você digitou os numeros {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes ')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
for n in num:
    if n % 2 == 0:
        print(f'Os valores pares digitados foram {n}')
