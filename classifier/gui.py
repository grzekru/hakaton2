# -*- coding: utf-8 -*-

import os
import re
import glob
import codecs
import NaiveBayes
import string
import sys
from PyQt4 import QtCore, QtGui
from Task905 import classify

from klasyfikator_gui import Ui_MainWindow


class StartQt4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"), self.file_dialog)
        QtCore.QObject.connect(self.ui.pushButton_2,QtCore.SIGNAL("clicked()"), self.file_dialog2)
        
    def file_dialog(self):
        def getfeatures(text):
            """Funkcja do testów."""
            text = text.lower();
            text = re.sub("[\?\!\.\,\:\;$\'\"„”_\(\)\[\]…]", " ", text);

            text = text.replace("ó", "o");
            text = text.replace("ą", "a");
            text = text.replace("ś", "s");
            text = text.replace("ć", "c");
            text = text.replace("ź", "z");
            text = text.replace("ż", "z");
            text = text.replace("ł", "l");
            text = text.replace("ę", "e");
            return list(set(text.split()))
        self.bayes = NaiveBayes.NaiveBayes(getfeatures)

        with codecs.open('featureCount.txt', 'r', encoding='utf-8') as f:
            self.bayes.feature_count = eval(f.read())
        with codecs.open('classCount.txt', 'r', encoding='utf-8') as f:
            self.bayes.class_count = eval(f.read())

        dialog = QtGui.QMessageBox.information(self, 'Załadowano', 'OK')

    def file_dialog2(self): 
        result = classify(self.bayes, self.ui.textEdit.toPlainText())
        #self.ui.textEdit.setText(result)
        self.ui.label_3.setText('Wynik: %s ' % result)

        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQt4()
    myapp.show()
    sys.exit(app.exec_())
