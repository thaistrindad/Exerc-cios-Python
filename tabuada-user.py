y = int(input('Digite um número: '))

if y < 1 or y > 10:
        print('Valor invalido, digite apenas números entre 1 e 10!')

else:
    for n in range (0,10+1):
        calc = y*n
        print(y, 'x', n, '=', calc)
