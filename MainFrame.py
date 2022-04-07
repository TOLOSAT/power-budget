
from tkinter.constants import VERTICAL
import ModifierFrame
import GestionData as ges
import tkinter as t

class app:

    def modifier(self) :
        mode = None
        ss = None
        if len(self.listSS.curselection()) != 0 :
            ss = self.listSS.get(self.listSS.curselection())
        else :
           mode = self.listMode.get(self.listMode.curselection())
        ModifierFrame.ModifierFrame(self.data, mode, ss)

    def supprimer(self):
        if len(self.listSS.curselection()) != 0 :
            self.data.delSS(self.listSS.get(self.listSS.curselection()))
        else :
            self.data.delModeSat(self.listMode.get(self.listMode.curselection()))
        self.listMode.delete(0, t.END)
        self.listSS.delete(0, t.END)
        self.initListBox()
        
    def initListBox(self):
        donnees = self.data.listSS()
        for i in range(len(donnees)) :
            self.listSS.insert(i, donnees[i])

        donnees = list(self.data.listModeSat())
        for i in range(len(donnees)) :
            self.listMode.insert(i, donnees[i])


    def __init__(self) :
        self.root = t.Tk()
        button = t.Frame(self.root)
        listeF = t.Frame(self.root)
        labelT = t.Frame(self.root)

        t.Label(self.root, text="Power budget").pack()
        t.Label(labelT, text="Mode des sous-systeme").grid(row=0, column=0)
        t.Label(labelT, text="      ").grid(row=0, column=1)
        t.Label(labelT, text="Mode du satelite").grid(row=0, column=2)

        t.Button(button, text='modifier', command=self.modifier).grid(row=0, column=0)
        t.Button(button, text='supprimer', command=self.supprimer).grid(row=0, column=3)
        t.Button(button, text='ajouter sous-systeme').grid(row=0, column=1)
        t.Button(button, text='ajouter un mod').grid(row=0, column=2)

        self.data = ges.GestionData("data.json")

        sb = t.Scrollbar(listeF, orient=VERTICAL)
        sb2 = t.Scrollbar(listeF, orient=VERTICAL)
        self.listSS = t.Listbox(listeF, yscrollcommand=sb.set)
        self.listMode = t.Listbox(listeF, yscrollcommand=sb2.set)
        sb['command'] = self.listSS.yview
        sb2['command'] = self.listMode.yview

        self.initListBox()

        self.listSS.grid(row=0, column=0)
        self.listMode.grid(row=0, column=2)
        sb.grid(row= 0, column=1,sticky='nsew')
        sb2.grid(row= 0, column=3, sticky='nsew')
        labelT.pack()
        listeF.pack()
        button.pack(padx=10, pady= 10)


        self.root.mainloop()

app()