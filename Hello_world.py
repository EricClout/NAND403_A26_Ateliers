'''
Note Perso: 
----------------------
**** Pour configuer USER ****
git config --global user.email "you@example.com"
git config --global user.name "Your Name"

*** Pour setter python ***
\WPy64-31180\python-3.11.8.amd64\python.exe -m venv .venv 
.\.venv\Scripts\Activate.ps1 
pip install pySide6

*** Pour cloner le repo sur nouvelle ordi ***
Se fait AUTO avec l'App GitHub
1: Lancer le Terminal dans windows
2.1: Aller dans le dossier où cloner et après copier le lien du GitHub
2.2: suivre les commandes suivantes:
PS C:\Users\ecloutier1> cd repos
PS C:\Users\ecloutier1\repos> git clone https://github.com/EricClout/NAND403_A26_TP1.git
----------------------
Ouvrir un ficher JSON avec Python
-> Path (1: Hard coder, 2: Lire input, 3: Argument)
-> Fonction qui load le fichier JSON
'''
import sys

a = "je suis un test string"
print(sys.argv[1])



# NOTE POUR TP1 +/- 180 lignes
# Comment charger un fichier json en mémoire
this_is_a_variable = 42 # Ok
thisIsAVariable = 42 # Wrong

#def = pour définir une fonction, my_function = nom de la fonction, () = paramètres de la fonction
def my_function(): # Ok
    print("Good Function Name")
def myFunction(): # Wrong
    print("Bad Function Name")

my_function("Will", 1.2, [420])


# from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
'''