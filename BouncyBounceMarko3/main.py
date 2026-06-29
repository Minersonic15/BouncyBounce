import sys
import os
from pathlib import Path

from pynput import keyboard
from pynput.keyboard import Key
import random
from PyQt6.QtCore import Qt, QTimer, QObject
from PyQt6.QtGui import QPixmap, QPainter
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QComboBox, QSpinBox, QLineEdit,
    QRadioButton, QCheckBox, QPushButton, QVBoxLayout, QHBoxLayout
)
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices

#add herobrine

class StartWindow(QWidget):
    def __init__(self):
        self.screen = QApplication.primaryScreen().size()
        super().__init__()
        self.setGeometry(100, 100, 500, 500)
        self.setFixedSize(500,500)
        self.setWindowTitle("BounceyBounce")

        self.Folder = Path('Assets/Images/')
        self.images = [fuh for fuh in self.Folder.iterdir() if fuh.is_file()]
        self.ImAges = []

        for i in range(len(self.images)):
            self.ImAges.append(self.images[i].stem)
        self.ImAges.sort()
        try:
            self.ImAges.remove(".DS_Store")
        except:
            print("you on a windows dawg")


        self.Folder2 = Path('Assets/Sound/')
        self.sounds = [fuh for fuh in self.Folder2.iterdir() if fuh.is_file()]
        self.So = []
        
        for i in range(len(self.sounds)):
            self.So.append(self.sounds[i].stem)
        self.So.sort()
        try:
            self.So.remove(".DS_Store")
            
        except:
            print("you on a windows dawg")
        self.SoUnds = ["None"] + self.So
        print(self.SoUnds)


        self.colour=""
        self.thing = None
        self.MakeBoxes()
        self.SetLayout()
        self.setLayout(self.layout)
        self.show()
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setFocus()
        


    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space and self.thing is not None:
            self.thing.UpdateAll()
            self.StartApp()

    def MakeBoxes(self):
        self.numBox = QSpinBox()
        self.speedBox = QSpinBox() #

        self.imageBox = QComboBox() #
        self.soundBox = QComboBox()
        self.preview = QLabel()
        #self.preview.setFixedSize(50,50)
        self.preview.pixmap().scaled(50, 50)

        self.openFolder = QPushButton("OpenFolder")
        self.openFolder.clicked.connect(self.OpenFinder)

        self.BounceBox = QCheckBox() #

        self.sizeXBox = QSpinBox()
        self.sizeYBox = QSpinBox()


        self.StartButt = QPushButton("Start")
        self.StartButt.clicked.connect(self.StartApp)

        self.ResetButt = QPushButton("Restart")
        self.ResetButt.clicked.connect(self.RestartApp)


        self.numBox.setMinimum(1)
        self.numBox.setMaximum(101)

        self.speedBox.setMinimum(1)
        self.speedBox.setMaximum(10)
        self.speedBox.setValue(3)
        self.Henry()
        self.sizeXBox.setValue(self.screen.width() // 5)
        self.sizeYBox.setValue(self.screen.height() // 5)
        self.BounceBox.setChecked(1)

        #self.fullBox.stateChanged.connect(self.Fulltick)
        self.imageBox.addItems(list(self.ImAges))
        #self.squareBox.stateChanged.connect(self.AutosizeTick)
        self.Cooper()
        self.preview.pixmap().scaled(50, 50)
        self.imageBox.currentTextChanged.connect(self.Cooper)

        self.soundBox.addItems(list(self.SoUnds))

        self.sizeXBox.valueChanged.connect(self.hersonX)
        self.sizeYBox.valueChanged.connect(self.hersonY)

    def Cooper(self):
        pixmap = QPixmap(f"Assets/Images/{self.imageBox.currentText()}.png")
        scaled = pixmap.scaled(
            self.sizeXBox.value() //5,
            self.sizeYBox.value() //5,
        )
        self.preview.setPixmap(scaled)

    def OpenFinder(self):
        QDesktopServices.openUrl(QUrl.fromLocalFile(str(self.Folder.resolve())))

    def hersonX(self):
        pixmap = QPixmap(f"Assets/Images/{self.imageBox.currentText()}.png")
        scaled = pixmap.scaled(
            self.sizeXBox.value() // 5,
            self.sizeYBox.value() // 5,
        )
        self.preview.setPixmap(scaled)
    def hersonY(self):
        pixmap = QPixmap(f"Assets/Images/{self.imageBox.currentText()}.png")
        scaled = pixmap.scaled(
            self.sizeXBox.value() // 5,
            self.sizeYBox.value() // 5,
        )
        self.preview.setPixmap(scaled)
    def RestartApp(self):
        self.newWindow = StartWindow()
        try:
            for i in range(len(self.thing.Labels)):
                self.thing.Labels[i].deleteLater()
            self.thing.deleteLater()
        except:
            print("hi")

        self.close()

        

    def Henry(self):
        self.sizeXBox.setMinimum(1)
        self.sizeXBox.setMaximum(self.screen.width())

        self.sizeYBox.setMinimum(1)
        self.sizeYBox.setMaximum(self.screen.height())


    def SetLayout(self):
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        #self.layout.addWidget(QLabel("yo🤑🤑🤑"))
        self.layout.addWidget(QLabel("Choose yo settings !"))
        self.layout.addWidget(QLabel("*Restart program if new files added*"))

        self.layout.addWidget(QLabel("Choose image and sound:"))
        
        self.spoon = QHBoxLayout()
        self.spoon.addWidget(self.imageBox)
        self.spoon.addWidget(self.preview)

        self.layout.addLayout(self.spoon)

        self.poon = QHBoxLayout()
        self.poon.addWidget(self.openFolder)
        self.poon.addWidget(self.soundBox)
        self.layout.addLayout(self.poon)

        self.layout.addWidget(QLabel("How many?"))
        self.layout.addWidget(self.numBox)

        self.physecks = QHBoxLayout()
        self.physecks.addWidget(QLabel("How fast good sir?"))
        self.physecks.addWidget(self.speedBox)
        self.physecks.addWidget(QLabel("Boingy or no boingy?"))
        self.physecks.addWidget(self.BounceBox)

        self.layout.addLayout(self.physecks)

        self.layout.addWidget(QLabel("Size of ✨✨✨Le Boingaloings✨✨✨"))
        self.Sizoodle = QHBoxLayout()
        self.Sizoodle.addWidget(QLabel("Width🤑"))
        self.Sizoodle.addWidget(self.sizeXBox)
        self.Sizoodle.addWidget(QLabel("Height"))
        self.Sizoodle.addWidget(self.sizeYBox)

        self.layout.addLayout(self.Sizoodle)

        self.layout.addWidget(self.StartButt)
        self.layout.addWidget(self.ResetButt)

    def StartApp(self):
        self.image = self.imageBox.currentText()
        self.sound = self.soundBox.currentText()
        self.speed = self.speedBox.value()
        self.Bounce = self.BounceBox.isChecked()
        self.sizeX = self.sizeXBox.value()
        self.sizeY = self.sizeYBox.value()
        self.nums = self.numBox.value()


        if self.thing is not None:
            self.thing.UpdateAll()

        self.thing = Thingalings(
            Speed=self.speed,
            image=self.image,
            sound=self.sound,
            Bounce= self.Bounce,
            sizeX=self.sizeX,
            sizeY = self.sizeY,
            nums=self.nums

        )

class Thingalings(QObject):
    def __init__(self, Speed, image, sound, Bounce, sizeX, sizeY, nums):
        super().__init__()
        self.speed = Speed
        self.Image =image
        self.screen = QApplication.primaryScreen().size()
        self.sound = sound
        self.timers = []
        self.Labels = []
        self.Bounce = Bounce
        self.numThingies = nums
        self.targetWidth = sizeX
        self.targetHeight = sizeY
        self.NahX = []
        self.NahY = []


        self.column = self.screen.width() // self.targetWidth
        self.row = self.numThingies // self.column

        self.timer = QTimer(self)
        self.timer.timeout.connect(
            self.UpdateFAAHHHHHHIHATETHISIMGOINGINSANEIJUSTCOMPLETELUREMADETHISPROJECTWITHNEARLYNOCHANEGDS)
        self.timer.start(16)
        self.LabellingItFrFr()

        #keyboard_listener = keyboard.Listener(on_press=self.keyPressEvent)
        #keyboard_listener.start()
        #keyboard_listener.join()

    def a(self, key):
        if key == Key.tab:
            for lbl in self.Labels:
                lbl.LabelResetPos()

    def LabellingItFrFr(self):
        for i in range(self.numThingies):
            self.Labels.append(
                Boingaloings(self, self.speed,f"Assets/Images/{self.Image}.png", self.sound, self.targetWidth, self.targetHeight,i)
            )
    def UpdateFAAHHHHHHIHATETHISIMGOINGINSANEIJUSTCOMPLETELUREMADETHISPROJECTWITHNEARLYNOCHANEGDS(self):
        for obj in self.Labels:
            obj.LabelMove()
        if self.Bounce:
            self.CheckBoingaloing()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Tab:
            for lbl in self.Labels:
                lbl.LabelResetPos()

    def CheckBoingaloing(self):
        for i in range(len(self.Labels)):
            for j in range(i + 1, len(self.Labels)):
                Eh = self.Labels[i]
                Bee = self.Labels[j]
                if self.IsBoingaloing(Eh, Bee):
                    self.BOINGALOING(Eh, Bee)

    def IsBoingaloing(self, Eh, Bee):
        return (
                Eh.X < Bee.X + Bee.width() and
                Eh.X + Eh.width() > Bee.X and
                Eh.Y < Bee.Y + Bee.height() and
                Eh.Y + Eh.height() > Bee.Y)

    def BOINGALOING(self, Eh, Bee):
        overlapX = min(Eh.X + Eh.width(), Bee.X + Bee.width()) - max(Eh.X, Bee.X)
        overlapY = min(Eh.Y + Eh.height(), Bee.Y + Bee.height()) - max(Eh.Y, Bee.Y)
        if overlapX < overlapY:
            Eh.DirX, Bee.DirX = Bee.DirX, Eh.DirX
        else:
            Eh.DirY, Bee.DirY = Bee.DirY, Eh.DirY

        Eh.move(Eh.X, Eh.Y)
        Bee.move(Bee.X, Bee.Y)
        Eh.sound.play()

    def UpdateAll(self):
        for lbl in self.Labels:
            lbl.close()
            lbl.deleteLater()

        self.Labels.clear()
        self.deleteLater()

class Boingaloings(QWidget):
    def __init__(self, papa,Speed, image, sound, sizeX, sizeY, j):
        super().__init__()
        self.parent = papa
        self.speed = Speed
        self.speeds = [-self.speed, self.speed]
        self.screen = QApplication.primaryScreen().size()
        self.Image = image
        self.sound = QSoundEffect()
        self.sound.setSource(QUrl.fromLocalFile(f"Assets/Sound/{sound}.wav"))
        self.sound.setVolume(1)
        self.targetWidth = sizeX
        self.targetHeight = sizeY
        self.Num = j
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.WindowStaysOnTopHint)

        self.CurrentColomn = j % self.parent.column
        self.CurRow = j // self.parent.column

        self.xPos = self.CurrentColomn * self.targetWidth
        self.yPos = self.CurRow * self.targetHeight

        self.setWindowTitle("Bouncy " + self.Image)
        self.setFixedSize(self.targetWidth, self.targetHeight)
        self.DirX = random.choice(self.speeds)
        self.DirY = random.choice(self.speeds)
        #self.SpawnFella()
        self.X = random.randrange(0, self.screen.width() - self.width())
        self.Y = random.randrange(30, self.screen.height() - self.height())

        self.pixmap = QPixmap(self.Image)

        self.show()
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setFocus()


    def SpawnFella(self): #MARKO REMEMBER THAT TS IS BRPLEN BECAUSE IT ONLY CHECKS PREVIOUS NOT ALL, MARKO Add A LIST THING so thAT it keeps TraCK OF ALLL
        if self.Num == 0:
            self.X = random.randrange(0, self.screen.width() - self.width())
            self.Y = random.randrange(30, self.screen.height() - self.height())
            self.parent.NahX.append(list(range(self.X, self.X + self.height())))
            self.parent.NahY.append(list(range(self.Y, self.Y + self.height())))
            print(self.parent.NahX)
            print(self.parent.NahY)
            self.move(self.X, self.Y)
            return

        #marko, the 2 lists have the no areas for the Xs and Ys. the indexes are the same. do something with that, like make sure it takes out BOTH of those from the list, maybe something that gens 2 numbers at once
        #Only problem is it hsould be able to gen numbers from the nono list, but only when its 1 nono number, if its 2 from same index it should block.
        #THINK mark, THINK.
        #while any(self.X in sublist for sublist in self.parent.NahX):
        pingas = False
        while not pingas:
            self.X = random.randrange(0, self.screen.width() - self.width())
            self.Y = random.randrange(30, self.screen.height() - self.height())
            self.rangeX = set(range(self.X, self.X + self.width()))
            self.rangeY = set(range(self.Y, self.Y + self.height()))

            ouegh = False
            for i, j in zip(self.parent.NahX, self.parent.NahY):
                if self.rangeX & set(i) and self.rangeY & set(j): #ts func links the variables, its like making them one kinda i think. you
                    ouegh = True
                    break
                    
            if not ouegh:
                pingas = True

        self.parent.NahX.append(list(range(self.X, self.X + self.width())))
        self.parent.NahY.append(list(range(self.Y, self.Y + self.height())))

        self.move(self.X,self.Y)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.width(), self.height(), self.pixmap)

    def LabelFUCK(self):
        self.X = self.xPos
        self.Y = self.yPos+35
        self.DirX = self.parent.speed
        self.DirY = self.parent.speed

    def LabelResetPos(self): #marko fix this with the similar stuff from spawn fella or something. Im so damn tired bro i slept at 2am last night dawg ahgaskjdgasdvoiubasehjvkadfkvhasl calculator
        self.DirX *= random.choice([-1,1])
        self.DirY *= random.choice([-1,1])
        self.move(self.X, self.Y)
        summonded = False
        try:
            while not summonded:
                self.nuX = random.randint(0, self.screen.width() - self.width())
                self.nuY = random.randint(30, self.screen.height() - self.height())
                summonded = True
                for Gangalangs in self.parent.Labels:
                    if Gangalangs is self:
                        continue
                    if (self.nuX < Gangalangs.X + Gangalangs.width() and
                            self.nuX + self.width() > Gangalangs.X and
                            self.nuY < Gangalangs.Y + Gangalangs.height() and
                            self.nuY + self.height() > Gangalangs.Y):
                        summonded = False
                        break

            self.X = self.nuX
            self.Y = self.nuY
            self.move(self.X, self.Y)
        except:
            self.move(self.X, self.Y)
            return

    def IsBoingaloing(self, Eh, Bee):
        return (
                Eh.X < Bee.X + Bee.width() and
                Eh.X + Eh.width() > Bee.X and
                Eh.Y < Bee.Y + Bee.height() and
                Eh.Y + Eh.height() > Bee.Y)
    def LabelMove(self):
        self.X += self.DirX
        self.Y += self.DirY
        if self.X < -self.speed + 1 or self.X > self.screen.width() - self.width() + self.speed - 1:
            self.LabelResetPos()
        elif self.X <= 0 or self.X >= self.screen.width() - self.width():
            self.DirX *= -1
            self.sound.play()

        if self.Y < 34 - self.speed or self.Y > self.screen.height() - self.height() + self.speed - 1:
            self.LabelResetPos()
        elif self.Y < 35 or self.Y >= self.screen.height() - self.height():
            self.DirY *= -1
            self.sound.play()
        
        self.move(self.X,self.Y)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StartWindow()
    sys.exit(app.exec())