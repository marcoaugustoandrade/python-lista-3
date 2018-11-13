num = int(input('Informe um número inteiro: '))
divisores = 0

for i in range(1, num):
    if num % i == 0:
        divisores += i

print("A soma dos divisores de %d é %d." % (num, divisores))
