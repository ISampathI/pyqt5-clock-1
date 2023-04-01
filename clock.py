from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os
tempp=getattr(sys, '_MEIPASS', os.getcwd())
tempp=tempp.replace("\\","/")
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)
class tview(QtWidgets.QLabel):
    def __init__(self,parent=None):
        super(tview, self).__init__(parent)
        self.setAcceptDrops(True)
        self.parent=parent
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.parent.frameGeometry().topLeft()
            event.accept()
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.parent.move(event.globalPos() - self.dragPosition)
            event.accept()
class Ui_Form(object):
    def wexit(self):
        Form.close()
    def showtime(self):
        time = QtCore.QTime.currentTime()
        date=QtCore.QDate.currentDate().toString("yyyy.MM.dd")
        text = time.toString('HH:mm:ss')
        self.label.setText(text)
        self.label_2.setText(date)
    def setupUi(self, Form):
        screen_resolution = app.desktop().screenGeometry()
        swidth, sheight = screen_resolution.width(), screen_resolution.height()
        print(swidth, sheight)
        Form.setObjectName(_fromUtf8("Form"))
        Form.move(swidth-240,0)
        Form.resize(240, 140)
        Form.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label = tview(Form)
        self.label.setGeometry(QtCore.QRect(20,20, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("border-radius: 5px;\n"
"border:2px solid rgba(10,122,196,200); \n"
"background-color: rgba(0,0,0,200);\n"
"color:rgba(10,122,196,200);"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(105, 95, 121, 16))
        self.label_2.setText(_fromUtf8(""))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(1)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.setStyleSheet(_fromUtf8("color:rgba(10,122,196,255);"))
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 23, 16, 16))
        self.pushButton.setStyleSheet(_fromUtf8("background-image: url(%s/data/clo.PNG);\n"
"background-color:rgba(0,0,0,0);")%(tempp))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.wexit)
        
        self.effect = QtWidgets.QGraphicsDropShadowEffect(self.label)
        self.effect.setOffset(QtCore.QPoint(0, 0))
        self.effect.setBlurRadius(30)
        self.effect.setColor(QtGui.QColor(10,122,196))
        self.label.setGraphicsEffect(self.effect)

        time = QtCore.QTime.currentTime()
        date=QtCore.QDate.currentDate().toString("yyyy.MM.dd")
        text = time.toString('HH:mm:ss')
        self.label.setText(text)
        self.label_2.setText(date)
        
        timer = QtCore.QTimer(Form)
        timer.timeout.connect(self.showtime)
        timer.start(1000)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyle('cleanlooks')
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
