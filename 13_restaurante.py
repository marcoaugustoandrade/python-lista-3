alunos = 0
menos10 = 0
entre10e20 = 0
mais20 = 0

while True:
    refeicoes = int(input('Quantas refeições você fez no mês? '))
    alunos += 1
    if refeicoes < 10:
        menos10 += 1
    elif 10 <= refeicoes <= 20:
        entre10e20 += 1
    elif refeicoes > 20:
        mais20 += 1
    m = input("Deseja informar mais algum (s/n)?")
    if m == 'n':
        break

print("Alunos entrevistados: %d" % alunos)
print("Alunos que fizeram menos de 10 refeições ao mês: %d" % menos10)
print("Alunos que fizeram entre 10 e 20 refeições ao mês: %d" % entre10e20)
print("Alunos que fizeram mais de 20 refeições ao mês: %d" % mais20)
