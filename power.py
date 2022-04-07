# -*- coding: utf-8 -*-

import sys
import signal
import os
import GestionData as ges


def handler_KeyboardInterrupt(sig, frame):
    print("sauvegarde réussi,  au revoir")
    sys.exit(0)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def menuPrincipal():
    print(" Bonjours,\n \t- pour la gestion des sous-systéme, Tapez 1 \n \t- Pour la gestion des mode du satélite, Tapez 2")
    return ges.entreIntUtilisateur(1, 2)


def GestionSS(data):
    entre = 0
    subSyst = None
    mode = None
    while entre != -1:
        Listmenu = [-1]

        menu = 0

        print("-1 - quitté l'application")
        if(subSyst != None):
            '''si dans un sous systéme, affiché les option sur le sous-systéme '''
            print(0, " - Retour au menu précédent")
            Listmenu.append(0)
            print(2, " - Ajouté un mode")
            Listmenu.append(1)
            print(3, " - Ajouté un Sous-systéme")
            Listmenu.append(2)
            menu = 3
        else:
            "si à la racine du dossier, affiché les option pour les sous systéme"
            print(1, " - Ajouté le sous-systéme")
            Listmenu.append(menu)
            menu = 1

        print()
        option = menu+1
        for i in data.listSS():
            menu += 1
            print(menu, " - ", i)
            

        entre = ges.entreIntUtilisateur(-1, menu)
        cls()
        if entre not in Listmenu:
            '''récupération des données du XML en fonction de la situhation actuelle'''
            if subSyst == None:
                subSyst = data.listSS()[entre-option]
                print("je suis là")
            else:
                mode = data.listSS()[entre-option]
        else:
            '''Menu pour le cas ou nous somme dans un sous systéme'''
            if entre == 1:
                data.addSS()
                print("\nAjout réussi")
            if entre == 0:
                data.delSS(subSyst)
                print("Suppression réussi")
            if entre == 2:
                data.addModeC(subSyst)
                print("\nAjout réussi")
            if 0 == entre:
                subSyst == None

        if mode != None:
            '''menu dans le cas ou un mode et selectionné'''
            print(" menu pour : ", subSyst, " ", mode)
            print(" 1 - supprimer mode")
            print(" 2 - modifier mode")
            entre = ges.entreIntUtilisateur(-1, 2)

            if entre == 1:
                data.delModeC(subSyst, mode)
                print("Suppression réussi")
            if entre == 2:
                data.modifierModeC(subSyst, mode)
                print("\nModifiaction réussi")
            mode = None
        cls()
    return entre


signal.signal(signal.SIGINT, handler_KeyboardInterrupt)
global data
data = ges.GestionData("data.json")

while True:
    menu = -1
    sousS = None
    mode = None

    entre = menuPrincipal()
    cls()
    if entre == 1 :
        menu = GestionSS(data)
    elif entre ==2 :
        x=0

