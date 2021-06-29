times = ('Corinthias', 'Palmeiras', 'Santos', 'Grêmio', 
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 
         'Atletico', 'Botafogo', 'Atletico - PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport', 'Vitoria', 
         'Coritiba', 'Avai', 'Ponte Preta', 'Atletico - Go')
print(f'Times do Brasileirão: {times}')
print('-='*70)
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print('-='*70)
print(f'Os 4 ultimos colocados são: {times[-4:]}')
print('-='*70)
print(f'Times em ordem afabetica {sorted(times)}')
print('-='*70)
print(f'O Chapecoense estar na {times.index("Chapecoense")+1}º posição')
