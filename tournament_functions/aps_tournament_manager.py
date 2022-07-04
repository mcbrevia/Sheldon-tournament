from datetime import datetime
import shutil
import os
import tkinter as tk

#importations des modules contenant les fonctions externalisées
from tournament_functions.aps_list_and_dictionnary import *
from tournament_functions.aps_files_manager import *
from tournament_functions.aps_initialisation import *


#def tournoi(num_tournoi, zone_affichage):
def tournoi(num_tournoi, zone_affichage, fichier_players, fichier_round, fichier_matchs, fichier_vainqueur, resultat_duels):
    """
    Summary:
        Fonction déclenchée suite à la sélection d'un tournoi par l'utilisateur. Elle permet de :
        - déplacer les fichiers round_0.csv et players_infos.csv du tournoi dans le répertoire courant
        - lancer le tournoi sélectionné
        - afficher le vainqueur
        - archiver les fichiers resultats du tournoi une fois terminé
            => format : <Nom du fichier>_<Numéro du tournoi>_<Horodatage>
    Args:
        num_tournoi (int): numéro du tournoi à lancer
        zone_affichage (entry): élément de la fenêtre servant à afficher le résultat du tournoi
        fichier_round: Fichier des matchs à jouer
        fichier_players: Fichier des joueurs inscrits au tournois
        fichier_matchs: Fichier d'archive des matchs
        fichier_vainqueur: Fichier avec le nom du vainqueur du tournois
        resultat_duels: liste des résultats des duels
    Returns:
        None
    """
    # Suppression de tout texte éventuel dans la zone d'affichage
    zone_affichage.delete(0,tk.END)
    # Déplacement des fichiers du tournoi sélectionné dans le répertoire courant
    path='tournament_'+str(num_tournoi)+'/'
    shutil.copyfile(path + fichier_round, fichier_round)
    shutil.copyfile(path + fichier_players, fichier_players)
    # Lancement du tournoi
    winner = deroulement_tournoi(fichier_round, fichier_players, fichier_matchs, fichier_vainqueur, resultat_duels)
    # Affichage du résultat à l'écran
    zone_affichage.insert(0,f'*** Le vainqueur du tournoi {num_tournoi} est : {winner} ***')
    # Archivage des fichiers résultats
    archive_result = 'archives/' + fichier_vainqueur.split('.')[0] + '_' + str(num_tournoi) + '_' + datetime.now().strftime('%Y%m%d%H%M%S') + '.' + fichier_vainqueur.split('.')[1]
    archive_matches = 'archives/' + fichier_matchs.split('.')[0] + '_' + str(num_tournoi) + '_' + datetime.now().strftime('%Y%m%d%H%M%S') + '.' + fichier_matchs.split('.')[1]
    shutil.copyfile(fichier_vainqueur, archive_result)
    shutil.copyfile(fichier_matchs, archive_matches)
    # Suppression des fichiers temporaires
    os.remove(fichier_round)
    os.remove(fichier_players)
    os.remove(fichier_vainqueur)
    os.remove(fichier_matchs)


def deroulement_tournoi(fichier_round, fichier_players, fichier_matchs, fichier_vainqueur, resultat_duels):
    """
    Summary:
        Fonction permettant de dérouler tout un tournoi en supprimant au fur et à mesure de chaque tour les perdants de chaque duel
    Args:
        fichier_round: Fichier des matchs à jouer
        fichier_players: Fichier des joueurs inscrits au tournois
        fichier_matchs: Fichier d'archive des matchs
        fichier_vainqueur: Fichier avec le nom du vainqueur du tournois
        resultat_duels: liste des résultats des duels
    Returns:
        vainqueur (string) : Nom du gagnant du tournoi
    """
    # Début du tournoi : on élimine les perdants de chaque tour jusqu'à ce qu'il ne reste plus qu'un seul concurrent
    table_round = lecture_fichier(fichier_round)
    table_players = lecture_fichier(fichier_players)
    player_and_choice_list = creation_dictionnaire_joueurs_et_coups(table_players)
    table_round, player_and_choice_dict, liste_joueurs = anonymisation_joueur(table_round, player_and_choice_list)
    archive_matchs = []
    round_en_cours = 0
    while True:
        vainqueurs =[]
        win=[]
        # Détermination des vainqueurs à chaque match (duel) du tour
        print(f'Matches du round {round_en_cours}: {table_round}')
        for concurrent in table_round:
            win = deroulement_combat(resultat_duels, concurrent[0].capitalize() \
                                     , player_and_choice_dict[concurrent[0]][round_en_cours].upper() \
                                     , concurrent[1].capitalize() \
                                     , player_and_choice_dict[concurrent[1]][round_en_cours].upper())
            winner, joueur1, joueur2 = replace_player_id(liste_joueurs, win, concurrent[0], concurrent[1])
            vainqueurs.append(win)
            archive_matchs.append([round_en_cours, winner, joueur1, player_and_choice_dict[concurrent[0]][round_en_cours], joueur2, player_and_choice_dict[concurrent[1]][round_en_cours]])
        print(f'Vainqueurs des duels du round {round_en_cours}: ', vainqueurs)
        if len(vainqueurs) == 1: # => le tournoi est terminé quand il n'y a plus qu'un seul joueur
            break
        # Mise en place du tour suivant : regroupement des vainqueurs 2 par 2 pour initier le tour suivant
        table_round= list(zip(*[iter(vainqueurs)] * 2))
        round_en_cours += 1

    # Archivage du déroulé du tournoi
    entete=['Round','Winner','Player 1 name','Player 1 sign','Player 2 name','Player 2 sign']
    ecriture_fichier(fichier_matchs, archive_matchs, entete, "csv", "w+")
    vainqueur_tournois = replace_player_id(liste_joueurs, vainqueurs[0])
    nom_vainqueur = str(f"TOURNAMENT WINNER : {vainqueur_tournois}")
    ecriture_fichier(fichier_vainqueur, nom_vainqueur)

    print(f"ENDEUX ZZZZE OUINNEUR IZZZZZZZ : {vainqueur_tournois}")

    return vainqueur_tournois

def deroulement_combat (resultat_duels, joueur1, attaque_j1, joueur2=None, attaque_j2=None):
    """
    Summary:
        Fonction déterminant le gagnant d'un combat en fonction de la matrice des duels
        => Cas particuliers :
            - si la matrice des duels ne peut pas départager les concurrents (match nul), le vainqueur est déterminé par ordre alphabétique des noms fournis
            - s'il n'y a qu'un seul concurrent fourni à la fonction, il est déclaré vainqueur par défaut
            - si une attaque d'un joueur n'est pas reconnue (en dehors de la liste prévue dans la matrice), l'autre joueur est déclaré vainqueur
            - si les deux attaques des deux concurrents sont inconnues, il y a égalité et le vainqueur se fera par ordre alphabétique sur le nom
    Args:
        resultat_duels: liste des résultats des duels
        joueur1 (string): nom du premier joueur
        attaque_j1 (string): attaque du premier joueur (ROCK, PAPER, SCISSORS, LIZARD ou SPOCK)
        joueur2 (string, optional): nom du second joueur. Argument facultatif positionné à None par défaut.
        attaque_j2 (string, optional): attaque du second joueur (ROCK, PAPER, SCISSORS, LIZARD ou SPOCK). Argument facultatif positionné à None par défaut.
    Returns:
        string: nom du joueur gagnant
    """
    #Traitement des cas particuliers
    if attaque_j2==None or joueur2 == None:
        return joueur1
    elif not attaque_j1 in (ROCK, PAPER, SCISSORS, LIZARD, SPOCK) and not attaque_j2 in (ROCK, PAPER, SCISSORS, LIZARD, SPOCK):
        return sorted((joueur1,joueur2))[0]
    elif not attaque_j1 in (ROCK, PAPER, SCISSORS, LIZARD, SPOCK):
        return joueur2
    elif not attaque_j2 in (ROCK, PAPER, SCISSORS, LIZARD, SPOCK):
        return joueur1
    elif attaque_j1 == attaque_j2:
        return sorted((joueur1,joueur2))[0]

    #Les cas articuliers étant écartés, recherche de l'attaque gagnante dans la matrice des duels
    if resultat_duels.get(attaque_j1 + attaque_j2, attaque_j2) == attaque_j2:
        return joueur2

    return joueur1
