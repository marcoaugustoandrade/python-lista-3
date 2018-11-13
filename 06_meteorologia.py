temperaturas = 0
maior = None
menor = None
contador = 0

while True:
    temperatura = float(input('Informe a temperatura: '))
    temperaturas += temperatura

    if maior == None or temperatura > maior:
        maior = temperatura

    if menor == None or temperatura < menor:
        menor = temperatura

    contador += 1

    mais = input('Deseja ler mais temperaturas (s/n)?')
    if mais == 'n':
        break

print("A maior temperatura foi de %.2f" % maior)
print("A menor temperatura foi de %.2f" % menor)
print("A média das temperaturas foi de %.2f" % (temperaturas / contador))
