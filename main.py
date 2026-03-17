"""
Auteur : David Vilela
Classe : SI-Ca1a
Projet : MA20 – 2048
Date de création: 10.02.2026

Description :
Ce programme est une reconstitution du jeu 2048 realisée avec Tkinter.

Source pour fenetre centrée: https://www.pythontutorial.net/tkinter/tkinter-window/
"""

import tkinter as tk
import copy
import random

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
  2: "#1B1D2F",
  4: "#283650",
  8: "#3C4C69",
  16: "#687792",
  32: "#8D99AE",
  64: "#CFC4D0",
  128: "#FA6D86",
  256: "#F43B5B",
  512: "#DF092E",
  1024: "#C00A2A",
  2048: "#7C0117",
  4096: "#51010F",
  8192: "#200006"
}

game = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

# copie du jeu pour bouton reset
game_very_old = copy.deepcopy(game)

current_score = 0
best_score = 0
old_best_score = 0
first_game = True
first_move = True
won = False
lose = False

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

#Affichage bouton Retour et Fonction retour
def back_game():
    global first_move
    global game
    global current_score
    global best_score
    if first_move == True:
        return
    else:
        game = copy.deepcopy(game_old)
        current_score = old_score
        best_score = old_best_score
        print("Retour")
        display()

back_button = tk.Button(
    bottom_row,
    text="<",
    font=("Helvetica", 14, "bold"),
    bg="#D9D9D9",
    fg="black",
    width=3,
    height=2,
    command=back_game
)
back_button.pack(side="left")

# Fonction Reset du jeu
def reset_game():
    global first_game
    global game
    global game_old
    global current_score
    global first_move
    global win
    win = False
    first_move = True
    game = copy.deepcopy(game_very_old)
    game_old = copy.deepcopy(game)
    current_score = 0
    if first_game == True:
        restart_button.config(text="Rejouer")
        first_game = False
    spawn_tile()
    spawn_tile()
    display()

# Affichage bouton reset
restart_button = tk.Button(
    bottom_row,
    text="Jouer",
    font=("Helvetica", 14, "bold"),
    bg="#D9D9D9",
    fg="black",
    width=11,
    height=2,
    command=reset_game
)
restart_button.pack(side="left", padx=8)


# -----------------------------------------PLATEAU-----------------------------------------

# Création du plateau
board_frame = tk.Frame(root, bg="#777676", width=600, height=600)
board_frame.pack(pady=20)

# Création des cases
tile_labels = []
for row in range(4):
    current_row = []
    for col in range(4):
        label = tk.Label(
            board_frame,
            text="",
            font=("Helvetica", 40, "bold"),
            width=4,
            height=2,
            bg="#777676",
            fg="#FFFFFF",
            bd=4,
            relief="raised"
        )
        label.grid(row=row, column=col, padx=10, pady=10)
        current_row.append(label)
    tile_labels.append(current_row)


# -----------------------------------------LOGIQUE DU JEU-----------------------------------------

# Mise à joue de l'affichage des cases
def display():
    for i in range(4):
        for j in range(4):
            val = game[i][j]
            if val == 0:
                tile_labels[i][j].config(text="", bg="#FFFFFF")
            else:
                tile_labels[i][j].config(text=str(val), bg=tiles_colors[val])
    # Actualisation des scores
    score_label.config(text=f"Score\n{current_score}")
    bestscore_label.config(text=f"Best Score\n{best_score}")

def win_message():
    print("Vous avez gagné !")

def lose():
    print("Vous avez perdu !")

def check_win():
    global won
    if not won:
        for row in game:
            if 2048 in row:
                won = True
                win_message()
                break

def check_lose():
    global lose

# Sauvegarde de l'etat du jeu
def save_state():
    global game_old
    global old_score
    global old_best_score
    global first_move
    first_move = False
    game_old = copy.deepcopy(game)
    old_score = current_score
    old_best_score = best_score

# Fonction qui fait apparaitre une "tile" random dans une case vide
def spawn_tile():
    # Trouver les cases vides
    empty_tiles = []
    for i in range(4):
        for j in range(4):
            if game[i][j] == 0:
                empty_tiles.append((i, j))
    if not empty_tiles:
        return
    # Choisir une case aléatoire
    i, j = random.choice(empty_tiles)
    # Choisir la valeur (80% 2, 20% 4)
    if random.randint(1,10) <= 8:
        game[i][j] = 2
    else:
        game[i][j] = 4


# Capture des inputs clavier
def key_input(event):
    key = event.keysym
    if key == "w" or key == "W" or key == "Up":
        up()
    if key == "a" or key == "A" or key == "Left":
        left()
    if key == "s" or key == "S" or key == "Down":
        down()
    if key == "d" or key == "D" or key == "Right":
        right()
root.bind("<KeyPress>", key_input)
root.focus_set()

# Ecrasement des cases lors de key_input
def pack4(a,b,c,d):
    global current_score
    global best_score
    # Déplacer les zéros vers la gauche
    if c == 0:
        c,d = d,0
    if b == 0:
        b,c,d = c,d,0
    if a == 0:
        a,b,c,d = b,c,d,0
    # Fusionner les cases et actualisation du score
    if a == b and a != 0:
        current_score += a * 2
        a,b,c,d = a*2, c, d, 0
    if b == c and b != 0:
        current_score += b * 2
        b,c,d = b*2, d, 0
    if c == d and c != 0:
        current_score += c * 2
        c,d = c*2, 0

    # Actualisation du meilleur score
    if current_score > best_score:
        best_score = current_score

    return (a,b,c,d)

# Ecrasement des cases selon direction
def right():
    save_state() # Sauvegarde l'état actuel du plateau et du score
    for i in range(4):
        # Pour chaque ligne i, on déplace et fusionne les tuiles vers la droite
        (game[i][3], game[i][2], game[i][1], game[i][0]) = pack4(game[i][3], game[i][2], game[i][1], game[i][0])
    if game_old == game:
        # Si aucune tuile ne bouge
        print("Le jeu n'a pas changé")
    if game_old != game:
        # Si le plateau a changé, ajouter une nouvelle tuile et vérifier la victoire
        spawn_tile()
        check_win()
    display()

def left():
    save_state() # Sauvegarde l'état actuel du plateau et du score
    for i in range(4):
        # Pour chaque ligne i, on déplace et fusionne les tuiles vers la gauche
        (game[i][0], game[i][1], game[i][2], game[i][3]) = pack4(game[i][0], game[i][1], game[i][2], game[i][3])
    if game_old == game:
        # Si aucune tuile ne bouge
        print("Le jeu n'a pas changé")
    if game_old != game:
        # Si le plateau a changé, ajouter une nouvelle tuile et vérifier la victoire
        spawn_tile()
        check_win()
    display()

def up():
    save_state() # Sauvegarde l'état actuel du plateau et du score
    for j in range(4):
        # Pour chaque ligne i, on déplace et fusionne les tuiles vers le haut
        (game[0][j], game[1][j], game[2][j], game[3][j]) = pack4(game[0][j], game[1][j], game[2][j], game[3][j])
    if game_old == game:
        # Si aucune tuile ne bouge
        print("Le jeu n'a pas changé")
    if game_old != game:
        # Si le plateau a changé, ajouter une nouvelle tuile et vérifier la victoire
        spawn_tile()
        check_win()
    display()

def down():
    save_state() # Sauvegarde l'état actuel du plateau et du score
    for j in range(4):
        # Pour chaque ligne i, on déplace et fusionne les tuiles vers le bas
        (game[3][j], game[2][j], game[1][j], game[0][j]) = pack4(game[3][j], game[2][j], game[1][j], game[0][j])
    if game_old == game:
        # Si aucune tuile ne bouge
        print("Le jeu n'a pas changé")
    if game_old != game:
        # Si le plateau a changé, ajouter une nouvelle tuile et vérifier la victoire
        spawn_tile()
        check_win()
    display()

display()
root.mainloop()
