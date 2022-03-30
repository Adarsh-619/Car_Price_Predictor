
from PyQt5 import QtCore, QtGui, QtWidgets


class DialogBox(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 145)
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        self.ok_btn = QtWidgets.QPushButton(Dialog)
        self.ok_btn.setGeometry(QtCore.QRect(200, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.ok_btn.setFont(font)
        self.ok_btn.setDefault(True)
        self.ok_btn.setFlat(False)
        self.ok_btn.setObjectName("ok_btn")
        self.info_label = QtWidgets.QLabel(Dialog)
        self.info_label.setGeometry(QtCore.QRect(40, 40, 611, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.info_label.setFont(font)
        self.info_label.setObjectName("info_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Information"))
        self.ok_btn.setText(_translate("Dialog", "OK"))
        self.info_label.setText(_translate("Dialog", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = DialogBox()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
