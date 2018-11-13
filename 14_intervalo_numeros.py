range1 = 0
range2 = 0
range3 = 0
range4 = 0

for i in range(0,10):
    num = float(input('Informe um número entre 0 e 100: '))
    if 0 <= num <= 25.9:
        range1 += 1
    elif 26 <= num <= 50.9:
        range2 += 1
    elif 51 <= num <= 75.9:
        range3 += 1
    elif 76 <= num <= 100:
        range4 += 1

print("Há %d números no intervalo [0 a 25.9]" % range1)
print("Há %d números no intervalo [26 a 50.9]" % range2)
print("Há %d números no intervalo [51 a 75.9]" % range3)
print("Há %d números no intervalo [76 a 100]" % range4)
