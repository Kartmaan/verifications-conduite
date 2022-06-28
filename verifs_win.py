from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1146, 726)
        MainWindow.setMinimumSize(QtCore.QSize(1146, 726))
        MainWindow.setMaximumSize(QtCore.QSize(1146, 726))
        MainWindow.setWindowTitle("Quiz vérifications conduite")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Frame title
        self.frame_title = QtWidgets.QFrame(self.centralwidget)
        self.frame_title.setGeometry(QtCore.QRect(10, 9, 1121, 61))
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")

        # Label title
        self.label_title = QtWidgets.QLabel(self.frame_title)
        self.label_title.setGeometry(QtCore.QRect(10, 9, 1101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")

        # Frame choice
        self.frame_choice = QtWidgets.QFrame(self.centralwidget)
        self.frame_choice.setGeometry(QtCore.QRect(10, 80, 351, 571))
        self.frame_choice.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_choice.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_choice.setLineWidth(2)
        self.frame_choice.setObjectName("frame_choice")

        # CheckBox vérifications intérieures
        self.checkBox_verif_int = QtWidgets.QCheckBox(self.frame_choice)
        self.checkBox_verif_int.setGeometry(QtCore.QRect(80, 170, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_verif_int.setFont(font)
        self.checkBox_verif_int.setText("Vérifications intérieures")
        self.checkBox_verif_int.setIconSize(QtCore.QSize(20, 20))
        self.checkBox_verif_int.setObjectName("checkBox_verif_int")

        # CheckBox vérifications extérieures
        self.checkBox_verif_ext = QtWidgets.QCheckBox(self.frame_choice)
        self.checkBox_verif_ext.setGeometry(QtCore.QRect(80, 290, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_verif_ext.setFont(font)
        self.checkBox_verif_ext.setText("Vérifications exterieures")
        self.checkBox_verif_ext.setIconSize(QtCore.QSize(20, 20))
        self.checkBox_verif_ext.setObjectName("checkBox_verif_ext")

        # PushButton Quiz
        self.pushButton_quiz = QtWidgets.QPushButton(self.frame_choice)
        self.pushButton_quiz.setGeometry(QtCore.QRect(10, 470, 331, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_quiz.setFont(font)
        self.pushButton_quiz.setObjectName("pushButton_quiz")

        # Label choice
        self.label_choice = QtWidgets.QLabel(self.frame_choice)
        self.label_choice.setGeometry(QtCore.QRect(4, 9, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_choice.setFont(font)
        self.label_choice.setAlignment(QtCore.Qt.AlignCenter)
        self.label_choice.setObjectName("label_choice")

        # Frame statut
        self.frame_statut = QtWidgets.QFrame(self.centralwidget)
        self.frame_statut.setGeometry(QtCore.QRect(10, 660, 1121, 61))
        self.frame_statut.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_statut.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_statut.setObjectName("frame_statut")

        # Label statut
        self.label_statut = QtWidgets.QLabel(self.frame_statut)
        self.label_statut.setGeometry(QtCore.QRect(14, 10, 1101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.label_statut.setFont(font)
        self.label_statut.setAlignment(QtCore.Qt.AlignCenter)
        self.label_statut.setObjectName("label_statut")

        # Tab widget
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(374, 79, 761, 571))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")

        ### Tab question
        self.tab_question = QtWidgets.QWidget()
        self.tab_question.setObjectName("tab_question")

        # Label consigne
        self.label_consigne = QtWidgets.QLabel(self.tab_question)
        self.label_consigne.setGeometry(QtCore.QRect(14, 50, 731, 101))
        self.label_consigne.setTextFormat(QtCore.Qt.AutoText)
        self.label_consigne.setScaledContents(False)
        self.label_consigne.setAlignment(QtCore.Qt.AlignCenter)
        self.label_consigne.setWordWrap(True)
        self.label_consigne.setObjectName("label_consigne")

        # GroupBox question 1
        self.groupBox_q1 = QtWidgets.QGroupBox(self.tab_question)
        self.groupBox_q1.setGeometry(QtCore.QRect(9, 159, 741, 121))
        self.groupBox_q1.setObjectName("groupBox_q1")

        # Label question 1
        self.label_q1 = QtWidgets.QLabel(self.groupBox_q1)
        self.label_q1.setGeometry(QtCore.QRect(30, 30, 681, 81))
        self.label_q1.setTextFormat(QtCore.Qt.AutoText)
        self.label_q1.setScaledContents(False)
        self.label_q1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_q1.setWordWrap(True)
        self.label_q1.setObjectName("label_q1")

        # GroupBox question 2
        self.groupBox_q2 = QtWidgets.QGroupBox(self.tab_question)
        self.groupBox_q2.setGeometry(QtCore.QRect(10, 350, 741, 121))
        self.groupBox_q2.setObjectName("groupBox_q2")

        # Label question 2
        self.label_q2 = QtWidgets.QLabel(self.groupBox_q2)
        self.label_q2.setGeometry(QtCore.QRect(30, 30, 681, 81))
        self.label_q2.setTextFormat(QtCore.Qt.AutoText)
        self.label_q2.setScaledContents(False)
        self.label_q2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_q2.setWordWrap(True)
        self.label_q2.setObjectName("label_q2")

        # Label question référence
        self.label_quest_ref = QtWidgets.QLabel(self.tab_question)
        self.label_quest_ref.setGeometry(QtCore.QRect(6, 20, 741, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_quest_ref.setFont(font)
        self.label_quest_ref.setAlignment(QtCore.Qt.AlignCenter)
        self.label_quest_ref.setObjectName("label_quest_ref")

        # pushButton NEXT
        self.pushButton_next = QtWidgets.QPushButton(self.tab_question)
        self.pushButton_next.setGeometry(QtCore.QRect(420, 487, 151, 41))
        self.pushButton_next.setObjectName("pushButton_next")

        # PushButton PREVIOUS
        self.pushButton_prev = QtWidgets.QPushButton(self.tab_question)
        self.pushButton_prev.setGeometry(QtCore.QRect(180, 487, 151, 41))
        self.pushButton_prev.setObjectName("pushButton_prev")

        ## ADD TAB
        self.tabWidget.addTab(self.tab_question, "")

        ### Tab reponse
        self.tab_reponse = QtWidgets.QWidget()
        self.tab_reponse.setObjectName("tab_reponse")

        # GroupBox reponse 1
        self.groupBox_r1 = QtWidgets.QGroupBox(self.tab_reponse)
        self.groupBox_r1.setGeometry(QtCore.QRect(10, 100, 741, 151))
        self.groupBox_r1.setObjectName("groupBox_r1")

        # Label reponse 1
        self.label_r1 = QtWidgets.QLabel(self.groupBox_r1)
        self.label_r1.setGeometry(QtCore.QRect(30, 40, 681, 101))
        self.label_r1.setTextFormat(QtCore.Qt.AutoText)
        self.label_r1.setScaledContents(False)
        self.label_r1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_r1.setWordWrap(True)
        self.label_r1.setObjectName("label_r1")

        # GroupBox reponse 2
        self.groupBox_r2 = QtWidgets.QGroupBox(self.tab_reponse)
        self.groupBox_r2.setGeometry(QtCore.QRect(10, 290, 741, 151))
        self.groupBox_r2.setObjectName("groupBox_r2")

        # Label reponse 2
        self.label_r2 = QtWidgets.QLabel(self.groupBox_r2)
        self.label_r2.setGeometry(QtCore.QRect(30, 40, 681, 101))
        self.label_r2.setTextFormat(QtCore.Qt.AutoText)
        self.label_r2.setScaledContents(False)
        self.label_r2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_r2.setWordWrap(True)
        self.label_r2.setObjectName("label_r2")

        # Label question référence 2
        self.label_quest_ref_2 = QtWidgets.QLabel(self.tab_reponse)
        self.label_quest_ref_2.setGeometry(QtCore.QRect(0, 20, 751, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_quest_ref_2.setFont(font)
        self.label_quest_ref_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_quest_ref_2.setObjectName("label_quest_ref_2")

        ## ADD TAB
        self.tabWidget.addTab(self.tab_reponse, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Quiz sur les vérifications pour l\'épreuve de conduite"))
        self.pushButton_quiz.setText(_translate("MainWindow", "Lancer le quiz"))
        self.label_choice.setText(_translate("MainWindow", "Choix du questionnaire"))
        self.label_statut.setText(_translate("MainWindow", "Message de status"))
        self.label_consigne.setText(_translate("MainWindow", "MONTREZ​ ​LE​ ​VOYANT​ ​D\'ALERTE​ ​SIGNALANT​ ​UNE​ ​TEMPÉRATURE​ ​TROP​ ​ÉLEVÉE DU​ ​LIQUIDE​ ​DE​ ​REFROIDISSEMENT"))
        self.groupBox_q1.setTitle(_translate("MainWindow", "Question 1"))
        self.label_q1.setText(_translate("MainWindow", "Sur autoroute, comment indiquer avec précision les lieux de \n"
"l’accident depuis un téléphone portable ?"))
        self.groupBox_q2.setTitle(_translate("MainWindow", "Question 2"))
        self.label_q2.setText(_translate("MainWindow", "Pourquoi ne faut-il pas laisser une personne en perte de \n"
"connaissance allongée sur le dos ?"))
        self.label_quest_ref.setText(_translate("MainWindow", "Vérifications intérieures | Question 9, 57"))
        self.pushButton_next.setText(_translate("MainWindow", "Suivant >>>"))
        self.pushButton_prev.setText(_translate("MainWindow", "<<< Précédent"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_question), _translate("MainWindow", "Questions"))
        self.groupBox_r1.setTitle(_translate("MainWindow", "Réponse 1"))
        self.label_r1.setText(_translate("MainWindow", "En indiquant le numéro de l’autoroute, le sens de \n"
"circulation et le point kilométrique"))
        self.groupBox_r2.setTitle(_translate("MainWindow", "Réponse 2"))
        self.label_r2.setText(_translate("MainWindow", "L’arrêt respiratoire et l’arrêt cardiaque"))
        self.label_quest_ref_2.setText(_translate("MainWindow", "Vérifications intérieures | Question 9, 57"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_reponse), _translate("MainWindow", "Réponses"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
