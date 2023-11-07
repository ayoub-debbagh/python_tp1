number1 , number2 = int(input("Entrer un nombre : ")), int(input("Entrer un autre : "))
operator = input("Entrer l'operateur : ")

result = str(number1) + operator + str(number2)

print(eval(result))