soma_pares = 0
mult_impares = 1

num1 = int(input('Informe o 1º número: '))
num2 = int(input('Informe o 2º número: '))

if num1 < num2:
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            soma_pares += i
        else:
            mult_impares *= i
elif num1 > num2:
    for i in range(num2, num1 + 1):
        if i % 2 == 0:
            soma_pares += i
        else:
            mult_impares *= i

print("A soma dos números pares do intervalor é %d" % soma_pares)
print("A multiplicação dos números ímpares do intervalor é %d" % mult_impares)
