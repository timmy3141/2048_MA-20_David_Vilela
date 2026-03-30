#2048 – Projet MA20

## Informations générales
* **Auteur** : David Vilela
* **Classe** : SI-Ca1a
* **Projet** : MA20 – Reconstruction du jeu 2048
* **Date de création** : 10.02.2026

---

## Description du projet

Ce projet est une reconstitution du célèbre jeu **2048**, réalisée en Python avec la bibliothèque **Tkinter**.
Le joueur doit déplacer les tuiles à l’aide du clavier pour les fusionner et atteindre la valeur **2048**.

---

## Objectif du jeu

* Fusionner les tuiles de même valeur
* Augmenter son score
* Atteindre la tuile **2048** pour gagner

Le jeu se termine lorsque :

* le joueur gagne (2048 atteint)
* ou qu’aucun mouvement n’est possible

---

## Contrôles

Le jeu se joue avec le clavier :

* Flèche haut / **W** → déplacer vers le haut
* Flèche bas / **S** → déplacer vers le bas
* Flèche gauche / **A** → déplacer vers la gauche
* Flèche droite / **D** → déplacer vers la droite

---

## Fonctionnalités

* Interface graphique avec Tkinter
* Génération aléatoire des tuiles (2 ou 4)
* Système de score et meilleur score
* Détection de victoire et défaite avec popups
* Bouton **Nouvelle Partie**
* Bouton **Retour** (undo du dernier coup ou plus selon implémentation)
* Historique des coups (avec `history`)

---

## Logique du jeu

* Les tuiles sont stockées dans un tableau 4x4
* Les déplacements utilisent une fonction de “tassement” (`pack4`)
* Les fusions augmentent le score
* L’état du jeu est sauvegardé à chaque coup pour permettre le retour en arrière

---

## Installation et exécution

### Prérequis

* Python 3.x installé

---

## Sources

* Centrage de fenêtre Tkinter :
  https://www.pythontutorial.net/tkinter/tkinter-window/

* Popups Tkinter :
  https://docs.python.org/3/library/tkinter.messagebox.html

* Aide complémentaire : ChatGPT

---

## Améliorations possibles

* Ajouter des animations
* Améliorer le design graphique
* Ajouter un système de sauvegarde du score
* Implémenter un système redo (avancer après undo)

---

 **Projet réalisé dans le cadre du cours MA20**
