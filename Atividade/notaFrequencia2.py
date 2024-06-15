nota = float(input('Digite uma nota de 1 a 10: '))
frequencia = float(input('Digite a frenquencia da aluna: '))

if nota >= 7 or frequencia >= 75:
    print('Tu foi aprovada')
elif nota >=1 and nota <=10 and frequencia <= 75:
    print('Reprovada!')  
else:
    print('ERRO!')
