#importations des modules contenant les fonctions externalisées
from tournament_functions.aps_initialisation import init_ap
from tournament_functions.aps_windows_manager import init_window

# Initialisation des données de référence
fichier_round, fichier_players, fichier_matchs, fichier_vainqueur, resultat_duels = init_ap()

# Afficher la fenêtre
init_window(fichier_round, fichier_players, fichier_matchs, fichier_vainqueur, resultat_duels)
