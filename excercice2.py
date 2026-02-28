
contacts=["1234","4321","2345","5432"]

print("1- ajouter un contact a votre liste")
print("2-afficher mes contacts")
print("3-quiter le programme")



choix=int(input("choisir une option:"))
    
if(choix==1):
        try:
            cont=int(input("contact a ajouter:"))
            contacts.append(cont)
            print("contact ajouter avec succes")
            for i, c in enumerate(contacts):
                 print(i,c)
            
        except Exception as e:
            print("erreur: ",e)

elif(choix==2):
        for i, c in enumerate(contacts):
            print(i,c)
       
else:
    print("au revoir")
    





 







