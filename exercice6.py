number1 , number2 = int(input("Entrer un nombre : ")), int(input("Entrer un autre : "))

result = ""

if number1 > 0 and number2 < 0 or number1 < 0 and number2 > 0:
    result = "Le produit est negatif"
else:
    result = "Le produit est positif"

print(result)