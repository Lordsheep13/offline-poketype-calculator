#!/usr/bin/env python
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QBoxLayout, QComboBox, QStackedLayout, QTextEdit, QMenuBar, QGraphicsDropShadowEffect, QRadioButton
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QIcon, QFont, QPixmap, QColor
from pkTypeCalculatorShell import *

typeCombos = ["normal","fighting","flying","poison","ground","rock","bug","ghost","steel","fire","water","grass","electric","psychic","ice","dragon","dark","fairy"]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pokemon Type Calculator")
        self.setGeometry(0,0,600,400)
        self.setStyleSheet("background-color: black;")
        self.initUI()
        self.calculator()

    def initUI(self):

        #root widget
        central_widget = QWidget()
        central_widget.setStyleSheet("background-color: red; color: black;")
        central_layout = QHBoxLayout()
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

        #input widget
        input_widget = QWidget()
        input_widget.setStyleSheet("background-color: red;")
        input_widget.setFixedWidth(150)
        input_layout = QVBoxLayout()

        input_widget.setLayout(input_layout)

        #input items
        self.help_window = None

        self.input_type_combo = QComboBox()
        self.input_type_combo.addItems(typeCombos)
        self.input_second_type_combo = QComboBox()
        self.input_second_type_combo.addItems(typeCombos)
        
        self.input_type_combo.setCurrentIndex(-1)
        self.input_second_type_combo.setCurrentIndex(-1)
        self.input_type_combo.activated.connect(self.typetest)
        self.input_second_type_combo.activated.connect(self.typetest)
        self.input_submit = QPushButton("submit")
        self.input_submit.clicked.connect(self.typetest)
        self.input_submit.clicked.connect(self.calculator)

        self.input_radio_atk = QRadioButton("Attack")
        self.input_radio_def = QRadioButton("Defend")
        self.input_radio_atk.setChecked(True)
        self.input_radio_atk.toggled.connect(self.changepage)
        self.input_radio_def.toggled.connect(self.changepage)

        #output info widget
        output_info = QWidget()
        output_info.setFixedWidth(100)
        output_info.setStyleSheet("background-color: white;")

        self.output_info_layout = QStackedLayout()
        output_info.setLayout(self.output_info_layout)

        #output info atk
        output_info_atk = QWidget()
        output_info_atk_layout = QVBoxLayout()
        output_info_atk.setStyleSheet("color: black;")
        output_info_atk.setLayout(output_info_atk_layout)
        
        output_info_atk_labelx2 = QLabel("damage x2")
        output_info_atk_labelx1 = QLabel("damage x1")
        output_info_atk_labelx05 = QLabel("damage x0.5")
        output_info_atk_labelx0 = QLabel("damage x0")

        #output info def
        output_info_def = QWidget()
        output_info_def_layout = QVBoxLayout()
        output_info_def.setStyleSheet("color: black;")
        output_info_def.setLayout(output_info_def_layout)

        output_info_def_labelx4 = QLabel("damage x4")
        output_info_def_labelx2 = QLabel("damage x2")
        output_info_def_labelx1 = QLabel("damage x1")
        output_info_def_labelx05 = QLabel("damage x0.5")
        output_info_def_labelx025 = QLabel("damage x0.25")
        output_info_def_labelx0 = QLabel("damage x0")

        #output widget
        output_widget = QWidget()
        output_widget.setStyleSheet("background-color: white;")
        self.output_layout = QStackedLayout()
        self.output_layout.setCurrentIndex(0)

        output_widget.setLayout(self.output_layout)


        #>>output pages

        #attackpage
        output_attack_page = QWidget()
        output_atk_page_layout = QVBoxLayout()
        output_attack_page.setStyleSheet("background-color: lightgray;")# padding: 0; margin: 0;")
        output_attack_page.setLayout(output_atk_page_layout)
        output_atk_page_layout.setContentsMargins(0,0,0,0)
        #output_atk_page_layout.setSpacing(0)

        #defendpage
        output_defend_page = QWidget()
        output_def_page_layout = QVBoxLayout()
        output_defend_page.setStyleSheet("background-color: lightgray;") #padding: 0; margin: 0;") 
        output_defend_page.setLayout(output_def_page_layout)
        output_def_page_layout.setContentsMargins(0,0,0,0)
        #output_def_page_layout.setSpacing(0)
        
        #x2 atk
        output_attack_x2 = QWidget()
        self.output_attack_x2_layout = QGridLayout()
        output_attack_x2.setLayout(self.output_attack_x2_layout)
        output_attack_x2.setStyleSheet("background-color: white;")

        #x1 atk
        output_attack_x1 = QWidget()
        self.output_attack_x1_layout = QGridLayout()
        output_attack_x1.setLayout(self.output_attack_x1_layout)
        output_attack_x1.setStyleSheet("background-color: white;")
        
        #x0.5 atk
        output_attack_x05 = QWidget()
        self.output_attack_x05_layout = QGridLayout()
        output_attack_x05.setLayout(self.output_attack_x05_layout)
        output_attack_x05.setStyleSheet("background-color: white;")
        
        #x0 atk
        output_attack_x0 = QWidget()
        self.output_attack_x0_layout = QGridLayout()
        output_attack_x0.setLayout(self.output_attack_x0_layout)
        output_attack_x0.setStyleSheet("background-color: white;")

        #x4 def
        output_defend_x4 = QWidget()
        self.output_defend_x4_layout = QGridLayout()
        output_defend_x4.setLayout(self.output_defend_x4_layout)
        output_defend_x4.setStyleSheet("background-color: white;")
        
        #x2 def
        output_defend_x2 = QWidget()
        self.output_defend_x2_layout = QGridLayout()
        output_defend_x2.setLayout(self.output_defend_x2_layout)
        output_defend_x2.setStyleSheet("background-color: white;")
        
        #x1 def
        output_defend_x1 = QWidget()
        self.output_defend_x1_layout = QGridLayout()
        output_defend_x1.setLayout(self.output_defend_x1_layout)
        output_defend_x1.setStyleSheet("background-color: white;")
        
        #x0.5 def
        output_defend_x05 = QWidget()
        self.output_defend_x05_layout = QGridLayout()
        output_defend_x05.setLayout(self.output_defend_x05_layout)
        output_defend_x05.setStyleSheet("background-color: white;")
        
        #x0.25 def
        output_defend_x025 = QWidget()
        self.output_defend_x025_layout = QGridLayout()
        output_defend_x025.setLayout(self.output_defend_x025_layout)
        output_defend_x025.setStyleSheet("background-color: white;")
        
        #x0 def
        output_defend_x0 = QWidget()
        self.output_defend_x0_layout = QGridLayout()
        output_defend_x0.setLayout(self.output_defend_x0_layout)
        output_defend_x0.setStyleSheet("background-color: white;")

        #<<

        #>>all type pngs

        sprites = accessIni("sprites")

        self.normalPng = QPixmap(f"{sprites}/1.png")
        self.fightingPng = QPixmap(f"{sprites}/2.png")
        self.flyingPng = QPixmap(f"{sprites}/3.png")
        self.poisonPng = QPixmap(f"{sprites}/4.png")
        self.groundPng = QPixmap(f"{sprites}/5.png")
        self.rockPng = QPixmap(f"{sprites}/6.png")
        self.bugPng = QPixmap(f"{sprites}/7.png")
        self.ghostPng = QPixmap(f"{sprites}/8.png")
        self.steelPng = QPixmap(f"{sprites}/9.png")
        self.firePng = QPixmap(f"{sprites}/10.png")
        self.waterPng = QPixmap(f"{sprites}/11.png")
        self.grassPng = QPixmap(f"{sprites}/12.png")
        self.electricPng = QPixmap(f"{sprites}/13.png")
        self.psychicPng = QPixmap(f"{sprites}/14.png")
        self.icePng = QPixmap(f"{sprites}/15.png")
        self.dragonPng = QPixmap(f"{sprites}/16.png")
        self.darkPng = QPixmap(f"{sprites}/17.png")
        self.fairyPng = QPixmap(f"{sprites}/18.png")

        #<<

        #add widget
        central_layout.addWidget(input_widget)
        central_layout.addWidget(output_info)
        central_layout.addWidget(output_widget)

        input_layout.addWidget(self.input_type_combo)
        input_layout.addWidget(self.input_second_type_combo)
        input_layout.addWidget(self.input_submit)
        input_layout.addWidget(self.input_radio_atk)
        input_layout.addWidget(self.input_radio_def)

        self.output_layout.addWidget(output_attack_page)
        self.output_layout.addWidget(output_defend_page)
        
        output_atk_page_layout.addWidget(output_attack_x2)
        output_atk_page_layout.addWidget(output_attack_x1)
        output_atk_page_layout.addWidget(output_attack_x05)
        output_atk_page_layout.addWidget(output_attack_x0)
        
        output_def_page_layout.addWidget(output_defend_x4)
        output_def_page_layout.addWidget(output_defend_x2)
        output_def_page_layout.addWidget(output_defend_x1)
        output_def_page_layout.addWidget(output_defend_x05)
        output_def_page_layout.addWidget(output_defend_x025)
        output_def_page_layout.addWidget(output_defend_x0)

        self.output_info_layout.addWidget(output_info_atk)
        self.output_info_layout.addWidget(output_info_def)
        
        output_info_atk_layout.addWidget(output_info_atk_labelx2)
        output_info_atk_layout.addWidget(output_info_atk_labelx1)
        output_info_atk_layout.addWidget(output_info_atk_labelx05)
        output_info_atk_layout.addWidget(output_info_atk_labelx0)
        
        output_info_def_layout.addWidget(output_info_def_labelx4)
        output_info_def_layout.addWidget(output_info_def_labelx2)
        output_info_def_layout.addWidget(output_info_def_labelx1)
        output_info_def_layout.addWidget(output_info_def_labelx05)
        output_info_def_layout.addWidget(output_info_def_labelx025)
        output_info_def_layout.addWidget(output_info_def_labelx0)
        
        #output_info_def_layout.addWidget()

    def typetest(self):
        print(self.input_type_combo.currentIndex())
        print(self.input_second_type_combo.currentIndex())

    def changepage(self):
        changer = self.sender()
        if changer.text() == "Attack":
            self.output_layout.setCurrentIndex(0)
            self.output_info_layout.setCurrentIndex(0)
        if changer.text() == "Defend":
            self.output_layout.setCurrentIndex(1)
            self.output_info_layout.setCurrentIndex(1)
    
    def calculator(self):
        spriteindex = ["nothing","normal","fighting","flying","poison","ground","rock","bug","ghost","steel","fire","water","grass","electric","psychic","ice","dragon","dark","fairy"]
        rootFolder = accessIni("rootFolder")
        path2glossary = accessIni("path2glossary")
        sprites = accessIni("sprites")
        hassecondtype = False

        if self.output_layout.currentIndex() == 0:
            hassecondtype = False
            maketypecall(self.input_second_type_combo.currentText())

        if self.output_layout.currentIndex() == 1:
            if self.input_type_combo.currentIndex() > -1:
                if self.input_second_type_combo.currentIndex() > -1:
                    if not self.input_type_combo.currentIndex() == self.input_second_type_combo.currentIndex():
                        hassecondtype = True
                        maketypecall(self.input_second_type_combo.currentText())



            maketypecall(self.input_type_combo.currentText())
            #typecalc(hassecondtype)
            print(normalAtk)
            print(normalDef)
            print(current_pokemon)


            #def x4
            for item in current_pokemon['pokemon_immunity']:
                for pktype in spriteindex:
                    if item == pktype:
                        pixlabel = QLabel(self)
                        pixmap = QPixmap(f"{sprites}/{spriteindex.index(item)}")
                        pixlabel.setPixmap(pixmap)
                        pixlabel.setScaledContents(True)
                        pixlabel.setFixedSize(30,10)
                        self.output_defend_x0_layout.addWidget(pixlabel)

            #def x2
            for item in current_pokemon['pokemon_immunity']:
                for pktype in spriteindex:
                    if item == pktype:
                        pixlabel = QLabel(self)
                        pixmap = QPixmap(f"{sprites}/{spriteindex.index(item)}")
                        pixlabel.setPixmap(pixmap)
                        pixlabel.setScaledContents(True)
                        pixlabel.setFixedSize(30,10)
                        self.output_defend_x0_layout.addWidget(pixlabel)

            #def x1
            for item in current_pokemon['pokemon_immunity']:
                for pktype in spriteindex:
                    if item == pktype:
                        pixlabel = QLabel(self)
                        pixmap = QPixmap(f"{sprites}/{spriteindex.index(item)}")
                        pixlabel.setPixmap(pixmap)
                        pixlabel.setScaledContents(True)
                        pixlabel.setFixedSize(30,10)
                        self.output_defend_x0_layout.addWidget(pixlabel)

            #def x05
            for item in current_pokemon['pokemon_immunity']:
                for pktype in spriteindex:
                    if item == pktype:
                        pixlabel = QLabel(self)
                        pixmap = QPixmap(f"{sprites}/{spriteindex.index(item)}")
                        pixlabel.setPixmap(pixmap)
                        pixlabel.setScaledContents(True)
                        pixlabel.setFixedSize(30,10)
                        self.output_defend_x0_layout.addWidget(pixlabel)

            #def x025
            for item in current_pokemon['pokemon_immunity']:
                for pktype in spriteindex:
                    if item == pktype:
                        pixlabel = QLabel(self)
                        pixmap = QPixmap(f"{sprites}/{spriteindex.index(item)}")
                        pixlabel.setPixmap(pixmap)
                        pixlabel.setScaledContents(True)
                        pixlabel.setFixedSize(30,10)
                        self.output_defend_x0_layout.addWidget(pixlabel)

    #        #def x0
            for item in current_pokemon['pokemon_immunity']:
                for pktype in spriteindex:
                    if item == pktype:
                        pixlabel = QLabel(self)
                        pixmap = QPixmap(f"{sprites}/{spriteindex.index(item)}")
                        pixlabel.setPixmap(pixmap)
                        pixlabel.setScaledContents(True)
                        pixlabel.setFixedSize(30,10)
                        self.output_defend_x0_layout.addWidget(pixlabel)

            #atk x2
            for item in current_pokemon['pokemon_strength']:
                for pktype in spriteindex:
                    if item == pktype:
                        pixlabel = QLabel(self)
                        pixmap = QPixmap(f"{sprites}/{spriteindex.index(item)}")
                        pixlabel.setPixmap(pixmap)
                        pixlabel.setScaledContents(True)
                        pixlabel.setFixedSize(30,10)
                        self.output_attack_x2_layout.addWidget(pixlabel)

            #atk x1
            for item in normalAtk:
                for pktype in spriteindex:
                    if item == pktype:
                        pixlabel = QLabel(self)
                        pixmap = QPixmap(f"{sprites}/{spriteindex.index(item)}")
                        pixlabel.setPixmap(pixmap)
                        pixlabel.setScaledContents(True)
                        pixlabel.setFixedSize(30,10)
                        self.output_attack_x1_layout.addWidget(pixlabel)

            #atk x05
            for item in current_pokemon['pokemon_weakness']:
                for pktype in spriteindex:
                    if item == pktype:
                        pixlabel = QLabel(self)
                        pixmap = QPixmap(f"{sprites}/{spriteindex.index(item)}")
                        pixlabel.setPixmap(pixmap)
                        pixlabel.setScaledContents(True)
                        pixlabel.setFixedSize(30,10)
                        self.output_attack_x05_layout.addWidget(pixlabel)

            #atk x0
            for item in current_pokemon['pokemon_incapable']:
                for pktype in spriteindex:
                    if item == pktype:
                        pixlabel = QLabel(self)
                        pixmap = QPixmap(f"{sprites}/{spriteindex.index(item)}")
                        pixlabel.setPixmap(pixmap)
                        pixlabel.setScaledContents(True)
                        pixlabel.setFixedSize(30,10)
                        self.output_attack_x0_layout.addWidget(pixlabel)
        print()
        clearCurrentPkmon()

        print(rootFolder)
        print(path2glossary)
        print(sprites)

        if self.output_layout.currentIndex() == 0:
            pass
        if self.output_layout.currentIndex() == 1:
            pass

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
