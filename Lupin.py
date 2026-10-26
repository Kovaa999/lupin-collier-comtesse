import random

# ---------- VARIABLES DE DÉPART ----------
pts_suspicion = 0
inventaire = []
en_cours = True
choix_valide = False
choix_2_valide = False
choix_3_valide = False
ruelle_fouillee = False
est_entre = False
dans_le_haul = True
a_parler_cuisinier = False
tours = 0
indice_lu = False

print("=== LUPIN ET LE COLLIER DE LA COMTESSE ===")
print()
print("Il est 21h. L'hôtel particulier se dresse devant toi, des lumières brillent au premier étage.")
print("Un garde patrouille près du portail.")

# ---------- GRANDE BOUCLE : on recommence tant qu'on n'est pas entré ----------
while est_entre == False:
    en_cours = True
    choix_valide = False
    choix_2_valide = False
    choix_3_valide = False

    # ----- MENU PRINCIPAL -----
    while en_cours:
        print()
        print("--- Devant l'hôtel ---")
        print("1. Entrer par la porte")
        print("2. Passer par la fenêtre")
        print("3. Te déguiser")
        print("4. Fouiller la ruelle (Fortement conseillé)")
        choix = input("Que fais-tu ? ")

        # Fouille de la ruelle
        if choix == "4":
            if ruelle_fouillee == False:
                ruelle_fouillee = True
                objets = ["carton", "crochet", "perruque", "loupe"]
                objet = random.choice(objets)
                inventaire.append(objet)
                if objet == "carton":
                    print("Tu as ramassé un carton d'invitation.")
                elif objet == "crochet":
                    print("Tu as ramassé un crochet (il peut ouvrir n'importe quelle porte).")
                elif objet == "perruque":
                    print("Tu as ramassé une perruque.")
                elif objet == "loupe":
                    print("Tu as ramassé une loupe.")
                print("Ton inventaire :", inventaire)
            else:
                print("Tu as déjà fouillé la ruelle.")
        elif choix == "1" or choix == "2" or choix == "3":
            en_cours = False
        else:
            print("Je n'ai pas compris.")

    # ----- CHOIX 1 : ENTRER PAR LA PORTE -----
    if choix == "1":
        print()
        print("--- La porte ---")
        print("A. Tenter de bluffer : « Je suis invité par la comtesse. »")
        print("B. Forcer la serrure de la porte de service")
        while choix_valide == False:
            choix_1 = input("Que fais-tu ? ").upper()
            if choix_1 == "A" or choix_1 == "B":
                choix_valide = True
            else:
                print("Je n'ai pas compris.")

        if choix_1 == "A":
            seuil = 4
            if "carton" in inventaire:
                seuil = seuil - 1
            de = random.randint(1, 6)
            print("Tu as obtenu", de, "au dé (il faut", seuil, "ou plus).")
            if de >= seuil:
                pts_suspicion = pts_suspicion + 1
                print("Le valet t'a cru, tu entres !")
                est_entre = True
            else:
                pts_suspicion = pts_suspicion + 3
                print("Le valet ne t'a pas cru. Tu retournes devant l'hôtel...")
            print("Tu as", pts_suspicion, "point(s) de suspicion.")

        elif choix_1 == "B":
            if "crochet" in inventaire:
                pts_suspicion = pts_suspicion + 1
                est_entre = True
                print("Tu crochètes la serrure, bravo ! Tu entres.")
            else:
                pts_suspicion = pts_suspicion + 3
                print("Il te manque un crochet ! Tu retournes devant l'hôtel...")
            print("Tu as", pts_suspicion, "point(s) de suspicion.")

    # ----- CHOIX 2 : PASSER PAR LA FENÊTRE -----
    elif choix == "2":
        print()
        print("--- Le jardin ---")
        print("Tu fais le tour du mur et tu sautes dans le jardin sans un bruit.")
        print("La lune éclaire des rosiers et une petite cabane en bois.")
        print("Au rez-de-chaussée, une fenêtre est entrouverte : de la lumière filtre à travers les rideaux.")
        print("A. Escalader la fenêtre tout de suite")
        print("B. Fouiller le jardin d'abord")
        while choix_2_valide == False:
            choix_2 = input("Que fais-tu ? ").upper()
            if choix_2 == "A" or choix_2 == "B":
                choix_2_valide = True
            else:
                print("Je n'ai pas compris.")

        # Si on fouille d'abord, on prend la loupe puis on escalade (choix A)
        if choix_2 == "B":
            print("Tu entres dans la cabane du jardinier.")
            print("Entre les pots et les outils, tu trouves une vieille loupe. Elle pourrait servir plus tard...")
            print("Tu la glisses dans ta poche, puis tu retournes vers la fenêtre.")
            inventaire.append("loupe")
            print("Ton inventaire :", inventaire)
            choix_2 = "A"

        if choix_2 == "A":
            seuil_2 = 3
            de_choix_2 = random.randint(1, 6)
            print("Tu as obtenu", de_choix_2, "au dé (il faut", seuil_2, "ou plus).")
            if de_choix_2 >= seuil_2:
                pts_suspicion = pts_suspicion + 1
                print("Tu es passé sans faire de bruit !")
            else:
                pts_suspicion = pts_suspicion + 3
                print("Tu es passé, mais un pot de fleurs s'est cassé ! Les gardes se méfient plus.")
            print("Tu as", pts_suspicion, "point(s) de suspicion.")
            est_entre = True

    # ----- CHOIX 3 : SE DÉGUISER -----
    elif choix == "3":
        print()
        print("--- Les déguisements ---")
        print("Dans une ruelle sombre, un ami t'attend avec une valise de costumes.")
        print("« Choisis bien Arsène : chacun a ses avantages. »")
        print("A. Le valet (discret, mais sans pouvoir)")
        print("B. L'inspecteur (impressionnant, mais risqué si un vrai policier te croise)")
        print("C. La comtesse russe (le plus audacieux)")
        while choix_3_valide == False:
            choix_3 = input("Que choisis-tu ? ").upper()
            if choix_3 == "A" or choix_3 == "B" or choix_3 == "C":
                choix_3_valide = True
            else:
                print("Je n'ai pas compris.")

        # --- Le valet ---
        if choix_3 == "A":
            seuil_3 = 3
            if "perruque" in inventaire:
                seuil_3 = seuil_3 - 1
            de_choix_3 = random.randint(1, 6)
            print("Tu as obtenu", de_choix_3, "au dé (il faut", seuil_3, "ou plus).")
            if de_choix_3 >= seuil_3:
                est_entre = True
                print("Tu as pu passer inaperçu !")
            else:
                pts_suspicion = pts_suspicion + 2
                print("Tu n'es pas passé ! Tu retournes devant l'hôtel...")
            print("Tu as", pts_suspicion, "point(s) de suspicion.")

        # --- L'inspecteur (2 dés) ---
        elif choix_3 == "B":
            print("Tu enfiles le long manteau et le képi.")
            print("Tu avances d'un pas assuré vers la porte : le garde te salue.")
            seuil_3 = 2
            if "perruque" in inventaire:
                seuil_3 = 1
            de_choix_3_B = random.randint(1, 6)
            print("Premier dé :", de_choix_3_B, "(il faut", seuil_3, "ou plus).")
            if de_choix_3_B >= seuil_3:
                print("Le garde te laisse passer !")
                pts_suspicion = pts_suspicion + 1
                print("Mais à l'intérieur, un vrai policier te dévisage...")
                de_police = random.randint(1, 6)
                print("Deuxième dé :", de_police, "(sur un 1, tu es démasqué).")
                if de_police == 1:
                    pts_suspicion = pts_suspicion + 5
                    print("Tu as été démasqué, tu retournes devant l'hôtel...")
                else:
                    print("Le policier ne se doute de rien. Tu es passé, félicitations !")
                    est_entre = True
            else:
                pts_suspicion = pts_suspicion + 2
                print("Le garde te refuse l'entrée. Tu retournes devant l'hôtel...")
            print("Tu as", pts_suspicion, "point(s) de suspicion.")

        # --- La comtesse russe (entrée directe + danse) ---
        elif choix_3 == "C":
            print("Tu entres par la grande porte sous les regards admiratifs.")
            print("Les invités t'entourent et t'invitent à danser.")
            pts_suspicion = pts_suspicion + 1
            est_entre = True
            de_danse = random.randint(1, 6)
            print("Tu as obtenu", de_danse, "au dé pour la danse (il faut 4 ou plus).")
            if de_danse >= 4:
                pts_suspicion = pts_suspicion - 1
                print("Tu séduis la salle, bravo !")
            else:
                pts_suspicion = pts_suspicion + 2
                print("Tu t'emmêles les pieds...")
            print("Tu as", pts_suspicion, "point(s) de suspicion.")

# ---------- ARRIVÉE DANS LE HALL ----------
print()
print("=== Tu es dans le hall d'entrée. ===")
print("Un grand escalier monte vers l’étage, un couloir part vers la bibliothèque, et un domestique passe avec un plateau.")

while dans_le_haul:
    print()
    print("--- Le hall ---")
    print("1. Aller à la bibliothèque")
    print("2. Suivre le domestique jusqu'à la cuisine")
    print("3. Monter au bureau de la comtesse")
    choix_haul = input("Où veux-tu aller ? ")

    # ----- LA BIBLIOTHÈQUE -----
    if choix_haul == "1":
        print()
        print("--- La bibliothèque ---")
        print("Des milliers de livres tapissent les murs. Sur une table, un vieux carnet est ouvert, écrit en tout petit.")
        print("Tu entends des pas dans le couloir : un garde fait sa ronde.")
        tours = 0
        dans_la_bibliotheque = True

        while dans_la_bibliotheque:
            print()
            print("1. Lire le carnet")
            print("2. Fouiller les étagères")
            print("3. Retourner au hall")
            choix_haul_1 = input("Que choisis-tu ? ")

            if choix_haul_1 == "1":
                if indice_lu:
                    print("Tu as déjà lu le carnet. Tu connais le secret, inutile d’y revenir.")
                elif "loupe" in inventaire:
                    print("Tu te penches sur le carnet. L’écriture est minuscule, mais grâce à ta loupe, tu déchiffres une phrase dans la marge :")
                    print("« Le code du coffre est un mot chiffré. Pour le lire, décale chaque lettre de 3 rangs dans l’alphabet. »")
                    indice_lu = True
                    tours = tours + 1
                else:
                    print("Tu te penches sur le carnet, mais l’écriture est bien trop petite.")
                    print("Tu perds de précieuses minutes à plisser les yeux, sans rien comprendre, il te faudrait une loupe...")
                    tours = tours + 2

            elif choix_haul_1 == "2":
                print("Tu parcours les étagères du bout des doigts. Entre deux reliures, tu trouves un vieux roman d’aventures de Maurice Leblanc. Rien d’utile, mais il t’a fait sourire.")
                tours = tours + 1

            elif choix_haul_1 == "3":
                print("Tu quittes la bibliothèque.")
                dans_la_bibliotheque = False

            else:
                print("Je n'ai pas compris.")

            # Le garde arrive quand le compteur de tours atteint 3
            if dans_la_bibliotheque and tours >= 3:
                if "perruque" in inventaire:
                    print("Un garde entre, te dévisage, puis te prend pour un domestique et repart.")
                else:
                    print("Un garde entre et te surprend près du carnet !")
                    pts_suspicion = pts_suspicion + 3
                print("Tu es donc de retour dans le hall.")
                dans_la_bibliotheque = False
                print("Tu as", pts_suspicion, "point(s) de suspicion.")

    # ----- LA CUISINE -----
    elif choix_haul == "2":
        print()
        print("--- La cuisine ---")
        print("Tu suis le domestique jusqu’à la cuisine. Le cuisinier prépare le dîner et te prend pour un livreur.")
        print("Une clé est accrochée au mur, près de la porte.")
        dans_la_cuisine = True

        while dans_la_cuisine:
            print()
            print("1. Parler au cuisinier")
            print("2. Voler la clé")
            print("3. Retourner au hall")
            choix_cuisine = input("Que choisis-tu ? ")

            if choix_cuisine == "1":
                if a_parler_cuisinier == True:
                    print("Le cuisinier est parti à la cave chercher du vin.")
                else:
                    print("« La comtesse cache ses secrets derrière un tableau, dans son bureau. Et elle écrit toujours ses codes avec un petit décalage... »")
                    print("« Bon, je descends à la cave chercher du vin, ne touche à rien ! »")
                    a_parler_cuisinier = True

            elif choix_cuisine == "2":
                if "clé" in inventaire:
                    print("Tu as déjà la clé !")
                elif a_parler_cuisinier == True:
                    inventaire.append("clé")
                    print("Tu récupères la clé sans être vu par le cuisinier, bravo !")
                else:
                    inventaire.append("clé")
                    pts_suspicion = pts_suspicion + 2
                    print("Le cuisinier te surprend en train de voler la clé... mais tu as le temps de partir avec !")
                print("Tu as", pts_suspicion, "point(s) de suspicion.")

            elif choix_cuisine == "3":
                print("Tu retournes dans le hall.")
                dans_la_cuisine = False

            else:
                print("Je n'ai pas compris.")

    # ----- LA PORTE DU BUREAU -----
    elif choix_haul == "3":
        if "clé" in inventaire or "crochet" in inventaire:
            print("Tu montes l'escalier jusqu'au bureau de la comtesse. La porte s'ouvre sans bruit.")
            dans_le_haul = False
        else:
            print("La porte du bureau est verrouillée. Il te faudrait une clé ou un crochet...")

    else:
        print("Je n'ai pas compris.")

# ---------- LE BUREAU ET LE COFFRE ----------
print()
print("=== Le bureau de la comtesse ===")
print("Derrière un tableau, tu découvres un gros coffre-fort. Un mot chiffré est gravé dessus :")
print("OXSLQ")

essais = 3
if indice_lu:
    essais = 4
    print("Grâce au carnet, tu sais qu'il faut décaler chaque lettre de 3 rangs en arrière.")
else:
    print("Tu ne sais pas comment lire ce code... Il te faudrait un indice.")
print("Tu as", essais, "essais.")

coffre_ouvert = False
while coffre_ouvert == False and essais > 0:
    mot = input("Quel est le mot de passe ? ").upper()
    if mot == "LUPIN":
        coffre_ouvert = True
    else:
        essais = essais - 1
        pts_suspicion = pts_suspicion + 1
        print("Le coffre reste fermé. Il te reste", essais, "essai(s).")

if coffre_ouvert:
    print("Clic ! Le coffre s'ouvre et le collier de la comtesse brille dans ta main.")
    print("Tu laisses ta carte de visite : « Arsène Lupin, gentleman-cambrioleur. »")
else:
    print("L'alarme retentit dans tout l'hôtel !")
    pts_suspicion = pts_suspicion + 5
    print("Tu t'enfuis par le toit, sans le collier...")

# ---------- VERDICT ----------
print()
print("=== FIN DE LA PARTIE ===")
if coffre_ouvert == False:
    print("Raté : tu repars les mains vides. Ganimard sourit au loin...")
elif pts_suspicion <= 3:
    print("Parfait : personne ne se doute de rien !")
    print("Une lettre est glissée dans l'écrin : « Merci, Arsène. L'assurance me paiera très bien. » Signé : la comtesse.")
    print("Elle était complice depuis le début !")
elif pts_suspicion <= 7:
    print("Honorable : tu t'enfuis de justesse par le toit, un garde à tes trousses.")
else:
    print("Limite : tu as le collier, mais tout Paris sait que Lupin était là.")
print("Tu finis avec", pts_suspicion, "point(s) de suspicion.")

input("Appuie sur Entrée pour quitter.")