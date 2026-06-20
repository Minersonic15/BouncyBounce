import sys
from PyQt6.QtGui import QPixmap, QInputDevice
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QSpinBox, QLineEdit, QRadioButton, QCheckBox, \
    QPushButton
from PyQt6.QtCore import QTimer, Qt
import random
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt6.QtMultimedia import QSoundEffect

#add herobrine

class StartWindow(QWidget):
    def __init__(self):
        self.screen = QApplication.primaryScreen().size()
        super().__init__()
        self.setGeometry(100, 100, 500, 500)
        self.setFixedSize(500,500)
        self.setWindowTitle("BounceyBounce")

        self.sound="Bok"
        self.colour=""

        self.MakeBoxes()
        self.SetLayout()
        self.setLayout(self.layout)
        self.show()
        #self.StartApp(self.speed, self.num, self.rows, self.image, self.sound, self.colour, self.Bounce, self.sizeX, self.sizeY, self.WinsizeX, self.WinsizeY)

    def MakeBoxes(self):
        self.numBox = QSpinBox()
        self.rowsBox = QSpinBox() #
        self.speedBox = QSpinBox() #

        self.imageBox = QComboBox() #
        self.soundBox = QComboBox()
        self.colourBox = QComboBox()

        self.BounceBox = QCheckBox() #

        self.AutosizeBox = QCheckBox()

        self.sizeXBox = QSpinBox()
        self.sizeYBox = QSpinBox()

        self.fullBox = QCheckBox()
        self.WinsizeXBox = QSpinBox()
        self.WinsizeYBox = QSpinBox()

        self.StartButt = QPushButton("Start")
        self.StartButt.clicked.connect(self.StartApp)

        self.numBox.setMinimum(1)
        self.numBox.setMaximum(101)
        self.rowsBox.setMinimum(1)
        self.rowsBox.setMaximum(101)
        #self.numBox.valueChanged.connect(self.updateRows)
        #self.updateRows()

        self.speedBox.setMinimum(0)
        self.speedBox.setMaximum(10)
        self.speedBox.setValue(3)
        self.Henry()
        self.BounceBox.setChecked(True)

        self.Henrique()
        #self.fullBox.stateChanged.connect(self.Fulltick)

        self.AutosizeBox.setChecked((True))
        self.AutosizeBox.stateChanged.connect(self.AutosizeTick)

        #self.squareBox.stateChanged.connect(self.AutosizeTick)

        self.imageBox.addItems([
            "Nio",
            "CHease",
            "Easter",
            "HENRIQUE",
            "LuhRX",
            "Niche",
            "Tank",
            "Toaster"
        ])
    def updateRows(self):
        #self.rowsBox.setMaximum(self.numBox.value())
        return

    def AutosizeTick(self):
        if self.AutosizeBox.isChecked():
            self.sizeXBox.setMinimum(0)
            self.sizeXBox.setMaximum(0)
            self.sizeXBox.setValue(0)

            self.sizeYBox.setMinimum(0)
            self.sizeYBox.setValue(0)
            self.sizeYBox.setMaximum(0)
        else:
            self.Henry()
    def Fulltick(self):
        if self.fullBox.isChecked():
            self.WinsizeXBox.setMinimum(0)
            self.WinsizeXBox.setMaximum(0)
            self.WinsizeXBox.setValue(0)

            self.WinsizeYBox.setMinimum(0)
            self.WinsizeYBox.setValue(0)
            self.WinsizeYBox.setMaximum(0)
        else:
            self.Henrique()
    def Henrique(self):
        self.WinsizeXBox.setMaximum(self.screen.width())
        self.WinsizeXBox.setMinimum(1)

        self.WinsizeYBox.setMaximum(self.screen.height())
        self.WinsizeYBox.setMinimum(1)

        self.WinsizeXBox.setValue(self.screen.width() // 2)
        self.WinsizeYBox.setValue(self.screen.height() // 2)

    def Henry(self):
        self.sizeXBox.setMinimum(1)
        try:
            self.sizeXBox.setMaximum(self.WinsizeXBox.value() // (self.numBox.value() // self.rowsBox.value()))
        except:
            self.sizeXBox.setMaximum(self.WinsizeXBox.value() // (self.rowsBox.value() // self.numBox.value()))

        self.sizeYBox.setMinimum(1)
        self.sizeYBox.setMaximum(self.WinsizeYBox.value() // self.rowsBox.value())

    def SetLayout(self):
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout.addWidget(QLabel("yo🤑🤑🤑"))
        self.layout.addWidget(QLabel("Choose yo settings Dawgchach!!"))

        self.layout.addWidget(QLabel("Choose image:"))
        self.layout.addWidget(self.imageBox)

        self.layout.addWidget(QLabel("Number stuff idk im not goodf at math:"))
        self.numbers = QHBoxLayout()
        self.numbers.addWidget(QLabel("How many, choomba?"))
        self.numbers.addWidget(self.numBox)
        self.numbers.addWidget(QLabel("Rows i ask, ROWS!!"))
        self.numbers.addWidget(self.rowsBox)

        self.layout.addLayout(self.numbers)

        self.physecks = QHBoxLayout()
        self.physecks.addWidget(QLabel("How fast good sir?"))
        self.physecks.addWidget(self.speedBox)
        self.physecks.addWidget(QLabel("Boingy or no boingy?"))
        self.physecks.addWidget(self.BounceBox)
        self.layout.addLayout(self.physecks)

        self.layout.addWidget(QLabel("Size of ✨✨✨Le Boingaloings✨✨✨"))

        self.Sizoodle = QHBoxLayout()
        self.Sizoodle.addWidget(QLabel("Auto Size3000:"))
        self.Sizoodle.addWidget(self.AutosizeBox)

        self.Sizoodle.addWidget(QLabel("Width🤑"))
        self.Sizoodle.addWidget(self.sizeXBox)
        self.Sizoodle.addWidget(QLabel("Height"))
        self.Sizoodle.addWidget(self.sizeYBox)

        self.layout.addLayout(self.Sizoodle)

        self.layout.addWidget(QLabel("widnow sisze :D"))

        self.Winsoozle = QHBoxLayout()
        self.Winsoozle.addWidget(QLabel("Full"))
        self.Winsoozle.addWidget(self.fullBox)
        self.Winsoozle.addWidget(QLabel("WindowWidth"))
        self.Winsoozle.addWidget(self.WinsizeXBox)
        self.Winsoozle.addWidget(QLabel("WindowHeitght"))
        self.Winsoozle.addWidget(self.WinsizeYBox)

        self.layout.addLayout(self.Winsoozle)

        self.layout.addWidget(self.StartButt)

    def StartApp(self):
        self.image = self.imageBox.currentText()
        self.num = self.numBox.value()
        self.rows = self.rowsBox.value()
        self.num *= self.rows
        self.speed = self.speedBox.value()
        self.Bounce = self.BounceBox.isChecked()
        self.sizeX = self.sizeXBox.value()
        self.sizeY = self.sizeYBox.value()
        self.winSizeX = self.WinsizeXBox.value()
        self.winSizeY = self.WinsizeYBox.value()
        self.tikitiki = self.fullBox.isChecked()

        MainWindow(
            Speed=self.speed,
            Num=self.num,
            Rows=self.rows,
            image=self.image,
            sound=self.sound,
            colour=self.colour,
            Bounce= self.Bounce,
            sizeX=self.sizeX,
            sizeY = self.sizeY,
            WinsizeX = self.winSizeX,
            WinsizeY = self.winSizeY,
            Tikitiki =self.tikitiki
        )


class MainWindow(QWidget):
    def __init__(self, Speed, Num, Rows, image, sound, colour, Bounce, sizeX, sizeY, WinsizeX, WinsizeY,Tikitiki):
        super().__init__()
        self.speed = Speed
        self.speeds = [-self.speed, self.speed]
        self.numThingies = Num
        self.rows = Rows
        self.colomn = self.numThingies // self.rows
        self.Image = image
        #self.sound = QSoundEffect()
        #self.sound.setSource(f"Assets/{sound}.wav")
        #self.sound.setVolume(0.5)
        self.Bounce = Bounce
        self.timers = []
        self.Labels = []
        self.Sizalize = (sizeX == 0 and sizeY == 0)
        self.tikitikitiki = Tikitiki


        screen = QApplication.primaryScreen().size()


        #if self.winSizalize:
            #self.setGeometry(100, 100, int(screen.width() // 2), int(screen.height() // 2))
            #self.setGeometry(100, 100, screen.width(), screen.height())
        #else:
            #self.setGeometry(100, 100,WinsizeX,WinsizeY)
        if sizeX == 0:
            self.targetWidth = int(self.width() // self.colomn-1)
        else:
            self.targetWidth = sizeX
        if sizeY == 0:
            self.targetHeight = int(self.height() // self.rows - 1)
        else: self.targetHeight = sizeY

        try:
            self.setStyleSheet(f"background-color: {colour};")
        except:
            return


        self.setWindowTitle("Bouncy " + self.Image)

        self.LabellingItFrFr()
        self.show()
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setFocus()

        self.timer = QTimer()
        self.timer.timeout.connect(self.UpdateFAAHHHHHHIHATETHISIMGOINGINSANEIJUSTCOMPLETELUREMADETHISPROJECTWITHNEARLYNOCHANEGDS)
        self.timer.start(16)
        if self.tikitikitiki:
            self.showFullScreen()
    def LabellingItFrFr(self):
        for i in range(self.numThingies):
            self.Labels.append(
                BouncyThing(self, f"Assets/Images/{self.Image}.png", self.speed, self.targetWidth, self.targetHeight, i)
            )
            #self.Labels.append(
                #BouncyThing(self, f"Assets/Toaster.png", self.speed, self.targetWidth, self.targetHeight, i+1)
            #)



    def UpdateFAAHHHHHHIHATETHISIMGOINGINSANEIJUSTCOMPLETELUREMADETHISPROJECTWITHNEARLYNOCHANEGDS(self):
        for obj in self.Labels:
            obj.LabelMove()
        if self.Bounce == True:
            self.CheckBoingaloing()

    def CheckBoingaloing(self):
        for i in range(len(self.Labels)):
            for j in range(i + 1, len(self.Labels)):
                Eh = self.Labels[i]
                Bee = self.Labels[j]
                if self.IsBoingaloing(Eh, Bee):
                    self.BOINGALOING(Eh, Bee)

    def IsBoingaloing(self, Eh, Bee):
        return (
                Eh.X < Bee.X + Bee.label.width() and
                Eh.X + Eh.label.width() > Bee.X and
                Eh.Y < Bee.Y + Bee.label.height() and
                Eh.Y + Eh.label.height() > Bee.Y)

    def BOINGALOING(self, Eh, Bee):
        overlapX = min(Eh.X + Eh.label.width(), Bee.X + Bee.label.width()) - max(Eh.X, Bee.X)
        overlapY = min(Eh.Y + Eh.label.height(), Bee.Y + Bee.label.height()) - max(Eh.Y, Bee.Y)
        if overlapX < overlapY:
            Eh.DirX, Bee.DirX = Bee.DirX, Eh.DirX
            # if Eh.X < Bee.X:
            # Eh.X -= overlapX // 2
            # Bee.X += overlapX // 2
            # else:
            # Eh.X += overlapX // 2
            # Bee.X -= overlapX // 2
        else:
            Eh.DirY, Bee.DirY = Bee.DirY, Eh.DirY
            # if Eh.Y < Bee.Y:
            # Eh.Y -= overlapY // 2
            # Bee.Y += overlapY // 2
            # else:
            # Eh.Y += overlapY // 2
            # Bee.Y -= overlapY // 2

        Eh.label.move(Eh.X, Eh.Y)
        Bee.label.move(Bee.X, Bee.Y)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Tab:
            for lbl in self.Labels:
                lbl.LabelResetPos()

        elif event.key() == Qt.Key.Key_Shift:
            for lbl in self.Labels:
                lbl.LabelFUCK()
        elif event.key() == Qt.Key.Key_Escape:
            self.close()
class BouncyThing:
    def __init__(self, parent, image, speed, width, height,j):
        self.parent = parent
        self.label = QLabel(parent)

        self.CurrentColomn = j % self.parent.colomn
        self.CurRow = j // self.parent.colomn

        self.xPos = self.CurrentColomn * width
        self.yPos = self.CurRow * height

        self.DirX = random.choice([-speed, speed])
        self.DirY = random.choice([-speed, speed])

        pixmap = QPixmap(image)
        self.label.setPixmap(pixmap.scaled(width, height))
        self.label.resize(width, height)

        summonded = False
        if self.parent.Sizalize:
            self.LabelFUCK()
        else:
            while not summonded:
                self.X = random.randint(0, parent.width() - width)
                self.Y = random.randint(0, parent.height() - height)
                summonded = True

                for Gangalangs in parent.Labels:
                    if (self.X < Gangalangs.X + Gangalangs.label.width() and
                            self.X + width > Gangalangs.X and
                            self.Y < Gangalangs.Y + Gangalangs.label.height() and
                            self.Y + height > Gangalangs.Y):
                        summonded = False
                        break

        self.label.move(self.X, self.Y)
        self.soundCooldown = 0


    def LabelResetPos(self):
        self.DirX *= random.choice([-1,1])
        self.DirY *= random.choice([-1,1])
        summonded = False
        tries = 0
        try:
            while not summonded and tries < 1000:
                self.nuX = random.randint(0, self.parent.width() - self.label.width())
                self.nuY = random.randint(0, self.parent.height() - self.label.height())
                summonded = True
                tries += 1
                for Gangalangs in self.parent.Labels:
                    if Gangalangs is self:
                        continue
                    if (self.nuX < Gangalangs.X + Gangalangs.label.width() and
                            self.nuX + self.label.width() > Gangalangs.X and
                            self.nuY < Gangalangs.Y + Gangalangs.label.height() and
                            self.nuY + self.label.height() > Gangalangs.Y):
                        summonded = False
                        break
                if summonded:
                    self.X = self.nuX
                    self.Y = self.nuY
                    self.label.move(self.X, self.Y)

            #if self.parent.Sizalize:
                #self.LabelFUCK()
            #else:
                #summonded = False
                #while not summonded:
                    #self.X = random.randint(0, self.parent.width() - self.label.width())
                    #self.Y = random.randint(0, self.parent.height() - self.label.height)
                    #summonded = True

                    #for Gangalangs in self.parent.Labels:
                        #if (self.X < Gangalangs.X + Gangalangs.label.width() and
             #                   self.X + self.label.width() > Gangalangs.X and
                    #            self.Y < Gangalangs.Y + Gangalangs.label.height() and
                   #             self.Y + self.label.height() > Gangalangs.Y):
                    #        summonded = False

        except:
            self.label.move(self.X, self.Y)
            return

    def LabelFUCK(self):
        self.X = self.xPos
        self.Y = self.yPos
        self.DirX = self.parent.speed
        self.DirY = self.parent.speed


    def LabelMove(self):
        self.X += self.DirX
        self.Y += self.DirY
        if self.soundCooldown > 0:
            self.soundCooldown -= 1
        if self.X < -self.parent.speed + 1 or self.X > self.parent.width() - self.label.width() + self.parent.speed - 1:
            self.LabelResetPos()



        elif self.X <= 0 or self.X >= self.parent.width() - self.label.width():
            self.DirX *= -1
            try:
                if self.soundCooldown == 0:
                    self.parent.sound.play()
                    self.soundCooldown = 8
            except:
                pass

        if self.Y < -self.parent.speed + 1 or self.Y > self.parent.height() - self.label.height() + self.parent.speed - 1:
            self.LabelResetPos()



        elif self.Y <= 0 or self.Y >= self.parent.height() - self.label.height():
            self.DirY *= -1
            try:
                if self.soundCooldown == 0:
                    self.parent.sound.play()
                    self.soundCooldown = 8
            except:
                pass

        self.label.move(self.X, self.Y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StartWindow()
    sys.exit(app.exec())
