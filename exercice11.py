poids = float(input('Le poids en Kg : '))
taille = float(input('La taille en m : '))

imc = poids/(taille**2)

message = ""

if imc > 40:
    message = "Obésité morbide ou massive"
elif 35 < imc <= 40:
    message = "Obésité sévère"
elif 30 < imc <= 35:
    message = "Obésité modérée"
elif 25 < imc <= 30:
    message = "Surpoids"
elif 18.5 < imc <= 25:
    message = "Corpulence normale"
elif 16.5 < imc <= 18.5:
    message = "Maigreur"
else :
    message = "Famine"


print(message)