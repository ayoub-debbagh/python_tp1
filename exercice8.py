notes = []
coefs = []

for i in range(4):
    note = float(input(f'note {i+1} : '))
    notes.append(note)
    coef = int(input(f'coefficient : '))
    coefs.append(coef)


moyenne = 0

for i in range(4):
    moyenne += notes[i] * coefs[i]


moyenne = moyenne / sum(coefs)
message = 'moyenne de ces 4 notes : {}, {}'.format(moyenne, 'semestre valide' if moyenne >= 10 else 'rattrapage' if 7<=moyenne<10 else 'non valide')
print(message)
