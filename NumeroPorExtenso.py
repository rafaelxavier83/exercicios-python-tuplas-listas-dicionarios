cont = ('zero', 'um', 'dois', 'tres', 'quatro', 
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quartoze', 
        'quinze', 'dezesseis', 'dezessete', 'dezeoito', 
        'dezenove', 'vinte')    
while True:
    num = int(input('Digite um numero entre 0 e 20: '))    
    if num >= 0 and num <= 20:
            break
    print('Tente novamente. ', end=' ')   
print(f'Você digitou o numero {cont[num]}')
