from  validation import verifier_priorite
from taches import ajouter_tache

taches = []
while True :
    titre = input("Titre de la tache :")
    priorite = input("prioriter(basse/haute):")
    try:
        priorite_validee = Verifier_priorite(priorite)
        taches = ajouter_tache(taches , titre ,prioriter_validee)
        print("Liste des taches :" , taches)
        break
    except ValueError as erreur :
        print(erreur)
        print("veuillez recommencer. /n")
        
    