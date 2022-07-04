import tkinter as tk

#importations des modules contenant les fonctions externalisées
from tournament_functions.aps_tournament_manager import tournoi


def init_window(fichier_round, fichier_players, fichier_matchs, fichier_vainqueur, resultat_duels) :
    """
    Summary:
        Fonction permettant la création et l'initialisation de l'écran de l'application et des paramètres globaux liés à la gestion de cette fenêtre
    Args:
        fichier_round: Fichier des matchs à jouer
        fichier_players: Fichier des joueurs inscrits au tournois
        fichier_matchs: Fichier d'archive des matchs
        fichier_vainqueur: Fichier avec le nom du vainqueur du tournois
        resultat_duels: liste des résultats des duels
    Returns:
        window : écran créé
    """
    # Création d'une fenêtre
    window=tk.Tk()
    window.title("Sheldon Tournament")
    window.geometry("1080x720")
    window.minsize(700,700)
    window.iconbitmap("img/bigBangTheory.ico")
    window.config(background="#15133d")

    frame = tk.Frame(window,bg="#15133d")
    # Affichage des entête
    label_title = tk.Label(frame, text= "Pierre, Papier, Ciseaux, Lézard, Spock", font=("Arial",30),bg="#15133d",fg="white")
    label_title.pack()
    label_subtitle = tk.Label(frame, text= "Big Bang Theory", font=("Arial",25),bg="#15133d",fg="white")
    label_subtitle.pack()

    frame_2 = tk.Frame(frame,bg="#15133d")
    # Définition de la partie gauche de la fenêtre : image
    width = 400
    height = 400
    image = tk.PhotoImage(file="img/rpsls.png").zoom(35).subsample(32)
    canvas = tk.Canvas(frame_2, width=width,height=height,bg="#15133d",bd=0,highlightthickness=0)
    canvas.create_image(width/2,height/2,image=image)
    canvas.grid(row=2,column=0,sticky=tk.W)
    # Définition de la partie centrale de la fenêtre : sélection du tournois à lancer
    right_frame = tk.Frame(frame_2,bg="#15133d")
    label_description = tk.Label(right_frame, text= "Sélectionnez le tournoi à lancer :", font=("Arial",15),bg="#15133d",fg="white")
    label_description.pack()
    tournoi1_button = tk.Button(right_frame, text= "Tournoi 1", font=("Arial",15),bg="white",fg="#15133d", command=lambda: tournoi(1,affichage_vainqueur, fichier_players, fichier_round, fichier_matchs, fichier_vainqueur, resultat_duels))
    tournoi1_button.pack(pady=5, fill=tk.X)
    tournoi2_button = tk.Button(right_frame, text= "Tournoi 2", font=("Arial",15),bg="white",fg="#15133d", command=lambda: tournoi(2,affichage_vainqueur, fichier_players, fichier_round, fichier_matchs, fichier_vainqueur, resultat_duels))
    tournoi2_button.pack(pady=5, fill=tk.X)
    tournoi3_button = tk.Button(right_frame, text= "Tournoi 3", font=("Arial",15),bg="white",fg="#15133d", command=lambda: tournoi(3,affichage_vainqueur, fichier_players, fichier_round, fichier_matchs, fichier_vainqueur, resultat_duels))
    tournoi3_button.pack(pady=5, fill=tk.X)
    right_frame.grid(row=2,column=1,sticky=tk.W)
    frame_2.pack(expand=tk.YES)

    affichage_vainqueur = tk.Entry(frame, font=('Arial', 15),bg="#15133d",fg="white", justify='center')
    affichage_vainqueur.pack(pady=5, fill=tk.X)

    # Sortie du programme
    exit_button = tk.Button(frame, text= "Quitter", font=("Arial",15),bg="white",fg="#15133d",command=window.destroy)
    exit_button.pack(fill=tk.X)

    frame.pack(expand=tk.YES)

    window.mainloop()
