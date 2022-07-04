def creation_dictionnaire_joueurs_et_coups(table_players):
    """
    Summary:
        Fonction qui concatène les joueurs avec tous ses coups
    Args:
        table_players (list): _description_
    Returns:
        dictionnaire: _description_
    """
    player_and_choice_list= []
    i = 0
    while i < len(table_players):
        joueur = table_players[i][0]
        coup = table_players[i][2]
        table_coups = []
        table_coups.append(coup)
        i+=1
        while True and i < len(table_players):
            round = table_players[i][1]
            if round !="0":
                table_coups.append(table_players[i][2])
                i+=1
            else:
                break
        #player_and_choice_list[joueur]= table_coups[:]
        player_and_choice_list.append([joueur, table_coups])
    return player_and_choice_list



def creation_liste_joueurs(table_round):
    """
    Cette fonction va créer une liste avec le nom de chaque joueur
    :param table_round: Tableau contenant la liste des matchs du premier tour
    :return: listeJoueursIntemediaire: Liste avec le nom de chaque joueur
    """
    i = 0
    liste_joueurs_intemediaire = []
    while i < len(table_round):
        liste_joueurs_intemediaire.append(table_round[i][0])
        liste_joueurs_intemediaire.append(table_round[i][1])
        i+=1
    return liste_joueurs_intemediaire


def creation_dictionnaire_joueurs(liste_joueurs_intemediaire):
    """
    Création d'un dictionnaire où:
    - la clé sera 'Joueur + n°' (n° = occurence en fonction de la liste envoyée en paramètre)
    - la valeur sera le nom du joueur
    :param liste_joueurs_intemediaire: liste triée alphabétiquement contenant le nom de chaque joueur
    :return: listeJoueurs: dictionnaire contenant l'identifiant de chaque joueur
    """
    liste_joueurs = {}
    i = 0
    while i < len(liste_joueurs_intemediaire):
        liste_joueurs['Joueur' + str(i + 1).zfill(4)]= liste_joueurs_intemediaire[i]
        i+=1
    return liste_joueurs


def remplacement_nom_joueurs(table_round, player_and_choice_list, liste_joueurs):
    """
    Fonction qui va remplacer le nom des joueurs par leur identifiant
    :param table_round: liste des matchs du premier tour
    :param player_and_choice_list: liste des joueurs + leurs coups
    :param liste_joueurs: Dictionnaire avec l'identifiant (clé) et le nom (valeur) des joueurs
    :return:
        tabRound: liste des matchs du premier tour (où le nom des joueurs a été remplacé par leur identifiant)
        joueur_et_coups_dict : dictionnaire reprennant les données de 'player_and_choice_list' (clé = identifiant du joueur, valeur = tableau des coups)
    """
    joueur_et_coups_dict = {}
    for cle_joueur, valeur_joueur in liste_joueurs.items():
        print(cle_joueur, valeur_joueur)

        for x in range(len(player_and_choice_list)):
            if valeur_joueur == player_and_choice_list[x][0]:
                joueur_et_coups_dict[str(cle_joueur)]=player_and_choice_list[x][1]
                player_and_choice_list[x][0] = str(cle_joueur)
                break

        for i in range(len(table_round)):
            if valeur_joueur == table_round[i][0]:
                table_round[i][0] = str(cle_joueur)
                break
            elif(valeur_joueur == table_round[i][1]):
                table_round[i][1] = str(cle_joueur)
                break

    return table_round, joueur_et_coups_dict


def anonymisation_joueur(table_round, player_and_choice_list):
    """
    Fonction permettant de remplacer le nom des joueurs par un identifiant 'Joueur+n°joueur' afin de gérer les doublons dans les noms
    :param table_round: Tableau contenant la liste des matchs du premier tour
    :param player_and_choice_list: Liste contenant le nom de chaque joueur + la liste de ses coups
    :return:
        tabround: tableau des matchs du premier tour où le nom du joueur a été remplacé par son identifiant
        tabPlayerAndChoice: tableau joueurs (où le nom de ce dernier a été remplacé par son identifiant) + liste de ses coups
    """
    liste_joueurs_intemediaire=sorted(creation_liste_joueurs(table_round))
    liste_joueurs=creation_dictionnaire_joueurs(liste_joueurs_intemediaire)
    table_round, player_and_choice_list = remplacement_nom_joueurs(table_round, player_and_choice_list, liste_joueurs)
    return table_round, player_and_choice_list, liste_joueurs


def replace_player_id(liste_joueurs, winner_id, player1_id=None, player2_id=None):
    """
    Fonction qui permet de remplacer l'identifiant des joueurs par leur nom
    :param liste_joueurs: Dictionnaire contenant l'identifiant (clé) et le nom (valeur) des joueurs
    :param winner_id: Identifiant du vainqueur
    :param player1_id: Identifiant du premier dueliste (optionnel)
    :param player2_id: Identifiant du second dueliste (optionnel)
    :return:
        winnerId = nom du vainqueur
        player1Id = nom du premier dueliste (si identifiant passé en paramètre)
        player2Id = nom du second dueliste (si identifiant passé en paramètre)
    """
    winner_id = liste_joueurs[str(winner_id)]
    if player1_id != None and player2_id!=None:
        player1_id = liste_joueurs[str(player1_id)]
        player2_id = liste_joueurs[str(player2_id)]
        return winner_id, player1_id, player2_id

    return winner_id
