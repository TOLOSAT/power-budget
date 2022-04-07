import tkinter as t
import GestionData as ges


class ModifierFrame :
    def __init__(self,data ,Mode, sub_sys):
        self.root = t.Toplevel()
        self.root.grab_set()
        self.mode = Mode
        self.sub_sys = sub_sys
        self.data = data
        self.radio_button_value = {}
        if(sub_sys != None):
            self.modifSousSystem()

    def sauvegarder(self):
        for i in range(len(self.testlist)) :
            conso = int(self.testlist[i].get())
            sub_sys = self.radio_button_value[self.radio[i]]
            self.data.modifierModeC(self.sub_sys,sub_sys, conso)
        self.data.save()
    
    def supprimer(self):
        self.data.delModeC(self.sub_sys, self.var.get())
        self.root.update()

    def modifSousSystem(self):
        pFrame = t.Frame(self.root)
        listFrame = t.Frame(pFrame)
        pbutton = t.Frame(self.root)
        t.Label(self.root, text="Modification de sous-systeme").grid(pady=10, row=0, column=0)
        t.Label(listFrame, text="Nom").grid(row=0, column=0)
        t.Label(listFrame, text="Consomation").grid(row=0, column=1)
        key, conso = self.data.listModeC(self.sub_sys)
        self.radio = []
        self.testlist=[]
        self.var = t.StringVar()
        self.var.set(key[0])

        for i in range(len(key)) :
            temp = t.Radiobutton(listFrame,text=key[i], variable=self.var, value=key[i])
            self.radio_button_value[temp] = key[i]
            temp.grid(row=i+1, column=0)
            self.radio.append(temp)
            temp = t.Entry(listFrame, textvariable=conso[i], text=key[i])
            temp.delete(0, t.END)
            temp.insert(t.INSERT, str(conso[i]))
            temp.grid(row=i+1, column=1)
            self.testlist.append(temp)

        pbutton.grid(row=2, column=0)
        t.Button(pbutton, text="sauvegarder", command=self.sauvegarder).grid(row=0, column=0, padx=10, pady=10)
        t.Button(pbutton,text="supprimer", command=self.supprimer ).grid(row=0, column=1)
        pFrame.grid(row=1, column=0, sticky="nwse", padx=10)
        listFrame.grid(row=0, column=0, sticky="nwse")
        self.root.mainloop()

