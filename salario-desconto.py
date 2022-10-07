sal = int(input('Digite o sálario bruto: '))

if sal < 1200:
    print('A porcentagem do desconto é 0%')
elif sal == 1200 or sal <= 3500:
    print('A porcentagem do desconto é 9,4%')
elif sal > 3500:
    print('A porcentagem do desconto é 21,1%')
if sal <=0:
    print('Não é permitido valor negativo!')
