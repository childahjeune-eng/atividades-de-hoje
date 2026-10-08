import random

numero_secreto = random.randint(1, 20)

print('pensei em um número de 1 20. Você tem 5 tentativas!')

for tentativas in range(1, 6):
    palpite = int(input('seu palpite:'))

    if palpite < numero_secreto:
        print('muito baixo. tente um número maior')
    elif palpite > numero_secreto:
        print('muito alto. tente um número menor')
    else:
        print(f'acertou em {tentativas} tentativas!')
        break
else:
    print(f'Acabaram as tentativas! O número secreto era: {numero_secreto}')
    