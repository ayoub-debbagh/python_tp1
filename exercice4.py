nbrSeconds = int(input('Nombre de secondes : '))

hours = nbrSeconds // 3600

min = (nbrSeconds % 3600) // 60

seconds = (nbrSeconds % 3600) % 60


hours = str(hours) + " h" if hours != 0 else ""
min = str(min) + " min" if min else ""
seconds = str(seconds) + " sec"

print(f'{nbrSeconds} secondes = {hours} {min} {seconds}')