# Import de librairie de base
import os
import sys

# On a obtenue le folder dans lequel il y a notre ficher courant
# __file__ = le ficher courant
absolute_file_path = os.path.abspath(__file__)
absolute_folder_path = os.path.dirname(absolute_file_path)
print(absolute_folder_path)
# Append = Ajout des éléments
# On vient ajouter absolute_folder_path au path de python pour qu'il puisse trouver
sys.path.append(absolute_folder_path)

import importlib
import ui
# Reload pour refresh la cache
importlib.reload(ui)

def main():
    random_animation_ui = ui.RandomAnimationUI()
    random_animation_ui.show()

    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass

main()