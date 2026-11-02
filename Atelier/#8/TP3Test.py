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

from UI import MyClass

def my_function():
    absolute_path = os.patch.abspath(os.path.curdir)
    print(absolute_path)

my_class = MyClass()
my_class.print_variable()