password="python123"
user_password=input("entrer le mot de passe:")

while user_password!=password:
    print("mot de passe incorrect, essayez à nouveau.")
    user_password=input("entrer le mot de passe:")
print("mot de passe correct, bienvenue!")
    