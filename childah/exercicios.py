# 1 - CRIE UM PROGRAMA QUE PARA CALCULAR O IMC DO USUÁRIO
# 2 - CRIE UM PROGRAMA QUE PEÇA UM NOME E UMA IDADE E MOSTRE A FRASE: "OLÁ, _______. DAQUI A 10 ANOS VOCÊ TERÁ X ANOS"
# 3 - FAÇA UM PROGRAMA QUE PEÇA UMA TEMPERATURA EM CELSIUS E CONVERTA PARA FAHRENHEIT (F = C * 9/5 + 32)
# 4 - FAÇA UM PROGRAMA QUE PEÇA 3 NOTAS E FAÇA A MÉDIA.
# 5 - FAÇA UM PROGRAMA QUE PEÇA A BASE E A ALTURA DE UM RETÂNGULO E MOSTRE A ÁREA E O PERÍMETRO.
# 6 MELHORE O PROGRAMA DE IMC CRIANDO CONDIÇÕES PARA:
#Menor que 18,5	Magreza / Abaixo do peso
#Entre 18,5 e 24,9	Peso normal (saudável)
#Entre 25,0 e 29,9	Sobrepeso
#Entre 30,0 e 34,9	Obesidade Grau I
#Entre 35,0 e 39,9	Obesidade Grau II
#Maior ou igual a 40,0	Obesidade Grau III (Grave)

1

peso = float(input('Digite seu peso (kg):'))
altura = float(input('Digite sua altura (m):'))

imc = peso / (altura ** 2)

print('aeu IMC  é:', imc)



2

nome = input('Digite seu nome:')
idade = int(input('Digite sua idade:'))

print('Olá,  nome + "!"')
print('Daqui a 10 anos você terá', idade + 10, 'anos.')



3

celsius = float(input('Digite a temperatura em Celsius:'))
fahrenheit = celsius * 9/5 + 32

print('A temperatura em Fahrenheit é:', fahrenheit)



4

nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
nota3 = float(input('Digite a terceira nota:'))

media = (nota1 + nota2 + nota3) / 3

print('A média das notas é:', media)



5

base = float(input('Digite a base do retângulo:'))
altura = float(input('Digite a altura do retângulo:'))

area = base * altura
perimetro = 2 * (base + altura)

print('A área é:', area)
print('O perímetro é:', perimetro)



6

imc = float(input('Digite seu IMC:'))

if imc < 18.5:
    print('Magreza / Abaixo do peso')
elif imc < 25:
    print('Peso normal (saudável)')
elif imc < 30:
    print('Sobrepeso')
elif imc < 35:
    print('Obesidade Grau I')
elif imc < 40:
    print('Obesidade Grau II')
else:
    print('Obesidade Grau III (Grave)')