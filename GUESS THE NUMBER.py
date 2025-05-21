import random

def guess_the_number():
    print("Bienvenue au jeu Devinez le nombre !")
    print("Je pense à un nombre entre 1 et 100. Pouvez-vous deviner ce que c'est ?")

    # Générer un nombre aléatoire entre 1 et 100
    secret_number = random.randint(1, 100)

    while True:
        try:
            guess = int(input("Entrez votre estimation : "))
            
            if guess < 1 or guess > 100:
                print("Veuillez entrer un nombre entre 1 et 100.")
                continue

            if guess < secret_number:
                print("Votre estimation est trop basse. Réessayez.")
            elif guess > secret_number:
                print("Votre supposition est trop élevée. Réessayez.")
            else:
                print("🎉 Félicitations ! Vous avez deviné le numéro correctement !")
                break
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier.")

# Démarrer le jeu
guess_the_number()
