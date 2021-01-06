
from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Robotics\Desktop\ingilizceturkcesozluk-main\ingilizceturkcesozluk-main\SÖZLÜK.accdb;')
cursor = conn.cursor()
cursor.execute('select * from IngilizceTurkceTablosu')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))

        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:#5aa57d;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)

        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 744, 600))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(self.filtrele)
        self.lineEdit.setStyleSheet("background-color:white;")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.goster_button)
        self.pushButton.setStyleSheet("background-color:white;")
        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.clicked.connect(self.temizle)
        self.pushButton2.setStyleSheet("background-color:white;")
        self.horizontalLayout_3.addWidget(self.pushButton2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)

        self.radioButton.setMinimumSize(QtCore.QSize(200, 25))
        self.radioButton.setMaximumSize(QtCore.QSize(200, 25))
        self.radioButton.setChecked(True)
        self.radioButton.setText("İngilizce-->Türkçe")
        self.radioButton.durum="ingilizceTurkce"
        self.radioButton.clicked.connect(self.temizle_radio)


        self.horizontalLayout_5.addWidget(self.radioButton)

        self.radioButton2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton2.setText("Türkçe-->İngilizce")
        self.horizontalLayout_5.addWidget(self.radioButton2)
        self.radioButton2.durum = "Turkceingilizce"
        self.radioButton2.clicked.connect(self.temizle_radio)

        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setMinimumSize(QtCore.QSize(350, 350))
        self.listWidget.setMaximumSize(QtCore.QSize(350, 350))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemClicked.connect(self.goster)
        self.listWidget.setStyleSheet("background-color:white;")

        cursor.execute('select SozcukAdi from IngilizceTurkceTablosu')
        for row in cursor.fetchall():
            self.listWidget.addItem(row[0])

        self.horizontalLayout.addWidget(self.listWidget)

        self.plaintext = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plaintext.setMinimumSize(QtCore.QSize(350, 350))
        self.plaintext.setMaximumSize(QtCore.QSize(350, 350))
        self.plaintext.setObjectName("PlaintTextEdit")
        self.plaintext.setStyleSheet("background-color:white;")

        self.horizontalLayout.addWidget(self.plaintext)

        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.action_k = QtWidgets.QAction(MainWindow)
        self.action_k.setObjectName("action_k")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "İngilizce-Türkçe/Türkçe-İngilizce Çeviri Programı"))
        self.pushButton.setText(_translate("MainWindow", "Bul"))
        self.pushButton2.setText(_translate("MainWindow", "Temizle"))


    def temizle(self):
        self.plaintext.clear()
        self.lineEdit.clear()

    def temizle_radio(self):
        if (self.lineEdit.text() == ""):
            self.listWidget.clear()
            if (self.radioButton.isChecked()):
                cursor.execute('select SozcukAdi from IngilizceTurkceTablosu')
                for row in cursor.fetchall():
                    self.listWidget.addItem(row[0])
            else :
                cursor.execute('select SozcukAdi from TurkceIngilizceTablosu')
                for row in cursor.fetchall():
                    self.listWidget.addItem(row[0])
        else :
            if (self.radioButton.isChecked()):
                self.listWidget.clear()
                cursor.execute(
                    "select * from IngilizceTurkceTablosu where SozcukAdi LIKE '{0}%'".format(self.lineEdit.text()))
                for row in cursor.fetchall():
                    self.listWidget.addItem(row[1])
                if (self.lineEdit.text() == ""):
                    cursor.execute('select SozcukAdi from IngilizceTurkceTablosu')
                    for row in cursor.fetchall():
                        self.listWidget.addItem(row[0])
            else:
                self.listWidget.clear()
                cursor.execute(
                    "select * from TurkceIngilizceTablosu where SozcukAdi LIKE '{0}%'".format(self.lineEdit.text()))
                for row in cursor.fetchall():
                    self.listWidget.addItem(row[1])
                if (self.lineEdit.text() == ""):
                    cursor.execute('select SozcukAdi from TurkceIngilizceTablosu')
                    for row in cursor.fetchall():
                        self.listWidget.addItem(row[0])


    def filtrele(self):
        if(self.radioButton.isChecked()):
            self.listWidget.clear()
            cursor.execute("select * from IngilizceTurkceTablosu where SozcukAdi LIKE '{0}%'".format(self.lineEdit.text()))
            for row in cursor.fetchall():
                self.listWidget.addItem(row[1])
            if(self.lineEdit.text()==""):
                cursor.execute('select SozcukAdi from IngilizceTurkceTablosu')
                for row in cursor.fetchall():
                    self.listWidget.addItem(row[0])
        else :
            self.listWidget.clear()
            cursor.execute(
                "select * from TurkceIngilizceTablosu where SozcukAdi LIKE '{0}%'".format(self.lineEdit.text()))
            for row in cursor.fetchall():
                self.listWidget.addItem(row[1])
            if (self.lineEdit.text() == ""):
                cursor.execute('select SozcukAdi from TurkceIngilizceTablosu')
                for row in cursor.fetchall():
                    self.listWidget.addItem(row[0])

    def goster(self,item):
        if (self.radioButton.isChecked()):
            cursor.execute("select SozcukAnlami from IngilizceTurkceTablosu where SozcukAdi='%s'"%item.text())
            for anlam in cursor.fetchone():
                self.plaintext.setPlainText(anlam)
        else :
            cursor.execute("select SozcukAnlami from TurkceIngilizceTablosu where SozcukAdi='%s'" % item.text())
            for anlam in cursor.fetchone():
                self.plaintext.setPlainText(anlam)

    def goster_button(self):
        if (self.lineEdit.text() != ""):
            if (self.radioButton.isChecked()):
                try:
                    db=cursor.execute("select SozcukAnlami from IngilizceTurkceTablosu where SozcukAdi='%s'" % self.lineEdit.text())
                    for anlam in db.fetchone():
                        self.plaintext.setPlainText(anlam)
                except:
                    pass

            else:
                try:
                    db = cursor.execute("select SozcukAnlami from TurkceIngilizceTablosu where SozcukAdi='%s'" % self.lineEdit.text())
                    for anlam in db.fetchone():
                        self.plaintext.setPlainText(anlam)
                except:
                    pass
        else:
            pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
