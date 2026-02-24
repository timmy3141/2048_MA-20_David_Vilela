"""
Auteur : David Vilela
Classe : SI-Ca1a
Projet : MA20 – 2048 (Sprint 1)
Date de création: 10.02.2026

Description :
Ce programme est une reconstitution graphique du jeu 2048 realisée avec Tkinter.
Il s'agit uniquement de la partie affichage : creation de la fenetre, du plateau,
des cases colorées et des scores.
"""

import tkinter as tk

root = tk.Tk()
root.title('2048')
root.resizable(False, False)
root.config(bg='#FFFFFF')

# Definition de la taille de la fenetre
window_width = 660
window_height = 850

# Obtient la taille de l'écran
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Trouve le centre de l'écran
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# Place la fenetre au centre de l'écran
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Definition des couleurs pour chaque valeur de case
tiles_colors = {
  "2": "#1B1D2F",
  "4": "#283650",
  "8": "#3C4C69",
  "16": "#687792",
  "32": "#8D99AE",
  "64": "#CFC4D0",
  "128": "#FA6D86",
  "256": "#F43B5B",
  "512": "#DF092E",
  "1024": "#C00A2A",
  "2048": "#7C0117",
  "4096": "#51010F",
  "8192": "#200006"
}
"""
game = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
"""
#Jeu en mémoire

game = [
    [2,4,8,16],
    [32,64,128,256],
    [512,1024,2048,4096],
    [8192,0,0,0]
]

current_score = 0
best_score = 0

# -----------------------------------------HEADER-----------------------------------------

# Frame pour le "header"
top_frame = tk.Frame(root, bg="#FFFFFF", height=150)
top_frame.pack(fill="x", pady=(20, 0))

# "Sous-frame" pour titre et scores
top_row = tk.Frame(top_frame, bg="#FFFFFF")
top_row.pack(fill="x", padx=20)

# "Sous-frame" pour bouton rejouer
bottom_row = tk.Frame(top_frame, bg="#FFFFFF")
bottom_row.pack(fill="x", padx=20, pady=(10,0))

# Affichage de "2048"
title_label = tk.Label(
    top_row,
    text="2048",
    font=("Helvetica", 30, "bold"),
    bg="#D9D9D9",
    fg="#333",
    width=8,
    height=2,
    bd=2,
    relief="solid"
)
title_label.pack(side="left", padx=(0, 20))

# Affichage score actuel
score_frame = tk.Frame(top_row, bg="#D9D9D9", bd=2, relief="solid")
score_frame.pack(side="right", padx=(10,0))
score_label = tk.Label(score_frame, text=f"Score\n{current_score}", font=("Helvetica", 16, "bold"), bg="#D9D9D9", fg="#333")
score_label.pack(padx=10, pady=10)

# Affichage meilleur score
bestscore_frame = tk.Frame(top_row, bg="#D9D9D9", bd=2, relief="solid")
bestscore_frame.pack(side="right", padx=(10,0))
bestscore_label = tk.Label(bestscore_frame, text=f"Best Score\n{best_score}", font=("Helvetica", 16, "bold"), bg="#D9D9D9", fg="#333")
bestscore_label.pack(padx=10, pady=10)

# Affichage bouton Rejouer
restart_button = tk.Button(
    bottom_row,
    text="Rejouer",
    font=("Helvetica", 14, "bold"),
    bg="#D9D9D9",
    fg="black",
    width=12,
    height=2,
)
restart_button.pack(side="left")


#-----------------------------------------PLATEAU-----------------------------------------

# Création du plateau
board_frame = tk.Frame(root, bg="#777676", width=600, height=600)
board_frame.pack(pady=20)

# Création des cases
tile_labels = [[None]*4 for _ in range(4)]
for i in range(4):
    for j in range(4):
        label = tk.Label(
            board_frame,
            text="",
            font=("Helvetica", 40, "bold"),
            width=4, height=2,
            bg="#777676",
            fg="#FFFFFF",
            bd=4,
            relief="raised"
        )
        label.grid(row=i, column=j, padx=10, pady=10)
        tile_labels[i][j] = label

# Mise à joue de l'affichage des cases
def display():
    for i in range(4):
        for j in range(4):
            val = game[i][j]
            if val == 0:
                tile_labels[i][j].config(text="", bg="#FFFFFF")
            else:
                tile_labels[i][j].config(text=str(val), bg=tiles_colors[str(val)])


display()
root.mainloop()
