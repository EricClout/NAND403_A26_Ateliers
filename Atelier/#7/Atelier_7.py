"""timing_group = QGroupBox("Animation Timing")
timing_layout = QHBoxLayout()
timing_group.setLayout(timing_layout)"""

"""7. La cavalerie

Le raisonnement des coups de marteau sur les poteaux de clôture que vous étiez en train d'installer au tôt fait d'attirer des problèmes.
Les fameux mécréants dont parlait Jason passent à l'attaque, les petites clôtures ne feront pas le poids. 
Vos yeux de tech artiste/cowboy/mystérieux analysent la cavalerie. Vous remarquez avec surprise que leurs mouvements sont synchronisés
comme s'ils étaient contrôlés par des keyframes! Vite, vous sortez votre revolver-laptop-rtx-rog afin d'écrire un script Maya qui pourra
les renvoyer chez eux (100m plus loin... on va dire)

Vous devez donc réaliser les étapes suivantes.

    utiliser un cube comme proxy à la place de la cavalerie
    Créer une animation de 100 frames
    déplacer le cube à au moins 3 positions différentes sur la ligne du temps (3 keyframes) 

Vous aurez besoin des outils suivants pour y arriver.

    Ajout de keyframe cmds.setKeyframe(objet, attribute, value, time) 
    tout effacer cmds.cutKey(objet, clear=True) **timeSliderClearKey;**
    configurer la durée de l'animation cmds.playbackOptions(min, max)"""

from maya import cmds
import maya.cmds as cmds

class animationCheval():

    object = "pCube1"
    timeStart = 0
    timeStop = 100

    cmds.cutKey(object, clear=True)
    cmds.scale(10, 10, 10)


    cmds.setKeyframe(object, attribute="translateX", value=0, time=0)
    cmds.setKeyframe(object, attribute="translateY", value=0, time=0)
    cmds.setKeyframe(object, attribute="translateX", value=20, time=33)
    cmds.setKeyframe(object, attribute="translateY", value=0, time=33)
    cmds.setKeyframe(object, attribute="translateX", value=50, time=66)
    cmds.setKeyframe(object, attribute="translateY", value=0, time=66)
    cmds.setKeyframe(object, attribute="translateX", value=100, time=99)
    cmds.setKeyframe(object, attribute="translateY", value=50, time=100)

    cmds.playbackOptions(animationStartTime=0)
    cmds.playbackOptions(animationEndTime=100)
    #cmds.playbackOptions(min=0, max=200)
    cmds.play( forward=True )
    cmds.play( backward=True )
