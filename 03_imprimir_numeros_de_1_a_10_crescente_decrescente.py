ordem = input('Qual a ordem de impressão (c/d)?')

if ordem == 'c':
    for i in range(1, 11):
        print(i)
elif ordem == 'd':
    i = 10
    while i > 0:
        print(i)
        i -= 1
