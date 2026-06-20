import sys
from cProfile import label

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget ,QLabel
from PyQt6.QtCore import QTimer
from PyQt6.QtCore import Qt
import random
from playsound3 import playsound

def window():
    #244:6
    #2560
    timers = []
    Freaky = 1
    speed = 3
    speeds = [-speed, speed]
    numThingies = 100000
    rows = 100
    colomn = numThingies // rows
    name= 9
    Images = [
            #"LuhRX",
            #"Tank",
            #"HENRIQUE",
             "Nio",
            #"Toaster",
        #"CHease",
        #"Vatican"
        #"Marko",
        #"Harison",
        #"Deveron"
            ]
    BounceSounds = [
            #"Click",
            "Bok",
            #"Boing"
        ]
    Labels = []


    app = QApplication(sys.argv)
    MaxScreen = app.primaryScreen().size()
    window = QWidget()
    window.setWindowTitle("Bouncy " + Images[0])
    window.setGeometry(100, 100, int(MaxScreen.width() // 2), int(MaxScreen.height() // 2))


    #window.setStyleSheet("background-color: ;")
    if Freaky == 1:
        targetWidth = int(window.width() // colomn-1)
        targetHeight = int(window.height() // rows-1)
        #targetHeight = targetWidth
        #targetWidth = targetHeight
    elif Freaky == 2:
        targetWidth = int(MaxScreen.width() // colomn - 1)
        targetHeight = int(MaxScreen.height() // rows-1)
        #targetHeight = targetWidth
    else:
        targetWidth = int(MaxScreen.width() // 3)
        targetHeight = int(MaxScreen.height() // 3)


    def LabelMaker(Name, Image, j):

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        DirX = random.choice(speeds)
        DirY = random.choice(speeds)

        label = QLabel(parent=window)
        pixmap = QPixmap(Image)

        scaled = pixmap.scaled(targetWidth, targetHeight)
        label.setPixmap(scaled)
        label.resize(scaled.size())

        X = random.randint(0, window.width() - label.width())
        Y = random.randint(0, window.height() - label.height())

        CurrentColomn = j % colomn
        CurRow = j // colomn

        xPos = CurrentColomn * label.width()
        yPos = CurRow * label.height()

        label.move(X, Y)


        def LabelResetPos():
            nonlocal X, Y, DirX, DirY
            DirX *= random.choice([-1,1])
            DirY *= random.choice([-1,1])
            try:
                X = random.randint(0, window.width() - label.width())
                label.move(X, Y)
            except:
                label.move(X, Y)
                return
            try:
                Y = random.randint(0, window.height() - label.height())
                label.move(X, Y)
            except:
                label.move(X, Y)
                return



        def LabelFUCK():
            nonlocal X, Y, DirX, DirY, xPos, yPos,j

            X = xPos
            Y = yPos
            DirX = speed
            DirY = speed

        Labels.append({
            "reset": LabelResetPos,
            "fuck": LabelFUCK
        })

        def LabelMove():
            nonlocal  X, Y, DirX, DirY

            X += DirX
            Y += DirY
            if X < -speed+1 or X > window.width() - label.width() + speed-1:
                LabelResetPos()
                print("X Out")
            elif X <= 0 or X >= window.width() - label.width():
                DirX *= -1
                #playsound(f"Assets/{BounceSounds[0]}.wav", block=False)

            if Y < -speed+1 or Y > window.height() - label.height() + speed-1:
                LabelResetPos()
                print ("Y out")
            elif Y <= 0 or Y >= window.height() - label.height():
                DirY *= -1
                #playsound(f"Assets/{BounceSounds[0]}.wav", block=False)

            label.move(X, Y)

        timer = QTimer()
        timer.timeout.connect(LabelMove)
        timer.start(16)
        timers.append(timer)

    items = len(Images)
    for i in range(numThingies):
        if numThingies <= items:
            ImageFile = Images[i]
        else:
            ImageFile = Images[0]
        LabelMaker(name, f"Assets/{ImageFile}.png", i)

    def butten(event):
        print("Butten")
        try:
            if event.key() == Qt.Key.Key_A:
                for lbl in Labels:
                    lbl["reset"]()

            elif event.key() == Qt.Key.Key_S:
                for lbl in Labels:
                    lbl["fuck"]()
        except AttributeError:
            return

    window.keyPressEvent = butten
    window.show()
    window.setFocus()
    app.exec()
window()
