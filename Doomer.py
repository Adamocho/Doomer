#!/usr/bin/python3

from distutils.fancy_getopt import wrap_text
from textwrap import wrap
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout
from PyQt5.QtGui import QFont, QIcon, QPixmap
from datetime import datetime
import os
import sys
import threading

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.width = 450
        self.height = 450

        self.titles = {
            'Ultimate Doom': 'doom.wad',
            'Doom II': 'doom2.wad',
            'Doom II: TNT Evilution': 'tnt.wad',
            'Doom II: Plutonia': 'plutonia.wad'
        }
        #'Doom II: Master Levels': 'doom2.wad -file'

        self.ml_wads = {
            '': 'wads/attack.wad',
            1: 'wads/attack.wad',
            2: 'wads/canyon.wad',
            3: 'wads/catwalk.wad',
            4: 'wads/combine.wad',
            5: 'wads/fistula.wad',
            6: 'wads/garrison.wad',
            7: 'wads/manor.wad',
            8: 'wads/paradox.wad',
            9: 'wads/subspace.wad',
            10: 'wads/subterra.wad',
            11: 'wads/ttrap.wad',
            12: 'wads/virgil.wad',
            13: 'wads/minos.wad',
            14: 'wads/Bloodsea.wad',
            15: 'wads/mephisto.wad',
            16: 'wads/nessus.wad',
            17: 'wads/geryon.wad',
            18: 'wads/vesperas.wad',
            19: 'wads/blacktwr.wad',
            20: 'wads/teeth.wad'
        }

        self.diff_lvls = {
            'ITYTD': 1,
            'HNTR': 2,
            'HMP': 3,
            'UV': 4,
            'Nightmare': 5
        }

        self.complevels = {
            'default' : -1,     # Current Prboom-plus
            'doom_12' : 0,      # Partial (improved) emulation of Doom.exe v1.2
            'doom_1666' : 1,    # Partial emulation of Doom.exe/Doom2.exe v1.666
            'doom2_19' : 2,     # Emulates the original Doom.exe v1.9 & Doom2's doom2.exe v1.9
            'ultdoomy' : 3,     # Emulates Ultimate Doom v1.9 and Doom95
            'finaldoom' : 4,    # Emulates Final Doom's doom2.exe
            'dosdoom' : 5,      # Emulates Dosdoom .47
            'tasdoom' : 6,      # Emulates Tasdoom.exe
            'boom' : 7,         # Emulates Boom's compatibility mode
            'boom_201' : 8,     # Emulates Boom v2.01
            'boom_202' : 9,     # Emulates Boom v2.02
            'lxdoom_1' : 10,    # Emulates LxDoom v1.4.x
            'mbf' : 11,         # Emulates MBF
            'prboom_1' : 12,    # Emulates PrBoom v2.03beta
            'prboom_2' : 13,    # Emulates PrBoom v2.1.0
            'prboom_3' : 14,    # Emulates PrBoom v2.1.1-2.2.6
            'prboom_4' : 15,    # Emulates PrBoom v2.3.x
            'prboom_5' : 16,    # Emulates PrBoom v2.4.0
            'prboom_6' : 17,    # Latest PrBoom-plus
        }

        # Window properties
        self.setGeometry(800, 300, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.setWindowTitle("Doomer")
        self.setWindowIcon(QIcon('img/prbico1.png'))
        self.setFont(QFont('Consolas', 15))

        #   UI elements
        # Label = canvas for image
        self.label = QtWidgets.QLabel(self)
        # Assign img to label + scale it to match window size
        self.label.setPixmap(QPixmap('img/dosguy0.png').scaled(self.width, self.height))

        # wad, skill, warp, nomonsters, fast, record, fastdemo, timedemo, playdemo, nomusic, nomouse, net

        # Game title combo box
        self.title_combo = QtWidgets.QComboBox(self)
        self.title_combo.setGeometry(5, 5, 300, 30)
        self.title_combo.addItems(self.titles)

        # Difficulty combo box
        self.diff_combo = QtWidgets.QComboBox(self)
        self.diff_combo.setGeometry(315, 5, 125, 30)
        self.diff_combo.addItems(self.diff_lvls)
        # HMP is set by default
        self.diff_combo.setCurrentIndex(2)

        # Complevel combo box
        self.complvl_combo = QtWidgets.QComboBox(self)
        self.complvl_combo.setGeometry(315, 40, 125, 30)
        self.complvl_combo.addItems(self.complevels)
        # HMP is set by default
        self.complvl_combo.setCurrentIndex(0)

        """ Checkboxes """
        # Record checkbox
        self.record_cbx = QtWidgets.QCheckBox('Record demo', self)
        self.record_cbx.setGeometry(250, 405, 150, 30)

        # Fast checkbox
        self.fast_cbx = QtWidgets.QCheckBox('Fast', self)
        self.fast_cbx.setGeometry(300, 265, 100, 30)

        self.nomo_cbx = QtWidgets.QCheckBox('No Monsters', self)
        self.nomo_cbx.setGeometry(300, 295, 130, 30)

        self.music_cbx = QtWidgets.QCheckBox('Music', self)
        self.music_cbx.setGeometry(300, 325, 110, 30)
        self.music_cbx.setChecked(True)

        self.mouse_cbx = QtWidgets.QCheckBox('Mouse', self)
        self.mouse_cbx.setGeometry(300, 355, 110, 30)
        self.mouse_cbx.setChecked(True)

        self.respawn_cbx = QtWidgets.QCheckBox('Respawn', self)
        self.respawn_cbx.setGeometry(300, 235, 100, 30)

        """ Line edits """

        self.map_le = QtWidgets.QLineEdit(self)
        self.map_le.setGeometry(30, 200, 100, 35)
        self.map_le.setPlaceholderText('Map')

        self.ip_le = QtWidgets.QLineEdit(self)
        self.ip_le.setGeometry(150, 200, 250, 35)
        self.ip_le.setPlaceholderText('IP for multiplayer')

        """ Buttons """

        self.launch_btn = QtWidgets.QPushButton('Play\Join Game', self)
        self.launch_btn.setGeometry(5, 395, 185, 50)
        self.launch_btn.clicked.connect(self.on_click)
        
        # Host server button
        self.server_btn = QtWidgets.QPushButton('Host Server', self)
        self.server_btn.setGeometry(5, 345, 150, 50)
        self.server_btn.clicked.connect(self.on_click_server)   

        self.show()


    def on_click(self):
        """Implements logic for the UI

        Takes no arguments
        Results in creating and sending a command to the shell
        """

        settings = {
            self.record_cbx.isChecked(): f'record {datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}',
            self.fast_cbx.isChecked(): 'fast',
            self.nomo_cbx.isChecked(): 'nomonsters',
            not self.music_cbx.isChecked(): 'nomusic',
            not self.mouse_cbx.isChecked(): 'nomouse',
            self.respawn_cbx.isChecked(): 'respawn'
        }

        # For master levels implementation
        # if self.title_combo.currentText() == 'Doom II: Master Levels':
        #     command = f'prboom-plus \
        #         -iwad wads/{self.titles[self.title_combo.currentText()]} {self.ml_wads[self.map_le.text()]} \
        #         -skill {str(self.diff_lvls[self.diff_combo.currentText()])}'    
        
        cmd = f'prboom-plus \
            -iwad wads/{self.titles[self.title_combo.currentText()]} \
            -skill {str(self.diff_lvls[self.diff_combo.currentText()])} \
            -complevel {self.complevels[self.complvl_combo.currentText()]}'

        # Apply chosen settings
        if (warp := self.map_le.text()): # and self.title_combo.currentText() != 'Doom II: Master Levels':
            cmd += f' -warp {warp}'
        if (net := self.ip_le.text()):
            cmd += f' -net {net}'

        for key in settings:
            if key:
                cmd += ' -' + settings[key]

        # Execute final command string
        # Additionaly create a thread so that it desn't freeze the app
        def exec_cmd(cmd, *arvs):
            """Executes shell command, used for threading"""
            os.system(cmd)

        threading.Thread(target=exec_cmd, args=(cmd, 1)).start()


    # Server logic NOT IMPLEMENTED yet
    def on_click_server(self):
        os.system("explorer.exe")


# If this is the main file
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())