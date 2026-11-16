"""Grâce à votre script, vous réussissez à retrouver votre cheval qui vous attendait sagement. Vous saluez Jason qui vous quitte pour la nuit.
En attrapant votre bagage pour aller vous reposer à l'auberge, un bout de papier coincé sur la selle attire votre attention. 
Mme/Mr Cowboy
Votre arrivée dans la ville ne passe pas inaperçue. Votre talent pour les scripts est impressionnant, J'ai besoin de vous, ma plantation de
cactus se meurt… Pourriez-vous m'aider à la sauver ? Rendez-vous demain matin à la première heure dans le désert, en dehorsde la ville, si vous
avez ce qu'il faut. En échange, une jolie somme d'or vous attend.

- Maïa 

Votre bourse est presque vide et vous savez que vous pouvez l'aider. C'est un coup de chance du destin. 

Votre idée est simple, créer un outil de type scatter qui propagera en un clic le dernier cactus vivant de la plantation. Votre outil devra supporter
l'affichage "always on top" de Maya ainsi que le live edit. (les changements se font en temps réel)"""


import random
from maya import cmds
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QSpinBox,
    QDoubleSpinBox,
    QPushButton,
    QMessageBox
)


class Scatter(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scatter")
        self.setMinimumWidth(250)
        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout(self)
        form = QFormLayout()
        layout.addLayout(form)

        self.count_spin = QSpinBox()
        self.count_spin.setRange(1, 100)
        self.count_spin.setValue(10)
        form.addRow("Copies", self.count_spin)

        self.radius_spin = QDoubleSpinBox()
        self.radius_spin.setRange(1.0, 50.0)
        self.radius_spin.setValue(10.0)
        form.addRow("Radius", self.radius_spin)

        self.seed_spin = QSpinBox()
        self.seed_spin.setRange(0, 9999)
        form.addRow("Seed", self.seed_spin)

        scatter_button = QPushButton("Scatter")
        scatter_button.clicked.connect(self.scatter)
        layout.addWidget(scatter_button)

    def scatter(self):
        selection = cmds.ls(selection=True, transforms=True)
        if not selection:
            QMessageBox.warning(self, "Scatter", "Select an object first.")
            return
        source = selection[0]

        cmds.undoInfo(openChunk=True)
        try:
            random.seed(self.seed_spin.value())
            radius = self.radius_spin.value()
            group = cmds.group(empty=True, name="scatter_grp")
            for i in range(self.count_spin.value()):
                copy = cmds.duplicate(source)[0]
                copy = cmds.parent(copy, group)[0]
                x = random.uniform(-radius, radius)
                z = random.uniform(-radius, radius)
                cmds.move(x, 0, z, copy, relative=True)
        finally:
            cmds.undoInfo(closeChunk=True)


def show_tool():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = Scatter()
    tool_window.show()


show_tool()
