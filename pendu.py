from fonctions import * 
from donnees import * 

# Scores des joueurs
infos_Joueurs = dict()
score = 0
mot_AuHasard = ""
liste_lettres_trouvees = list()
nb_chances_du_joueur = nb_Chances

# Demander le nom du joueur
nom_joueur = input("Entrez votre nom: ")
nom_joueur = nom_joueur.upper()

# Récupérer les informations concernant le joueur
infos_Joueurs = RecupererScore()
if nom_joueur in infos_Joueurs.keys():
    score = infos_Joueurs[nom_joueur]

# Affichage du score
print("Bonjour! Vous avez un score de ", score, " points. Bonne chance!")

# On sélectionne un mot au mot_AuHasard
mot_AuHasard = RetourneMotHasard()
mot_AuHasard = mot_AuHasard.upper()

# On affiche le mot
mot_AAfficher = AfficherMot(mot_AuHasard, liste_lettres_trouvees)
mot_AAfficher = mot_AAfficher.upper()

le_jeu_continue = True
print("VOICI LE MOT A DECOUVRIR: ", mot_AAfficher)

# Demander une lettre à l'utilisateur
while nb_chances_du_joueur  != 0 and le_jeu_continue:
    lettre_choisie = input("    une lettre: ")
    
    lettre_en_majuscule = lettre_choisie.upper()
    
    if lettre_en_majuscule  not in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ") or len(lettre_en_majuscule)==0:
        print("lettre non valide")
    else:
        # Vérifier si la lettre est dans le mot
                
        if lettre_en_majuscule in mot_AuHasard:
        # Afficher le nouveau mot_AAfficher

            if lettre_en_majuscule in liste_lettres_trouvees:
                print("Vous avez déjà trouvé cette lettre: ", lettre_en_majuscule)
            else:
                liste_lettres_trouvees.append(lettre_en_majuscule ) 
                mot_AAfficher = AfficherMot(mot_AuHasard, liste_lettres_trouvees)
                
                print(mot_AAfficher)
                # La partie est terminée si les 2 mots correspondent
                if mot_AAfficher == mot_AuHasard:
                    le_jeu_continue = False
                                
                    # Sauvegarder le nouveau score du joueur
                    score += nb_chances_du_joueur 
                    
                    print("Bravo ! Vous avez cumulé ", score, " points.")
        else:
            print("Pas de lettre: ", lettre_en_majuscule, " dans le mot. Il vous reste ", nb_chances_du_joueur, " essais.")
            # Le joueur vient de perdre une chance de jouer.
            nb_chances_du_joueur  -= 1

if nb_chances_du_joueur == 0:
    score = 0
        
infos_Joueurs[nom_joueur] = score
SauvegarderScore(infos_Joueurs)
  
print("Jeu terminé avec un score de: ", score)
