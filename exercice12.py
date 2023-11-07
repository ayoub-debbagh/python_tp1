def prime(grade, hours) :
    prim = 0
    if grade == 'A':
        if hours >= 20:
            prim += 1000 * (hours//20)
    elif grade == 'B':
        if hours >= 20:
            prim += 800 * (hours//20) 
    elif grade == 'C':
        if hours >= 15:
            prim += 500 * (hours//15)
    elif grade == 'D':
        if hours >= 15:
            prim += 350 * (hours//15)
    elif grade == 'E':
        if hours >= 10:
            prim += 100 * (hours//10)

    return prim

grade = input("Entrer votre grade : ")

hours = int(input("Entrer le nombre d'heures de travail : "))

grades = ('A', 'B', 'C', 'D', 'E')
incomePerHour = dict(A=200, B=150, C=120, D=100, E=80)

salary =  0

if grade in grades and hours > 0:
    salary = incomePerHour.get(grade, 0)
    salary *= hours
    salary += prime(grade, hours)


print(f'Salary = {salary} Dh')


