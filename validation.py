def verifier_priorite(valeur) :
    if valeur == "basse " or valeur == "haute" :
                 return valeur 
    raise ValueError("La priorite doit etre basse ou haute ")
