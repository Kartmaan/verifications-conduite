import random
import sys

import pandas as pd
from PyQt5 import QtWidgets, QtCore

from verifs_win import Ui_MainWindow

# Création des DataFrames
verif_int = pd.read_excel("verif_int.xlsx")
verif_ext = pd.read_excel("verif_ext.xlsx")

# Int indexes
verif_int_idx = []
for idx in verif_int['Numéro']:
    verif_int_idx.append(eval(idx))

# Ext indexes
verif_ext_idx = []
for idx in verif_ext['Numéro']:
    verif_ext_idx.append(eval(idx))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.quest_posees = []
        self.df_choisi = None
        self.quiz_choisi = None

        # Initialisation des widgets
        self.checkBox_verif_int.setChecked(True)
        self.checkBox_verif_ext.setChecked(True)

        self.label_quest_ref.setText("...")
        self.label_quest_ref_2.setText("...")

        self.label_consigne.setText("...")

        self.label_q1.setText("...")
        self.label_q2.setText("...")

        self.label_r1.setText("...")
        self.label_r2.setText("...")

        self.label_statut.setText("...")

        # Connexion des boutons avec leurs fonctions
        self.pushButton_quiz.clicked.connect(self.quiz_button)
        self.pushButton_next.clicked.connect(self.next_button)
        self.pushButton_prev.clicked.connect(self.previous_button)
        self.checkBox_verif_int.clicked.connect(self.int_checkBox)
        self.checkBox_verif_ext.clicked.connect(self.ext_checkBox)

    def findNum(self, quiz):
        """ Choisi d'un nombre aléatoire et vérifie
        s'il correspond à une question existante
        dans le/les DataFrame(s). Si c'est le cas, 
        renvoie l'index correspondant """

        dblQuiz = []

        # Vérifiactions intérieures OU global
        if quiz == 0 or quiz == 2:
            found = False
            
            while found == False:
                num = random.randint(1, 99)
                i = 0

                for idx in verif_int_idx:
                    if num in idx:
                        print("{} est à l'index {}".format(num, i))
                        found = True
                        break
                    if num not in idx:
                        i+=1
                        found = False
                    if i >= len(verif_int_idx):
                        found = False
                        #print("{} PAS DANS LA LISTE".format(num))
                        break
            if quiz == 0:
                return i
            if quiz == 2:
                dblQuiz.append(i)
        
        # Vérifications extérieures ou globale
        if quiz == 1 or quiz == 2:
            found = False
        
            while found == False:
                num = random.randint(1, 99)
                i = 0

                for idx in verif_ext_idx:
                    if num in idx:
                        print("{} est à l'index {}".format(num, i))
                        found = True
                        break
                    if num not in idx:
                        i+=1
                        found = False
                    if i >= len(verif_ext_idx):
                        found = False
                        #print("{} PAS DANS LA LISTE".format(num))
                        break
            if quiz == 1:
                return i
            if quiz == 2:
                dblQuiz.append(i)
                return(dblQuiz)
    
    def quiz_button(self):

        # Vérifications intérieures
        if self.checkBox_verif_int.isChecked() and not self.checkBox_verif_ext.isChecked():
            self.display(df = verif_int, quiz=0)

        # Vérifications extèrieures
        elif not self.checkBox_verif_int.isChecked() and self.checkBox_verif_ext.isChecked():
            self.display(df = verif_ext, quiz=1)
        
        # Vérifications int. ET ext.
        else:
            self.display(df = None, quiz=2)

        """ Une fois le quiz lancé, le bouton se désactive 
        jusqu'à qu'un changement survienne dans le cochement
        des cases """
        self.pushButton_quiz.setEnabled(False)

        self.quest_posees = [] # Vidage de la liste
    
    def display(self, df, quiz, rand = True):
        if quiz == 2:
            df = random.choice([verif_int, verif_ext])

            if df is verif_int:
                idx = self.findNum(quiz)[0]
            else:
                idx = self.findNum(quiz)[1]
        else :
            idx = self.findNum(quiz)

        cons = str(df.at[idx, "Consigne"])
        q1 = str(df.at[idx, "Question 1"])
        q2 = str(df.at[idx, "Question 2"])
        r1 = str(df.at[idx, "Réponse 1"])
        r2 = str(df.at[idx, "Réponse 2"])

        self.label_consigne.setText(cons)
        self.label_q1.setText(q1)
        self.label_q2.setText(q2)
        self.label_r1.setText(r1)
        self.label_r2.setText(r2)

        # Save
        self.df_choisi = df
        self.quiz_choisi = quiz

        quest_num = eval(df.at[idx, "Numéro"])
        if 0 in quest_num:
            quest_num = "{}".format(quest_num[0])
        else:
            quest_num = "{}, {}".format(quest_num[0], quest_num[1])

        if self.df_choisi is verif_int:
            #print(quest_num)
            self.label_quest_ref.setText("Vérifications intèrieures - Question {}".format(quest_num))
            self.label_quest_ref_2.setText("Vérifications intèrieures - Question {}".format(quest_num))

        else:
            self.label_quest_ref.setText("Vérifications extèrieures - Question {}".format(quest_num))
            self.label_quest_ref_2.setText("Vérifications extèrieures - Question {}".format(quest_num))
    
    def next_button(self):
        self.display(self.df_choisi, quiz = self.quiz_choisi)
    
    def previous_button(self):
        print("PREVIOUS")
    
    def int_checkBox(self):
        """ Comportement du checkBox Vérif. int. """

        if not self.checkBox_verif_int.isChecked() and not self.checkBox_verif_ext.isChecked():
            self.pushButton_quiz.setEnabled(False)
            self.label_statut.setText("Cochez au moins un questionnaire")
        
        if self.checkBox_verif_int.isChecked() or self.checkBox_verif_ext.isChecked():
            self.pushButton_quiz.setEnabled(True)
            self.label_statut.setText("...")

    def ext_checkBox(self):
        """ Compotement du checkBox Vérif. ext. """
        if not self.checkBox_verif_int.isChecked() and not self.checkBox_verif_ext.isChecked():
            self.pushButton_quiz.setEnabled(False)
            self.label_statut.setText("Cochez au moins un questionnaire")
        
        if self.checkBox_verif_int.isChecked() or self.checkBox_verif_ext.isChecked():
            self.pushButton_quiz.setEnabled(True)
            self.label_statut.setText("...")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())