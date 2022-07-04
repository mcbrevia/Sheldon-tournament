ROCK = 'ROCK'
PAPER = 'PAPER'
SCISSORS = 'SCISSORS'
LIZARD = 'LIZARD'
SPOCK = 'SPOCK'

def init_ap():
    """
    Summary:
        Fonction d'initialisation
    Args:
        None
    Returns:
        - round (string) : nom du fichier listant les combats du 1er tour
        - players (sring) : nom du fichier listant la liste des coups par joueur et par tour
        - matchs (string) : nom du fichier listant le détail de tous les matches joués
        - vainqueur (string) : nom du fichier contenant le vainqueur du tournoi
        - duels (dictionnaire) : matrice des combats
    """
    # Nom des fichiers à importer
    round = "round_0.csv"
    players = "players_infos.csv"

    # Noms des fichiers à générer
    matchs = "matches.csv"
    vainqueur = "result.txt"

    # Matrice des duels
    duels = {
        ROCK + SCISSORS : ROCK,
        ROCK + LIZARD : ROCK,
        PAPER + ROCK : PAPER,
        PAPER + SPOCK : PAPER,
        SCISSORS + PAPER : SCISSORS,
        SCISSORS + LIZARD : SCISSORS,
        LIZARD + PAPER : LIZARD,
        LIZARD + SPOCK : LIZARD,
        SPOCK + ROCK : SPOCK,
        SPOCK + SCISSORS : SPOCK,
    }

    return round, players, matchs, vainqueur, duels