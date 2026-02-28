nombre1=float(input("entrer le premier nombre:"))
nombre2=float(input("entrer le deuxieme nombre:"))
print("1- addition")
print("2- soustraction")
print("3- multiplication")
print("4- division")
choix=int(input("choisir une option:"))
if(choix==1):
    print("a+b:",nombre1+nombre2)
elif(choix==2):
    print("a-b:",nombre1-nombre2)
elif(choix==3):
    print("a*b:",nombre1*nombre2)
elif(choix==4):
    try:
        print("a/b:",nombre1/nombre2)
    except ZeroDivisionError:
        print("erreur: division par zero")