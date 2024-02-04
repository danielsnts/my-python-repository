from random import randint

print("Olá, seu número da Mega da Virada é:")
dezenas = ''

for i in range(6):
    dezena = randint(1,60)
    dezenas += '-'+ str(dezena)

print(f"Dezenas :{dezenas}")