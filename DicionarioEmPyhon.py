aluno = {}
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Média do {aluno["nome"]}: '))
print('-='*30)
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] < 7:
    aluno['situacao'] = 'Recuperacao'
else:
    aluno['situacao'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
