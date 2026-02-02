while True:
    

    nombre1 = input("Entrez un premier nombre : ")
    operation = input("opération : ")
    nombre2 = input("Entrez un deuxième nombre :")

    #Etape 2 Ok 

    if not nombre1.isnumeric() or not nombre2.isnumeric():
        raise SystemExit("Caractère inconnu, veuillez tape uniquement en chiffre")

    #Etape 3 OK
    nombre1 = int(nombre1)
    nombre2 = int(nombre2)

    #Etape 4

    
        
    match operation:
        case"+":
            resultat = nombre1 + nombre2
        case"-":
            resultat = nombre1 - nombre2
        case"*":
            resultat = nombre1 * nombre2
        case"/":
            if nombre2 != 0:
                resultat = round(nombre1 / nombre2)
            else: raise SystemExit("Error")
            
        case _: raise SystemExit("Erreur opération inconnue,")





    print(resultat)

    again = input('Voulez-vous refaire (oui/non) ?')
    if again != "oui":
        print(f"Fin du programme")
        break
