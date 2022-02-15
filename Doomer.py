from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QFont, QIcon, QPixmap
from datetime import datetime
import os
import sys
import threading

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.win_width = 450
        self.win_height = 450

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

        # Window properties
        self.setGeometry(800, 300, self.win_width, self.win_height)
        self.setFixedSize(self.win_width, self.win_height)
        self.setWindowTitle("Doomer")
        self.setWindowIcon(QIcon('icons/prbico1.png'))
        self.setFont(QFont('Consolas', 15))

        #   UI elements
        # Label = canvas for image
        self.label = QtWidgets.QLabel(self)
        # Assign img to label + scale it to match window size
        self.label.setPixmap(QPixmap('icons/prbico1.png').scaled(self.win_width, self.win_height))

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

        # Record checkbox
        self.record_cbx = QtWidgets.QCheckBox('Record', self)
        self.record_cbx.setGeometry(170, 40, 100, 30)

        # Fast checkbox
        self.fast_cbx = QtWidgets.QCheckBox('Fast', self)
        self.fast_cbx.setGeometry(40, 80, 100, 30)

        self.nomo_cbx = QtWidgets.QCheckBox('No Monsters', self)
        self.nomo_cbx.setGeometry(310, 50, 130, 30)

        self.music_cbx = QtWidgets.QCheckBox('Music', self)
        self.music_cbx.setGeometry(335, 110, 110, 30)

        self.mouse_cbx = QtWidgets.QCheckBox('Mouse', self)
        self.mouse_cbx.setGeometry(330, 80, 110, 30)

        self.respawn_cbx = QtWidgets.QCheckBox('Respawn', self)
        self.respawn_cbx.setGeometry(25, 50, 100, 30)

        self.launch_btn = QtWidgets.QPushButton('Play\Join Game', self)
        self.launch_btn.setGeometry(5, 395, 200, 50)
        self.launch_btn.clicked.connect(self.on_click)

        # server logic to implement
        #self.server_btn = QtWidgets.QPushButton('Start Server', self)
        #self.server_btn.setGeometry(295, 395, 150, 50)
        #self.server_btn.clicked.connect(self.on_click_server)   

        self.map_le = QtWidgets.QLineEdit(self)
        self.map_le.setGeometry(30, 200, 100, 35)
        self.map_le.setPlaceholderText('Map')

        self.ip_le = QtWidgets.QLineEdit(self)
        self.ip_le.setGeometry(150, 200, 250, 35)
        self.ip_le.setPlaceholderText('IP for multiplayer game')

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
            self.music_cbx.isChecked(): 'nomusic',
            self.mouse_cbx.isChecked(): 'nomouse',
            self.respawn_cbx.isChecked(): 'respawn'
        }

        # For master levels implementation
        # if self.title_combo.currentText() == 'Doom II: Master Levels':
        #     command = f'prboom-plus \
        #         -iwad wads/{self.titles[self.title_combo.currentText()]} {self.ml_wads[self.map_le.text()]} \
        #         -skill {str(self.diff_lvls[self.diff_combo.currentText()])}'    
        
        cmd = f'prboom-plus \
            -iwad wads/{self.titles[self.title_combo.currentText()]} \
            -skill {str(self.diff_lvls[self.diff_combo.currentText()])}'

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
        print("Server")


# If this is the main file
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())