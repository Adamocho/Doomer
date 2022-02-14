from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QWizard, QFileDialog
from PyQt5.QtCore import pyqtSlot, QEvent
from PyQt5 import QtGui
from PyQt5.QtGui import QFont, QIcon, QPixmap
from datetime import datetime
import sys
import subprocess
import os




class App(QWidget):
    def __init__(self):
        super().__init__()
        self.w = 450
        self.h = 450
        self.gamel = {'Ultimate Doom': 'doom.wad', 'Doom II': 'doom2.wad', 'Doom II: TNT Evilution': 'tnt.wad', 'Doom II: Plutonia': 'plutonia.wad'}
                      #'Doom II: Master Levels': 'doom2.wad -file'

        self.masterl = {'': 'wads/attack.wad', 1: 'wads/attack.wad', 2: 'wads/canyon.wad', 3: 'wads/catwalk.wad', 4: 'wads/combine.wad', 5: 'wads/fistula.wad', 6: 'wads/garrison.wad', 7: 'wads/manor.wad',
                        8: 'wads/paradox.wad', 9: 'wads/subspace.wad', 10: 'wads/subterra.wad', 11: 'wads/ttrap.wad', 12: 'wads/virgil.wad', 13: 'wads/minos.wad', 14: 'wads/Bloodsea.wad',
                        15: 'wads/mephisto.wad', 16: 'wads/nessus.wad', 17: 'wads/geryon.wad', 18: 'wads/vesperas.wad', 19: 'wads/blacktwr.wad', 20: 'wads/teeth.wad'}

        self.diffl = {'ITYTD': 1, 'HNTR': 2, 'HMP': 3, 'UV': 4, 'Nightmare': 5}

        self.setGeometry(800, 300, self.w, self.h)
        self.setFixedSize(self.w, self.h)
        self.setWindowTitle("Prboom GUI")
        self.setWindowIcon(QIcon('icons/prbico1.png'))

        self.setFont(QFont('MS Shell Dlg 2', 15))


        #   Now there's some UI
        # Label = canvas for image
        self.l1 = QtWidgets.QLabel(self)                                                                                
        # Assign img to label + scale it to match window size
        self.l1.setPixmap(QPixmap('icons/prbico1.png').scaled(self.w, self.h))

        # wad, skill, warp, nomonsters, fast, record, fastdemo, timedemo, playdemo, nomusic, nomouse, net

        # Game
        self.combo1 = QtWidgets.QComboBox(self)                                                                         
        self.combo1.setGeometry(5, 5, 300, 30)
        self.combo1.addItems(self.gamel)

        # Difficulty
        self.combo2 = QtWidgets.QComboBox(self)                                                                         
        self.combo2.setGeometry(315, 5, 125, 30)
        self.combo2.addItems(self.diffl)
        # Default is HMP
        self.combo2.setCurrentIndex(2)        


        self.cbox1 = QtWidgets.QCheckBox('Record', self)
        self.cbox1.setGeometry(170, 40, 100, 30)

        self.cbox2 = QtWidgets.QCheckBox('Fast', self)
        self.cbox2.setGeometry(40, 80, 100, 30)

        self.cbox3 = QtWidgets.QCheckBox('No Monsters', self)
        self.cbox3.setGeometry(310, 50, 130, 30)

        self.cbox4 = QtWidgets.QCheckBox('No Music', self)
        self.cbox4.setGeometry(335, 110, 110, 30)

        self.cbox5 = QtWidgets.QCheckBox('No Mouse', self)
        self.cbox5.setGeometry(330, 80, 110, 30)

        self.cbox6 = QtWidgets.QCheckBox('Respawn', self)
        self.cbox6.setGeometry(25, 50, 100, 30)

        self.button1 = QtWidgets.QPushButton('Play\Join Game', self)
        self.button1.setGeometry(5, 395, 200, 50)
        self.button1.clicked.connect(self.on_click)

        #self.button2 = QtWidgets.QPushButton('Start Server', self)
        #self.button2.setGeometry(295, 395, 150, 50)
            # UNKOMMENT THIS WHEN YOU FINISH WORKING ON SERVER SCRIPT!!!!!!!!!!!!!
        #self.button2.clicked.connect(self.on_click_server)   

        self.le1 = QtWidgets.QLineEdit(self)
        self.le1.setGeometry(30, 200, 100, 35)
        self.le1.setPlaceholderText('Map')

        self.le2 = QtWidgets.QLineEdit(self)
        self.le2.setGeometry(150, 200, 250, 35)
        self.le2.setPlaceholderText('IP for multiplayer game')

        # Show window with everything declared earlier
        self.show()                                                                                                    

    def on_click(self):              # Create string for bat file and run it
        # print('|', self.le1.text(), '|')
        if self.combo1.currentText() == 'Doom II: Master Levels':
            # batstring = f'prboom-plus -iwad wads/{self.gamel[self.combo1.currentText()]} {self.masterl[int(self.le1.text())]} -skill {str(self.diffl[self.combo2.currentText()])}'
            batstring = f'prboom-plus -iwad wads/{self.gamel[self.combo1.currentText()]} {self.masterl[self.le1.text()]} -skill {str(self.diffl[self.combo2.currentText()])}'

        else:
            # batstring = f'prboom-plus -iwad wads/{self.gamel[self.combo1.currentText()]} -skill {str(self.diffl[self.combo2.currentText()])}'
            batstring = f'prboom-plus -iwad wads/{self.gamel[self.combo1.currentText()]} -skill {str(self.diffl[self.combo2.currentText()])}'


        if self.le1.text() != '' and self.combo1.currentText() != 'Doom II: Master Levels':
            batstring += f' -warp {self.le1.text()}'
        if self.le2.text() != '':
            batstring += f' -net {self.le2.text()}'
        if self.cbox1.isChecked():
            batstring += f' -record {datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}'
        if self.cbox2.isChecked():
            batstring += ' -fast'
        if self.cbox3.isChecked():
            batstring += ' -nomonsters'
        if self.cbox4.isChecked():
            batstring += ' -nomusic'
        if self.cbox5.isChecked():
            batstring += ' -nomouse'
        if self.cbox6.isChecked():
            batstring += ' -respawn'

        # print(batstring)
        with open('batch.bat', "w") as f:
            f.write(batstring)
            f.close()

        print(batstring)
        fullstring = 'C:/Users/oller/Desktop/Games/prboom+/' + batstring
        
        p = subprocess.Popen(fullstring, shell=True, stdout=subprocess.PIPE)

        stdout, stderr = p.communicate()
        #print(stdout, stderr)


    # def on_click_server(self):
    #    print(5)







# If this is the main file
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())