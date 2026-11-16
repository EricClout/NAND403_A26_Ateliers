from PySide6.QtWidgets import QWidget, QSlider, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt
from maya import cmds
import maya.OpenMayaUI as omui
from shiboken6 import wrapInstance
 
def maya_main_window():
    pointer = omui.MQtUtil.mainWindow()
    return wrapInstance(int(pointer), QWidget)
 
class LiveScale(QWidget):
    def __init__(self):
        super().__init__(maya_main_window())
        self.setWindowFlags(Qt.Window)
        self.build_ui()
 
    def build_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.create_label()
        self.create_slider()
 
    def create_label(self):
        self.label_text_template = "Scale : "
        self.scale_label = QLabel(self.label_text_template + f"{50}")
        self.main_layout.addWidget(self.scale_label)
 
    def create_slider(self):
        self.scale_slider = QSlider()
        self.scale_slider.setOrientation(Qt.Horizontal)
        self.scale_slider.setRange(1, 300)
        self.scale_slider.setValue(50)
        self.scale_slider.valueChanged.connect(self.apply_scale)
        self.main_layout.addWidget(self.scale_slider)
 
    def update_label(self, scale_factor):
        self.scale_label.setText(self.label_text_template + f"{scale_factor}")
 
    def apply_scale(self):
        scale_factor = self.scale_slider.value()/100.0
        self.update_label(scale_factor)
        selection = cmds.ls(selection=True, transforms=True)
        for obj in selection:
            cmds.setAttr(f"{obj}.scale", scale_factor, scale_factor, scale_factor)
 
def show_live_scale():
    global live_scale
    try:
        live_scale.close()
    except:
        pass
    live_scale = LiveScale()
    live_scale.show()
 
show_live_scale()


"""from PySide6.QtWidgets import QWidget, QSlider, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt
from maya import cmds
import maya.OpenMayaUI as omui
from shiboken6 import wrapInstance

#   Fait que le popout de l'outil soit tjs apparent dans maya même si on clique à côté
def maya_main_window():
    pointer = omui.MQtUtil.mainWindow()
    return wrapInstance(int(pointer), QWidget)
# --------------------------------------------------------------------------------------
 
class LiveScale(QWidget):
    def __init__(self):
        super().__init__(maya_main_window())
        self.setWindowFlags(Qt.Window)
        self.build_ui()
 
    def build_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.create.label()
        self.create.slider()
        self.scale_lable = QLabel("Scale : 50")
        self.scale_slider = QSlider()
        self.scale_slider.setOrientation(Qt.Horizontal)
        self.scale_slider.setRange(1, 100)
        self.scale_slider.setValue(50)
        self.main_layout.addWidget(self.scale_slider)
        self.apply_button = QPushButton("Apply Scale")
        self.scale_slider.valueChanged.connect(self.on_apply_scale)
#######################        self.apply_button.clicked.connect(self.on_apply_scale_clicked)
# Pour mettre un bouton        self.main_layout.addWidget(self.apply_button)
 
    def on_apply_scale(self):
        scale_factor = self.scale_slider.value()/100.0
        selection = cmds.ls(selection=True, transforms=True)
        for obj in selection:
            cmds.setAttr(f"{obj}.scale", scale_factor, scale_factor, scale_factor)
 
def show_live_scale():
    global live_scale
    try:
        live_scale.close()
    except:
        pass
    live_scale = LiveScale()
    live_scale.show()
 
show_live_scale()"""