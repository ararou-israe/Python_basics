age=int(input("entrer ton age:"))
if(age>0 and age<=12):
    print("tu es un enfant")
elif(age>12 and age<=18):
    print("tu es un adolescent")
elif(age>18 and age<=60):
    print("tu es un adulte")
else:
    print("tu es un senior")