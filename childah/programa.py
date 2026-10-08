#----ADIVINHE O NÚMERO----#

import random

numero_secretob = random.randint(1, 20)
tentativas = 0

print('pensei em um número de 1 a 20. Consegue acertar?')

while True:
    palpite = int(input("seu palpite:"))
    tentativas += 1

    if palpite < numero_secretob:
        print("muito baixo! tente um número maior")
    elif palpite > numero_secretob:
        print("muito alto! tente um número menor")
    else:
        print('acertou em {tentativas} tentativa(s)!.')
        break

    