"""Satisfait de votre dernier outil, le modélisateur vous fait maintenant confiance.
Il s'appelle Jason et vous annonce qu'il est le maire de la ville. Rassuré de s'être fait un ami, 
il se confie un peu à vous. Certains bandits menacent de piller la ville. Pour se protéger, et c'est 
pour cette raison qu'il veut redessiner la ville en commençant par l'ajout de défense. Il vous demande 
encore de l'aide pour construire des clôtures. Étant un tech artist, votre réflexe est, bien sûr, de faire 
un script dans Maya pour accélérer le processus."""

#### CODE DE L'ATELIER 4-5 ###
import random
from maya import cmds
import maya.cmds as cmds

import random
from maya import cmds
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QPushButton,
    QSpinBox,
    QDoubleSpinBox
)

# ------------------------------------------------------------------------------------------
# Classe personnalisée pour gérer la génération aléatoire d'objets dans Maya
class RandomGenerator(QWidget):
    # Initialisation de la fenêtre avec comme titre "Atelier 4-5"
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 4-5")
        self.create_ui()

        # Définir la taille de la fenêtre et setter ses limites
        self.resize(400, 300)
        self.setMinimumSize(400, 250)

    #                       --------------------

    # Création de l'interface utilisateur
    def create_ui(self):
        # Layout principal vertical
        layout = QVBoxLayout(self)

        # Crée la ligne (Layout de l'interface) horizontal pour le Nb d'objets
        objs_layout = QHBoxLayout()
        objs_label = QLabel("Nb d'objects ?")

        # ---------- (QSpinBox) !!! C'est nouveau ça !!! ---------- #
        # Crée à case pour enter un Nb d'objets à spawner
        self.obj_spin = QSpinBox()                        # Crée la case éditable
        self.obj_spin.setRange(1, 1000)                   # Range max de 1000 objets
        self.obj_spin.setValue(5)                         # Valeur par défaut de 5 objets

        # Crée la ligne du texte (label) et du spinbox au layout horizontal
        objs_layout.addWidget(objs_label)
        objs_layout.addWidget(self.obj_spin)
        layout.addLayout(objs_layout)                    # Ceci ajoute les 2 lignes ci-dessus au layout vertical principal

        # ----------- (QGridLayout) !!! C'est nouveau ça !!! ----------- #
        #  Grille pour organiser les limites Min / Max des valeurs entrées
        grid_layout = QGridLayout()

        # En-têtes des colonnes Min & Max
        grid_layout.addWidget(QLabel("Min"), 0, 1)          # En-tête colonne 1
        grid_layout.addWidget(QLabel("Max"), 0, 2)          # En-tête colonne 2

        # ------------------------- "Position X" ------------------------ #
        # Configuration des colonnes & de la rangée
        grid_layout.addWidget(QLabel("Position X"), 1, 0)   # Titre Rangées #1 à gauche
        self.pos_x_min = QDoubleSpinBox()                   # Crée la case éditable
        self.pos_x_min.setRange(-1000, 1000)                # Range Min & Max
        self.pos_x_min.setValue(-50)                        # Valeur par défaut

        self.pos_x_max = QDoubleSpinBox()                   # Crée la case éditable
        self.pos_x_max.setRange(-1000, 1000)                # Range Min & Max
        self.pos_x_max.setValue(50)                         # Valeur par défaut

        grid_layout.addWidget(self.pos_x_min, 1, 1)         # Rangée 1, Colonne 1
        grid_layout.addWidget(self.pos_x_max, 1, 2)         # Rangée 1, Colonne 2

        # ------------------------- "Position Y" ------------------------ #
        # Configuration des colonnes & de la rangée
        grid_layout.addWidget(QLabel("Position Y"), 2, 0)   # Titre Rangées #2 à gauche
        self.pos_y_min = QDoubleSpinBox()                   # Crée la case éditable
        self.pos_y_min.setRange(-1000, 1000)                # Range Min & Max
        self.pos_y_min.setValue(0)                          # Valeur par défaut

        self.pos_y_max = QDoubleSpinBox()                   # Crée la case éditable
        self.pos_y_max.setRange(-1000, 1000)                # Range Min & Max
        self.pos_y_max.setValue(10)                         # Valeur par défaut

        grid_layout.addWidget(self.pos_y_min, 2, 1)         # Rangée 2, Colonne 1
        grid_layout.addWidget(self.pos_y_max, 2, 2)         # Rangée 2, Colonne 2

        # ------------------------- "Position Z" ------------------------ #
        # Configuration des colonnes & de la rangée
        grid_layout.addWidget(QLabel("Position Z"), 3, 0)   # Titre Rangées #3 à gauche
        self.pos_z_min = QDoubleSpinBox()                   # Crée la case éditable
        self.pos_z_min.setRange(-1000, 1000)                # Range Min & Max
        self.pos_z_min.setValue(-10)                        # Valeur par défaut

        self.pos_z_max = QDoubleSpinBox()                   # Crée la case éditable
        self.pos_z_max.setRange(-1000, 1000)                # Range Min & Max
        self.pos_z_max.setValue(10)                         # Valeur par défaut

        grid_layout.addWidget(self.pos_z_min, 3, 1)         # Rangée 3, Colonne 1
        grid_layout.addWidget(self.pos_z_max, 3, 2)         # Rangée 3, Colonne 2

        # --------------------------- "Scale" -------------------------- #
        # Configuration des colonnes & de la rangée
        grid_layout.addWidget(QLabel("Scale"), 4, 0)        # Titre Rangées #4 à gauche
        self.scale_min = QDoubleSpinBox()                   # Crée la case éditable
        self.scale_min.setRange(0.1, 100)                   # Range Min & Max
        self.scale_min.setValue(1)                          # Valeur par défaut 

        self.scale_max = QDoubleSpinBox()                   # Crée la case éditable
        self.scale_max.setRange(0.1, 100)                   # Range Min & Max
        self.scale_max.setValue(3)                          # Valeur par défaut

        grid_layout.addWidget(self.scale_min, 4, 1)         # Rangée 4, Colonne 1
        grid_layout.addWidget(self.scale_max, 4, 2)         # Rangée 4, Colonne 2

        
        # Ajout des infos ci-dessus au layout principal
        layout.addLayout(grid_layout)                       # Ceci ajoute X, Y, Z & Scale au layout vertical principal
        
        #                       --------------------

        # Création du BOUTON magique // ATTENTION : Placez le bouton APRÈS les "spinbox" pour une meilleure ergonomie
        self.button = QPushButton("Click donc ici voir... MAGIE !")
        layout.addWidget(self.button)                       # Ceci ajoute le bouton au layout vertical principal
        
        # Connexion du signal 'clicked' vers la méthode de génération
        self.button.clicked.connect(self.on_click)

        #                       --------------------

    # Fonction appelée via le Bouton pour appliquer nos choix et les générer 
    def on_click(self):
        # Récupère la Qty d'objets à générer
        qty = self.obj_spin.value()

        # Récupère les limites des positions X, Y, Z
        x_min = self.pos_x_min.value()
        x_max = self.pos_x_max.value()

        y_min = self.pos_y_min.value()
        y_max = self.pos_y_max.value()

        z_min = self.pos_z_min.value()
        z_max = self.pos_z_max.value()

        # Récupère les limites du Scale
        s_min = self.scale_min.value()
        s_max = self.scale_max.value()

        # ----------FOR LOOP !!! C'est nouveau ça !!! ---------- #
        # Pour générer les objs inscrites dans l'outil
        for _ in range(qty):
            # Choisi Random un forme * la Qty entrée parmi ceux dans le paramètre
            forme = random.choice(["cube", "cylindre", "cone", "sphere"])

            # Création des formes 3D dans la scène Maya de façon Random
            # Ça prend les noms spécifique que Maya a par défaut pour les créer
            if forme == "cube":
                obj_create = cmds.polyCube()[0]          # Ceci [0] & "cmds" c'est géré par Maya pour récupérer le nom de l'objet créé
            elif forme == "cylindre":
                obj_create = cmds.polyCylinder()[0]
            elif forme == "cone":
                obj_create = cmds.polyCone()[0]
            else:
                obj_create = cmds.polySphere()[0]

            # Randomize les Ojbs dans la scène en se fiant aux limites choisies dans l'outil
            rand_x = random.uniform(x_min, x_max)
            rand_y = random.uniform(y_min, y_max)
            rand_z = random.uniform(z_min, z_max)
            rand_scale = random.uniform(s_min, s_max)

            # Applique les nouvelles valeurs aux Objs en les plaçant dans Maya
            cmds.move(rand_x, rand_y, rand_z, obj_create)
            cmds.scale(rand_scale, rand_scale, rand_scale, obj_create)

# ------------------------------------------------------------------------------------------

def main():
    global widget               # Ça tool_window ou widget.close ça fait la même chose
    try:
        widget.close()
    except Exception:
        pass
    widget = RandomGenerator()
    widget.show()

main()



"""
# ------------------------------------------------------------------------------------------
#                        Cette partie c'est le code fourni de base.
# ------------------------------------------------------------------------------------------
class RandomGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 4-5")
        self.setMinimumWidth(400)
        self.build_ui()
    
    def build_ui(self):
        layout = QVBoxLayout(self)

        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_object)
        layout.addWidget(self.create_button)

    def create_object(self):
        forme = random.choice(["cube", "cylindre", "sphere"])

        if forme == "cube":
            objet = cmds.polyCube()[0]
        elif forme == "cylindre":
            objet = cmds.polyCylinder()[0]
        else:
            objet = cmds.polySphere()[0]

        random_value = random.uniform(-10, 10)
        cmds.move(random_value, random_value, random_value, objet)


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RandomGenerator()
    tool_window.show()

main()"""