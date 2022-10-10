# Pile en classe

class Pile:
    def __init__(self):
        self.data = []    #Créer la liste de la pile

    def EST_VIDE(self):
        if self.data == []:   #Vérifie si la pile est vide (=renvoie True) ou non (=renvoie False)
            return True
        else:
            return False

    def Empiler(self, valeur):
        self.data.append(valeur)      #Empile une valeur donnée

    def Dépiler(self):
        del self.data[-1]         #Dépile

    def __str__(self):
        return str(self.data) + " <- -> Entrée/Sortie"     # Interface donnant l'entrée et la sortie d'une pile avec print(nompile)

# Objet appartenant à la classe Pile

pile = Pile()

# File en classe

class File:
    def __init__(self):
        self.data = []      #Créer la liste de la file

    def EST_VIDE(self):
        if self.data == []:     #Vérifie si la file est vide
            return True
        else:
            return False

    def Enfiler(self, valeur):
        self.data.insert(0, valeur)     #Enfile

    def Défiler(self):
        del self.data[-1]       #Défile

    def __str__(self):
        return "Entrée -> " + str(self.data) + " -> Sortie" # Interface donnant l'entrée et la sortie d'une file avec print(nomfile)

b = File()
