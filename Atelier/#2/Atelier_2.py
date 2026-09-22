'''
2. Le Saloon

— Où est le saloon de ce trou perdu ?

Demanda l'inconnu au shérif après avoir refusé de s'identifier malgré le splendide formulaire que vous lui avez gracieusement fourni. Le shérif, ahuri par la confiance du mystérieux cavalier, lui désigna un vieux bâtiment fraichement construit dont les vibrations de l'ambiance festive à l'intérieur parvenaient aux oreilles aiguisées du mystérieux cowboy.

Une fois à l'intérieur, le vacarme candide fut remplacé par un silence de mort. Après un long moment d'échange de regards furtifs du côté des fêtards, le nouvel arrivant dit d'une voix sèche : 

— J'ai soif, qu'est-ce qu'il y a à boire ?

Le barman consulta son inventaire puis annonça :
— J'ai seulement un fichier JSON. On aurait besoin d'un tech artist pour visualiser les données…

À ce moment, tout le bar se tourna vers vous et votre ordinateur. Aidez notre cowboy à commander son drink en lui bâtissant un outil pour afficher dans un tableau les différents drinks à l'aide de PySide6.
'''
import sys
import json
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem
    )

json_file = sys.argv[1]
print(json_file)

try:
    file = open(json_file)
    data = json.load(file)
    print(type(data))
except:
    print(f"Erreur lors du load du fichier {json_file}")

for i in data:
    for k in i.values():
        print(f"   - {k}")
# print(f"Drink: {drink['name']}, Price: {drink['price']}, Type: {drink['type']}")

'''with open(json_file) as json_data:
    data = json.load(json_data)
    print(data)'''

app = QApplication()
window = QMainWindow()
window.show()
sys.exit(app.exec())