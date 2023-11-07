login = input("Nom d'utilisateur : ")
passwd = input("Mot de passe : ")

if login == "admin" and passwd == "admin":
    print('Bienvenue!')
else:
    print("Le nom d'utilisateur ou le mot de passe est incorrecte!")