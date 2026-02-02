a = input(' Nome do Aluno? ')
n1 = float(input(' Sua primeira nota e '))
n2 = float(input(' Sua segunda nota e '))
situacao = float( n1 + n2 )
print (' O aluno {} teve nota {} e esta:'.format(a,situacao))
if situacao >= 7:
    print('Aprovado')
elif situacao >= 5:
    print(' Recuperacao')
else:
    print('Reprovado')
# rint (' O aluno {} teve nota {}:'.format(a,situacao))
