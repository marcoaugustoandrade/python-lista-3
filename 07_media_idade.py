idade = None
idades = 0
contador = 0
while idade != 0:
    idade = int(input('Informe a idade: '))
    idades += idade
    if idade != 0:
        contador += 1

print("A média de idade do grupo é %i." % (idades / contador))
