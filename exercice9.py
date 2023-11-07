articles = []

for i in range(2):
    nom = input("Nom du 1er article : ")
    qte = int(input('Quantite du 1er article : '))
    prix = float(input('Prix unitaire du 1er article : '))
    articles.append({'nom':nom, 'qte':qte, 'prix':prix, 'totaleHT':prix * qte, 'totaleTTC':(prix * qte) * 1.2})

totaleTTC = 0
for i in range(2):
    print(f"Totale pour l'article {articles[i].get('nom')} : {articles[i].get('totaleHT')} Dh (HT)")
    totaleTTC += articles[i].get('totaleTTC')
2
print("Le totale de votre facture est : {:.2f} Dh (TTC)".format(totaleTTC))

