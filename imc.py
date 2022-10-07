genero = input("Qual seu genero? Digite (a) para feminino e (b) para masculino: ")
peso = float(input('Qual o seu peso em Kg? '))
altura = float(input('Qual sua altura em metros? '))

calc = peso//altura**2
print ('O seu imc é:', calc)

if calc <= 18.5:
    print('Está abaixo do peso.')
elif calc >= 18.5 and calc <= 24.9:
    print('Peso normal.')
elif calc >= 25.0 and calc <= 29.9:
    print('Está acima do peso.')
elif calc > 40:
    print('Obesidade Grau 3')

