'''
3. l'Apprenti

Grâce à votre script, le cowboy réussit à se commander un verre d'eau. Mieux vaut garder son esprit clair lorsqu'on arrive dans un nouvel endroit.

Au fond du bar, assis devant un vieux portable, un curieux personnage semble être en train de faire de la modélisation 3D dans Maya. Son air déprimé
interpelle le cowboy qui ne peut s'empêcher de venir en aide aux gens. L'artiste 3D du Far West lui explique qu'il est à la recherche de quelqu'un
pour l'aider dans une lourde tâche. Il ne veut pas tout de suite expliquer de quoi il s'agit, car il juge l'endroit trop bruyant. Il demande quand
même si le cowboy est intéressé à l'aider. Il devra d'abord faire ses preuves s'il veut en savoir plus. Comme il est nouveau dans cette ville et veut
se faire des amis, il accepte.

D'un air satisfait, le mystérieux modélisateur lui présente son test : Écrire un script Python qui tourne dans Maya qui affiche un message de son choix.

'''

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QTextEdit,
    QPushButton,
    QMessageBox
)
 
class MessageBoard(QWidget):
    # Initialisation de la fenêtre avec comme titre "Message board"
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message board")
        self.create_ui()

        # Définir la taille de la fenêtre et setter ses limites de redimensionnement
        self.resize(350, 200)
        self.setMinimumSize(350, 200)
        self.setMaximumSize(600, 500)

    # Création de l'interface utilisateur
    def create_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel("Message board")
        layout.addWidget(label)

        # Permet de conserver la zone de texte en mémoire pour pouvoir y accéder dans la fonction on_click
        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)
 
        # Créer un bouton pour envoyer le message
        self.button = QPushButton("Envoyer")
        layout.addWidget(self.button)
        self.button.clicked.connect(self.on_click)

    # Fonction appelée lorsque le bouton est cliqué
    def on_click(self):
        print("on click called")
        # Afficher le message dans une boîte de dialogue
        # toPlainText() permet de récupérer le texte multi-lignes contenu dans la zone de texte
        # PS: .text() est utilisé avec QLineEdit pour afficher le texte d'une seule ligne
        message = self.text_edit.toPlainText()
        QMessageBox.information(self, "Message", f"Message envoyé : {message}")
         
def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()
 
main()