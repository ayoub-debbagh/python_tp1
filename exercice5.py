number = int(input('Entrer un entier : '))

resultat = {'1':"Ce nombre est pair", '2':"Ce nombre est impair, mais est multiple de 3", '3':"Ce nombre n'est ni pair ni multiple de 3"}

indice = '1' if (number % 2 == 0) else ('2' if (number % 3 == 0) else '3')

print(resultat.get(indice))