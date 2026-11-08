"""8. Aider son prochain

Juste à temps, vous lancez le script. Le bruit des sabots et les cris de la cavalerie, qui
s’intensifiaient jusqu’ici, s’éloignent soudain.La menace est écartée grâce à vous ! C’est du moins
l’impression que vous avez, pour le moment…
En vous retournant, vous êtes surpris de voir une foule grandissante composée d’habitants. D’abord
perplexes, ils se mettent à crier et à applaudir votre exploit. C’est fou l’effet qu’un script peut
provoquer. ;)
Le maire de la ville, toujours à vos côtés, vous félicite. Puis, une idée vous vient : la menace n’a
été que temporairement écartée. Pour aider la ville, vous décidez de donner à tous le moyen d’utiliser
votre script. Il vous faudra documenter comment installer le script de l’atelier 7 et créer une icône.
Vous devrez aussi trouver un cobaye prêt à tester l’installation.

Consignes :

    Sur Git, rédigez une brève documentation qui explique où placer le script et comment configurer l’icône.
    Afin de bien tester vos instructions : demander à un habitant (un collègue de la classe) de tester vos instructions à la lettre."""



import maya.cmds as cmds


# ---------- PARAMÈTRES DE LA CHAISE ---------- #

assise_largeur = 4.0
assise_profondeur = 4.0
assise_epaisseur = 0.4

patte_largeur = 0.5
patte_hauteur = 3.0

dossier_largeur = 4.0
dossier_hauteur = 3.0
dossier_epaisseur = 0.4


# ---------- LISTE DES MORCEAUX DE LA CHAISE ---------- #

morceaux_chaise = []


# ---------- CALCULS DES DIMENSIONS & POSITIONS ---------- #

# Hauteur du centre de l'assise
assise_y = patte_hauteur + (assise_epaisseur / 2.0)

# Hauteur du centre des pattes
patte_y = patte_hauteur / 2.0

# Position des pattes aux quatre coins de l'assise
position_x = assise_largeur / 2.0 - patte_largeur / 2.0
position_z = assise_profondeur / 2.0 - patte_largeur / 2.0

# Position du dossier derrière l'assise
dossier_y = assise_y + (assise_epaisseur / 2.0) + (dossier_hauteur / 2.0)
dossier_z = -(assise_profondeur / 2.0) + (dossier_epaisseur / 2.0)


# ---------- CRÉATION DE L'ASSISE ---------- #

assise_obj = cmds.polyCube(name="Chaise_Assise", width=assise_largeur, height=assise_epaisseur, depth=assise_profondeur)[0]

cmds.move(0, assise_y, 0, assise_obj)

# Ajouter l'assise dans la liste
morceaux_chaise.append(assise_obj)


# ---------- CRÉATION DES 4 PATTES ---------- #

# Positions X et Z des quatre pattes
positions_pattes = [
    (-position_x, -position_z),
    (-position_x, position_z),
    (position_x, -position_z),
    (position_x, position_z)
]

# Génération et positionnement des pattes
for i in range(4):

    patte_obj = cmds.polyCube(name="Chaise_Patte_" + str(i + 1), width=patte_largeur, height=patte_hauteur, depth=patte_largeur)[0]

    cmds.move(
        positions_pattes[i][0],
        patte_y,
        positions_pattes[i][1],
        patte_obj
    )

    # Ajouter la patte dans la liste
    morceaux_chaise.append(patte_obj)


# ---------- CRÉATION DU DOSSIER ---------- #

dossier_obj = cmds.polyCube(name="Chaise_Dossier", width=dossier_largeur, height=dossier_hauteur, depth=dossier_epaisseur)[0]

cmds.move(0, dossier_y, dossier_z, dossier_obj)

# Ajouter le dossier dans la liste
morceaux_chaise.append(dossier_obj)


# ---------- FUSION DES MORCEAUX ---------- #

# Sélectionner les six morceaux
cmds.select(morceaux_chaise)

# Fusionner les morceaux en un seul objet
chaise_obj = cmds.polyUnite(name="Chaise", constructionHistory=False)[0]