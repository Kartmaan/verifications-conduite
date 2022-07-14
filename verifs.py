import random
import sys

import pandas as pd
from PyQt5 import QtWidgets, QtCore

from verifs_win import Ui_MainWindow

# Création des DataFrames
verif_int = pd.read_excel("verif_int.xlsx")
verif_ext = pd.read_excel("verif_ext.xlsx")

# Pour chaque dataframe la numérotation des questions sera extraite 
# et stockée dans une liste. Du fait qu'une question peut avoir 
# jusqu'à 2 numérotations différentes elles sont contenues dans un 
# tuple. Ces listes permettront à la fonction self.findnum() de les 
# parcourir afin définir un nombre aléatoire présent dans celles-ci

# Numérotation pour vérifications intérieures
verif_int_idx = []
for idx in verif_int['Numéro']:
    verif_int_idx.append(eval(idx))

# Numérotation pour vérifications extèrieures
verif_ext_idx = []
for idx in verif_ext['Numéro']:
    verif_ext_idx.append(eval(idx))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Toutes les questions précédement et actuellement posées 
        # sont stockées dans cette liste sous la forme :
        # [dataframe, code quiz, index de la question] 
        self.quest_posees = []

        # Cette valeur indique le positionnement de la question 
        # actuellement affichée parmis les questions précédement 
        # posées dans la liste 'self.quest_posees'. La valeur 
        # s'incrémente quand l'utilisateur clique sur suivant et 
        # se décrémente lorsqu'il clique sur précédent
        self.idx_actuel = -1

        # Sauvegarde du dataframe choisi en fonction des choix du 
        # quiz par l'utilisateur
        self.df_choisi = None

        # Sauvegarde du code quiz en fonction des choix du quiz par 
        # l'utilisateur
        # 0 : Uniquement vérifications intérieures
        # 1 : Uniquement vérifications extèrieures
        # 2 : Vérifications int. ET ext.
        self.quiz_choisi = None

        # Initialisation des widgets à l'execution du programme
        self.checkBox_verif_int.setChecked(True)
        self.checkBox_verif_ext.setChecked(True)

        self.pushButton_prev.setEnabled(False)
        self.pushButton_next.setEnabled(False)

        self.label_quest_ref.setText("...")
        self.label_quest_ref_2.setText("...")

        self.label_consigne.setText("...")

        self.label_q1.setText("...")
        self.label_q2.setText("...")

        self.label_r1.setText("...")
        self.label_r2.setText("...")

        self.label_statut.setText("...")

        # Connexion des boutons avec leurs fonctions respectives
        self.pushButton_quiz.clicked.connect(self.quiz_button)
        self.pushButton_next.clicked.connect(self.next_button)
        self.pushButton_prev.clicked.connect(self.previous_button)
        self.checkBox_verif_int.clicked.connect(self.int_checkBox)
        self.checkBox_verif_ext.clicked.connect(self.ext_checkBox)

    def findNum(self, quiz):
        """ Choisi un nombre aléatoire et vérifie
        s'il correspond à une question existante
        dans le/les DataFrame(s) séléctionné(s). 
        Si c'est le cas, renvoie l'index correspondant.
        
        quiz 0 = Vérifications intérieures
        quiz 1 = Vérifications extérieures
        quiz 2 = Vérifications intérieures ET extérieures """

        # Si les deux questionnaires ont été cochés 
        # (code quiz = 2), cette liste contiendra l'index 
        # valable trouvé pour le 1er dataframe ainsi que 
        # pour le 2eme  
        dblQuiz = []

        # Vérifiactions intérieures OU global
        if quiz == 0 or quiz == 2:
            found = False
            
            while found == False:
                num = random.randint(0, 99)
                i = 0

                for idx in verif_int_idx:
                    if num in idx:
                        found = True
                        break # Sortie de la boucle for
                    if num not in idx:
                        i+=1
                        found = False
                    if i >= len(verif_int_idx):
                        found = False
                        break # Sortie de la boucle for
                        # valeur non trouvée
                        # reprise de la boucle while

            if quiz == 0:
                return i
            if quiz == 2:
                dblQuiz.append(i)
        
        # Vérifications extérieures ou globale
        if quiz == 1 or quiz == 2:
            found = False
        
            while found == False:
                num = random.randint(0, 99)
                i = 0

                for idx in verif_ext_idx:
                    if num in idx:
                        found = True
                        break
                    if num not in idx:
                        i+=1
                        found = False
                    if i >= len(verif_ext_idx):
                        found = False
                        break
            if quiz == 1:
                return i
            if quiz == 2:
                dblQuiz.append(i)
                return(dblQuiz)
    
    def quiz_button(self):
        """ Lors du clique sur 'Lancer le quiz' le programme choisi 
        le/les dataframe(s) à partir duquel/desquels afficher les 
        questions en fonction des choix cochés par l'utilisateur """

        # Au commencement du quiz le bouton 'Précédent' est 
        # désactivé et le bouton 'Suivant' activé
        self.pushButton_prev.setEnabled(False)
        self.pushButton_next.setEnabled(True)

        # A chaque lancement de quiz, la liste des questions 
        # précédement posées se vide et l'index actuel se 
        # réinitialise
        self.quest_posees = [] # Vidage de la liste
        self.idx_actuel = -1 # Réinitialisation de l'index

        # -- Vérifications intérieures --
        # L'utilisateur n'a coché QUE cette case
        if self.checkBox_verif_int.isChecked() and not self.checkBox_verif_ext.isChecked():
            self.display(df = verif_int, quiz=0)
            self.df_choisi = verif_int

        # -- Vérifications extèrieures --
        # L'utilisateur n'a coché QUE cette case
        elif not self.checkBox_verif_int.isChecked() and self.checkBox_verif_ext.isChecked():
            self.display(df = verif_ext, quiz=1)
            self.df_choisi = verif_ext
        
        # -- Vérifications int. ET ext. --
        # L'utilisateur a coché les DEUX cases
        # Le choix aléatoire du dataFrame se fait dans la fonction
        # self.display() 
        else:
            self.display(df = None, quiz=2)

        # Une fois le quiz lancé, le bouton 'Lancer le quiz' 
        # se désactive jusqu'à qu'un changement survienne dans 
        # le cochement des cases
        self.pushButton_quiz.setEnabled(False)
    
    def display(self, df, quiz = None, rand = True, idx_choosen = None):
        """ Affichage des informations """
        
        """ Il ne s'agit pas d'une nouvelle question aléatoire 
        l'index de la question à afficher et le dataframe sont déjà 
        connus (stockés dans la liste 'self.quest_posees' """
        if rand == False:
            idx = idx_choosen
        
        # Nouvelle question aléatoire
        else:
            if quiz == 2: # Double quiz (ext+int)
                # Choix aléatoire entre les 2 dataframes
                df = random.choice([verif_int, verif_ext])
                self.df_choisi = df

                if df is verif_int: # Verif int
                    idx = self.findNum(quiz)[0]
                else: # Verif ext
                    idx = self.findNum(quiz)[1]

            else: # Mono quiz
                # Le dataframe a déjà été défini dans la 
                # fonction self.quiz_button()
                idx = self.findNum(quiz)

        # Récupération des données
        cons = str(df.at[idx, "Consigne"])
        q1 = str(df.at[idx, "Question 1"])
        q2 = str(df.at[idx, "Question 2"])
        r1 = str(df.at[idx, "Réponse 1"])
        r2 = str(df.at[idx, "Réponse 2"])

        # Affichage des données
        self.label_consigne.setText(cons)
        self.label_q1.setText(q1)
        self.label_q2.setText(q2)
        self.label_r1.setText(r1)
        self.label_r2.setText(r2)

        # Save
        self.quiz_choisi = quiz

        # Affichage numéro de la question
        quest_num = eval(df.at[idx, "Numéro"])
        if None in quest_num:
            quest_num = "{}".format(quest_num[0])
        else:
            quest_num = "{}, {}".format(quest_num[0], quest_num[1])

        if self.df_choisi is verif_int:
            self.label_quest_ref.setText("Vérifications intèrieures - Question {}".format(quest_num))
            self.label_quest_ref_2.setText("Vérifications intèrieures - Question {}".format(quest_num))

        else:
            self.label_quest_ref.setText("Vérifications extèrieures - Question {}".format(quest_num))
            self.label_quest_ref_2.setText("Vérifications extèrieures - Question {}".format(quest_num))

        
        if self.idx_actuel == -1 or self.idx_actuel == 0:
            #print("+1 DISPLAY 1")
            self.idx_actuel += 1

        # Insertion de la question dans la liste
        """ Les nouvelles questions sont ajoutées à la 
        liste self.quest_posees sous forme d'une liste 
        contenant [Le dataframe choisi,  
        le code quiz (0,1,2), 
        l'index de la question] """
        if self.idx_actuel == len(self.quest_posees) and rand == True:
            add = [self.df_choisi, quiz, idx]
            self.quest_posees.append(add)
            #print("+1 DISPLAY 2")
            self.idx_actuel += 1

    def next_button(self):
        """
        A chaque nouvelle question posée la valeur de l'index 
        (self.idx_actuel) est incrémenté de 1 et les données de la 
        question sont ajoutées à la liste (self.quest_posees).
        Le bouton 'Suivant' incrémente 'self.idx_actuel' de 1, 
        tandis que le bouton "Précédent" la décrémente de 1
        
        - Si l'index de la question actuellement affichée 
        (self.idx_actuel) correspond à la longueur de la liste 
        des questions précédement posées (self.quest_posees), 
        la question suivante sera une nouvelle question aléatoire
        
        - Si l'index de la question actuellement affichée 
        (self.idx_actuel) est inférieur à la longueur de la 
        liste des questions posées, on affiche la question suivante 
        sur la liste (il s'agit d'une question précédement posées)
        """

        # (dés)activation des boutons
        """ Si l'index actuel se trouve en tout début de la 
        liste des questions posées, le bouton 'Précédent' 
        se désactive (pas de retour en arrière) """
        if self.idx_actuel >= 1:
            self.pushButton_prev.setEnabled(True)
        else:
            self.pushButton_prev.setEnabled(False)

        # Nouvelle question aléatoire
        """ L'index actuel correspond à la longueur de la liste des 
        questions posées, on se trouve donc en bout de liste. La 
        prochaine question sera une nouvelle question aléatoire qui 
        sera ajoutée à son tour la liste """
        if self.idx_actuel == len(self.quest_posees):
            self.display(self.df_choisi, quiz = self.quiz_choisi)
        
        else: # Question déjà posée
            """ L'index actuel est inférieur à la longueur de la 
            liste des questions posées, on affiche la question 
            suivante sur la liste (il s'agit d'une question 
            précédement posées) """
            #print("+1 NEXT")
            self.idx_actuel += 1

            df = self.quest_posees[self.idx_actuel-1][0]
            quiz = self.quest_posees[self.idx_actuel-1][1]
            idx_c = self.quest_posees[self.idx_actuel-1][2]

            self.display(df, quiz = quiz, rand=False, idx_choosen=idx_c)

        #print("TAILLE LISTE : ", len(self.quest_posees))
        #print("INDEX ACTUEL : ", self.idx_actuel)
    
    def previous_button(self):
        #print("-1 PREV")
        self.idx_actuel -= 1
        
        # (dés)activation des boutons
        if self.idx_actuel == 1:
            self.pushButton_prev.setEnabled(False)
        else:
            self.pushButton_prev.setEnabled(True)
        
        df = self.quest_posees[self.idx_actuel-1][0]
        quiz = self.quest_posees[self.idx_actuel-1][1]
        idx_c = self.quest_posees[self.idx_actuel-1][2]
        self.display(df, quiz = quiz, rand=False, idx_choosen=idx_c)

        #print("TAILLE LISTE : ", len(self.quest_posees))
        #print("INDEX ACTUEL : ", self.idx_actuel)
    
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