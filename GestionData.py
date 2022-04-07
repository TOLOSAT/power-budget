import json

class GestionData :
    def __init__(self, path):
        fichier = open(path, "r")
        self.path = path
        contenu = ""
        for ligne in fichier:
            contenu += ligne
        self.data = json.JSONDecoder().decode(contenu)

    def save(self):
        fichier = open(self.path, 'w')
        contenu = json.JSONEncoder().encode(self.data)
        fichier.write(contenu)

    def listSS(self):
        return list(self.data["sous-sys"].keys())

    def addSS(self):
        print(" Nom du sous-Systéme")
        nom = input("> ")
        self.data["sous-sys"]['nom']={}
        self.save()
    
    def delSS(self, name):
        del self.data["sous-sys"][name]
        for value in self.data["mode"]:
            if name in value :
                del value[name]
        self.save()
    
    def addModeC(self, ss): 
        print("Nom du mode de la carte : ", end="")
        nom = input("> ")
        print("\nConsomation de la carte : ", end="")
        conso = entreFloat()
        print()
        self.data["sous-sys"][ss][nom] = conso
        self.save()
        
    def delModeSat(self, mode):
        del self.data["mode"][mode]
    
    def delModeC(self, ss, modec):
        del self.data["sous-sys"][ss][modec]
        for value in self.data["mode"].values():
            if ss in value.keys() and modec in value.values():
                del value[ss]
        self.save()

    def modifierModeC(self, ss, modec, conso):
        self.data["sous-sys"][ss][modec] = conso


    def listModeC(self, ss):
        return (list(self.data["sous-sys"][ss].keys()), list(self.data["sous-sys"][ss].values()))

    def listModeSat(self):
        return self.data["mode"].keys()
    
    def addModeSat(self):
        print("Nom du sous-systéme de Tolosat", end="")
        nom = input("> ")
        print()
        for key, value in self.data["sous-sys"] :
            print("qu'elle sera le mode pour le sous systeme ", key)
            i=0
            for clef, valeur in value :
               print(i, " - ", clef, " : ", valeur)
               i = i+1
            entre = entreIntUtilisateur(0, i)
            self.data["mode"][nom]={}
            self.data["mode"][nom][value.keys()[entre]]=value.values()[i]
        self.save()

    def modifierModeSat(self, mode):
        self.data["mode"][mode] = {}
        for key, value in self.data["sous-sys"] :
            print("qu'elle sera le mode pour le sous systeme ", key)
            i=0
            for clef, valeur in value :
               print(i, " - ", clef, " : ", valeur)
               i = i+1
            entre = entreIntUtilisateur(0, i)
            self.data["mode"][mode]={}
            self.data["mode"][mode][value.keys()[entre]]=value.values()[i]
        self.save()

    def consoTotalModeSat(self, mode):
        conso = 0
        for key, valeur in self.data["mode"][mode] :
            conso += self.data["sous-sys"][key][valeur]
        return conso

def entreIntUtilisateur(max, min):
    value = input("> ")
    retour = None
    try:
        retour = int(value)
    except ValueError:
        retour = None
        pass
    while(retour == None or retour < max or retour > min):
        print("Erreur de saisie, veuillez recommencer")
        try:
            retour = int(input("> "))
        except ValueError:
            retour = None
            pass
    return retour

def entreFloat():
    value = input()
    retour = None
    try:
        retour = float(value)
    except ValueError:
        retour = None
        pass
    while( retour == None):
        print("Erreur de saisie, veuillez recommencer")
        try:
            retour = float(input())
        except ValueError:
            retour = None
            pass
    return retour

