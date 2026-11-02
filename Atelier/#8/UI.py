from Pyside6.Qwidgets import (
    Qwidget
)

class RandomAnimationUI(QWideget) :
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Animation Tool")
        self.create_ui()
        # Définir la taille de la fenêtre et setter ses limites de redimensionnement
        self.resize(350, 200)
        self.setMinimumSize(350, 200)
        self.setMaximumSize(600, 500)

    def print_variable(self):
        print(self.my_variable)