menor = None
maior = None

for i in range(1,11):
    n = int(input('Informe o %d número: ' % i))
    if menor == None or n < menor:
        menor = n
    if maior == None or n > maior:
        maior = n

print("O menor número digitado foi %d" % menor)
print("O maior número digitado foi %d" % maior)
