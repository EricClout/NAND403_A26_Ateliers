"""Satisfait de votre dernier outil, le modélisateur vous fait maintenant confiance.
Il s'appelle Jason et vous annonce qu'il est le maire de la ville. Rassuré de s'être fait un ami, 
il se confie un peu à vous. Certains bandits menacent de piller la ville. Pour se protéger, et c'est 
pour cette raison qu'il veut redessiner la ville en commençant par l'ajout de défense. Il vous demande 
encore de l'aide pour construire des clôtures. Étant un tech artist, votre réflexe est, bien sûr, de faire 
un script dans Maya pour accélérer le processus."""


import random
from unicodedata import name
from maya import cmds
import maya.cmds as cmds

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QPushButton,
    QSpinBox,
    QDoubleSpinBox,
    QSlider             # Utilisé pour création de slider bar
    )


# ------------------------------------------------------------------------------------------
# Classe personnalisée pour gérer la création procédurale de clôtures dans Maya
class FenceGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 6 - Clôtures pour Jason")
        self.create_ui()

        # Définir la taille de la fenêtre et fixer ses limites
        self.resize(400, 300)
        self.setMinimumSize(400, 250)

        #                       --------------------

        # Création de l'interface utilisateur
    def create_ui(self):
        # Layout principal vertical
        layout = QVBoxLayout(self)

        # Crée (Layout horizontal) pour les sliders
        numb_layout = QHBoxLayout()
        numb_label = QLabel("Nombre de poteaux ?")

        # ----------- (QSlider) !!! C'est nouveau ça !!! ----------- #
        # Création du slider horizontale
        self.numb_slider = QSlider(Qt.Orientation.Horizontal)
        self.numb_slider.setRange(2, 50)                                       # Limites Min (2) et Max (50)
        self.numb_slider.setValue(10)                                          # Valeur par défaut (10)

        # Label dynamique qui affiche la valeur em cours du slider
        self.numb_value_label = QLabel("10")

        # ** Connexion du signal : quand la valeur du slider change, on met à jour le texte du QLabel
        # ** (Voir méthode update_numb_label plus bas)
        self.numb_slider.valueChanged.connect(self.update_numb_label)

        # Crée la ligne du slider au layout horizontal
        numb_layout.addWidget(numb_label)
        numb_layout.addWidget(self.numb_slider)
        numb_layout.addWidget(self.numb_value_label)
        layout.addLayout(numb_layout)                   # Ceci ajoute les 3 lignes ci-dessus au layout vertical principal

        # ----------- (QDoubleSpinBox) ESPACE entre les POTEAUX ----------- #
        # Crée (Layout horizontal) pour les sliders
        spacing_layout = QHBoxLayout()
        spacing_label = QLabel("Espace entre les poteaux ?")                    # Titre Rangées #1 à gauche        
        self.spacing_spin = QDoubleSpinBox()                                    # Crée la case éditable
        self.spacing_spin.setRange(0.5, 10.0)                                   # Range Min & Max
        self.spacing_spin.setValue(2.0)                                         # Valeur par défaut

        # Crée la ligne du slider au layout horizontal
        spacing_layout.addWidget(spacing_label)
        spacing_layout.addWidget(self.spacing_spin)        
        layout.addLayout(spacing_layout)                # Ceci ajoute les 2 lignes ci-dessus au layout vertical principal

        #                       --------------------

        # Création du BOUTON magique // ATTENTION : Placez le bouton APRÈS les "spinbox" pour une meilleure ergonomie
        self.button = QPushButton("Construire les défenses de la ville !")
        layout.addWidget(self.button)                                           # Ceci ajoute le bouton au layout vertical principal

        # Connexion du signal 'clicked' vers la méthode de génération
        self.button.clicked.connect(self.on_click)

    # ----------- (update_numb_label) !!! C'est nouveau ça !!! ----------- #
    # Méthode pour mettre à jour l'affichage du nombre à côté du slider
    def update_numb_label(self, value):
        self.numb_value_label.setText(str(value))

    #                       --------------------
       
    # Fonction appelée via le Bouton pour générer la clôture _ poteaux + 3 planches (Up = 6", Mid = 12", Bas = 6")
    def on_click(self):
        # Récupère le nombre de poteaux ainsi que leur espacement
        total_poteau = self.numb_slider.value()
        spacing = self.spacing_spin.value()

        # ---------- CALCULS DES DIMENSIONS & POSITIONS (en unités Maya) ---------- #
        # Longueur totale de la clôture et centre sur l'axe X
        total_length = (total_poteau - 1) * spacing
        center_x = total_length / 2.0

        # - DESCRIPTION - Hauteurs Y prédéfinies pour le positionnement des 3 planches :
        #   - Planche du Bas (2x6)  : Espace de 30cm (12") du sol
        #   - Planche du Mid (2x12) : Espace de 10cm (4") au-dessus de la planche du Bas
        #   - Planche du Up (2x6)   : Espace de 10cm (4") au-dessus de la planche du Mid
        y_bas = 0.30                            # Espace du bas et/ou sol 30cm
        y_mid = y_bas + 0.15 + 0.10 + 0.15      # Centre de la planche du milieu (2x12)
        y_up = y_mid + 0.15 + 0.10 + 0.075      # Centre de la planche du haut (2x6)

        # Hauteur poteau dépasse de 10 cm (4") au-dessus
        poteau_height = y_up + 0.15 + 0.10      # Dépasse de 10cm en haut

        # ---------- FOR LOOP - Génération des poteaux alignés ---------- #
        for i in range(total_poteau):
            # Création du poteau (un cylindre de 0.1 rayon)
            poteau_obj = cmds.polyCylinder(radius=0.1, height=poteau_height)[0]     # le [0] c'est l'incrémentation de maya 0, 1, 2...

            # Calcul de la position X du poteau
            pos_x = i * spacing

            # Placement du poteau sur l'axe X (Y ajusté pour que la base repose au sol)
            cmds.move(pos_x, poteau_height / 2.0, 0, poteau_obj)


        # ---------- CRÉATION DES 3 PLANCHES HORIZONTALES (TRAVERSES) ---------- #
        # Liste des planches : (nom_variante, hauteur_y, largeur_l)
        planche_config = [("Planche_Bas_2x6", y_bas, 0.15), ("Planche_Centre_2x12", y_mid, 0.30), ("Planche_Haut_2x6", y_up, 0.15)]

        # Boucle pour générer et placer chacune des 3 planches (1 seul cube par planche pour la logueur totale de la clôture)
        for nom, y_pos, largeur_planche in planche_config:
            # Création du cube de la planche
            planche_obj = cmds.polyCube(width=1.0, height=largeur_planche, depth=0.05, name=nom)[0]

            # Scale en X de la planche sur toute la longueur de la clôture
            cmds.scale(total_length, 1, 1, planche_obj)

            # Alignement au centre X, à la hauteur Y spécifique & un petit décalé du poteau sur le Z pour éviter le clipping
            cmds.move(center_x, y_pos, 0.1, planche_obj)

# ------------------------------------------------------------------------------------------

def main():
    global widget               # Ça tool_window ou widget.close ça fait la même chose
    try:
        widget.close()
    except Exception:
        pass
    widget = FenceGenerator()
    widget.show()

main()