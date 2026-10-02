taches = ["Reviser python", "Faire les exercices ","lire le cours"]
print("1. Reviser Python ")
print("2. faire les exercices ")
print("3. Lire le cours ")

while True :
    try:
        numero= int(input("numero de la tache :"))
    except ValueError:
        print("Entre un nombre entier ")
        
    else:
        if 1 <= numero <= len(taches) :
            print (taches[numero - 1])
            break 
        else:
            print("chissisez un numero entre 1 et 3.")
            
    finally:
        print("fin de la tentative.")
        
      


     
      
    
     