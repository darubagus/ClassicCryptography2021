from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1129, 868)
        MainWindow.setStyleSheet("background-color: rgb(21, 45, 53);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 10, 321, 71))
        self.label.setStyleSheet("background-color: rgb(52, 91, 99);\n"
                                 "font-family: \"Cascadia Code SemiBold\";\n"
                                 "border: 2px solid black;\n"
                                 "border-radius: 5px;\n"
                                 "font-size: 10px;\n"
                                 "color: #D4ECDD;")
        self.label.setObjectName("label")
        self.outputTextArea = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.outputTextArea.setGeometry(QtCore.QRect(150, 110, 841, 361))
        self.outputTextArea.setStyleSheet("background-color: #D4ECDD;\n"
                                          "font-size: 15px;\n"
                                          "font-weight: bold;\n"
                                          "border-radius: 20px;\n"
                                          "border: 3px solid black;\n"
                                          "font: 75 18pt \"Cascadia Code\";\n"
                                          "padding: 10px;\n"
                                          "color: #112031")
        self.outputTextArea.setPlainText("")
        self.outputTextArea.setObjectName("outputTextArea")
        self.cipherAlgorithmComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.cipherAlgorithmComboBox.setGeometry(
            QtCore.QRect(580, 630, 391, 31))
        self.cipherAlgorithmComboBox.setStyleSheet("background-color: rgb(212, 236, 221);\n"
                                                   "font: 75 10pt \"Cascadia Code\";\n"
                                                   "padding-left: 10px;\n"
                                                   "border: none;")
        self.cipherAlgorithmComboBox.setObjectName("cipherAlgorithmComboBox")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.cipherAlgorithmComboBox.addItem("")
        self.encryptDecryptButton = QtWidgets.QPushButton(self.centralwidget)
        self.encryptDecryptButton.setGeometry(QtCore.QRect(580, 670, 391, 61))
        self.encryptDecryptButton.setStyleSheet("color: #D4ECDD;\n"
                                                "font: 75 10pt \"Cascadia Code\";\n"
                                                "border: 2px solid #D4ECDD;\n"
                                                "border-radius: 5px;")
        self.encryptDecryptButton.setObjectName("encryptDecryptButton")
        self.inputText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputText.setGeometry(QtCore.QRect(160, 530, 401, 201))
        self.inputText.setStyleSheet("border: 2px solid #D4ECDD;\n"
                                     "border-radius: 5px;\n"
                                     "color: rgb(212, 236, 221);\n"
                                     "padding: 5px;\n"
                                     "font: 75 13pt \"Cascadia Code\";")
        self.inputText.setPlainText("")
        self.inputText.setObjectName("inputText")
        self.inputFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.inputFileButton.setGeometry(QtCore.QRect(580, 500, 391, 111))
        self.inputFileButton.setStyleSheet("color: #D4ECDD;\n"
                                           "font: 75 20pt \"Cascadia Code\";\n"
                                           "border: 2px solid #D4ECDD;\n"
                                           "border-radius: 5px;")
        self.inputFileButton.setObjectName("inputFileButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 500, 111, 21))
        self.label_2.setStyleSheet("color: #D4ECDD;\n"
                                   "font: 75 13pt \"Cascadia Code\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 80, 111, 21))
        self.label_3.setStyleSheet("color: #D4ECDD;\n"
                                   "font: 75 13pt \"Cascadia Code\";")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1129, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Coding here....
        self.inputFileButton.clicked.connect(self.inputFileHandler)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Add method here...
    def inputFileHandler(self):
        file = QtWidgets.QFileDialog.getOpenFileName()
        path = file[0]
        filename = path.split('/')[-1]

        self.inputFileButton.setText(filename)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Classic Cryptography App"))
        self.label.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Classic Cryptography</span></p></body></html>"))
        self.cipherAlgorithmComboBox.setItemText(0, _translate(
            "MainWindow", "Vignere Cipher Standard Encrypt"))
        self.cipherAlgorithmComboBox.setItemText(1, _translate(
            "MainWindow", "Vignere Cipher Standard Decrypt"))
        self.cipherAlgorithmComboBox.setItemText(
            2, _translate("MainWindow", "Full Vignere Cipher Encrypt"))
        self.cipherAlgorithmComboBox.setItemText(
            3, _translate("MainWindow", "Full Vignere Cipher Decrypt"))
        self.cipherAlgorithmComboBox.setItemText(4, _translate(
            "MainWindow", "Auto Key Vignere Cipher Encrypt"))
        self.cipherAlgorithmComboBox.setItemText(5, _translate(
            "MainWindow", "Auto Key Vignere Cipher Decrypt"))
        self.cipherAlgorithmComboBox.setItemText(6, _translate(
            "MainWindow", "Extended Vignere Cipher Encrypt"))
        self.cipherAlgorithmComboBox.setItemText(7, _translate(
            "MainWindow", "Extended Vignere Cipher Decrypt"))
        self.cipherAlgorithmComboBox.setItemText(
            8, _translate("MainWindow", "Playfair Cipher Encrypt"))
        self.cipherAlgorithmComboBox.setItemText(
            9, _translate("MainWindow", "Playfair Cipher Decrypt"))
        self.cipherAlgorithmComboBox.setItemText(
            10, _translate("MainWindow", "Affine Cipher Encrypt"))
        self.cipherAlgorithmComboBox.setItemText(
            11, _translate("MainWindow", "Affine Cipher Decrypt"))
        self.cipherAlgorithmComboBox.setItemText(
            12, _translate("MainWindow", "Hill Cipher Encrypt"))
        self.cipherAlgorithmComboBox.setItemText(
            13, _translate("MainWindow", "Hill Cipher Decrypt"))
        self.encryptDecryptButton.setText(
            _translate("MainWindow", "Encrypt / Decrypt"))
        self.inputFileButton.setText(_translate("MainWindow", "Input File"))
        self.label_2.setText(_translate("MainWindow", "Text Input"))
        self.label_3.setText(_translate("MainWindow", "Text Output"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
