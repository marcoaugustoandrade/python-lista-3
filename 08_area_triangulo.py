base = 0
altura = 0

while True:
    base = float(input('Informe a base do triângulo (cm): '))
    if base > 0:
        break

while True:
    altura = float(input('Informe a altura do triângulo (cm): '))
    if altura > 0:
        break

print("A área do triângulo é %.2f." % ((base * altura) / 2))
