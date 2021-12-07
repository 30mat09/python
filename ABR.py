class ABR:
    def __init__(self,v=None):
        self.valeur=v
        self.gauche=None
        self.droite=None
    def insertData(self,x):
        if(not(isinstance(x,int)) and not(isinstance(x,float))):
            return("Must be an integer")
        else:
            if(x>self.valeur):
                if(self.droite is None):
                    self.droite=ABR(x)
                else:
                    self.droite.insertData(x)
            elif(x<=self.valeur):
                if(self.gauche is None):
                    self.gauche=ABR(x)
                else:
                    self.gauche.insertData(x)
    def estVide(self):
        if(self.gauche is None and self.droite is None and self.valeur is None):
            return(True)
        else:
            return(False)
    def search(self,x):
        if(self.estVide()):
            return("Empty")
        else:
            if(x==self.valeur):
                return(True)
            elif(self.gauche is not None and x<=self.valeur):
                return(self.gauche.search(x))
            elif(self.droite is not None and x>self.valeur):
                return(self.droite.search(x))
            else:
                return(False)
    def infixe(self):
        if(self.estVide()):
            return([])
        elif(self.gauche is None and self.droite is None):
            return([self.valeur])
        else:
            if(self.gauche is None):
                return([self.valeur]+self.droite.infixe())
            elif(self.droite is None):
                return(self.gauche.infixe()+[self.valeur])
            else:
                return(self.gauche.infixe()+[self.valeur]+self.droite.infixe())
    def affichage(self,decalage=""):
        if(self.estVide()):
            print(f"{decalage}-")
        else:
            print(f"{decalage}{str(self.valeur)}")
            if(self.gauche is not None):
                self.gauche.affichage(decalage+"   ")
            else:
                print(f"{decalage}   -")
            if(self.droite is not None):
                self.droite.affichage(decalage+"   ")
            else:
                print(f"{decalage}   -")
    def max(self):
        if(self.droite is None):
            return(self.valeur)
        else:
            return(self.droite.max())
    def min(self):
        if(self.gauche is None):
            return(self.valeur)
        else:
            return(self.gauche.min())

def tri(liste):
    arbre=ABR(liste[0])
    for i in liste[1:]:
        arbre.insertData(i)
    return(arbre.infixe())

def occurence(n,liste):
    arbre=ABR(liste[0])
    for i in liste[1:]:
        arbre.insertData(i)
    return(n in arbre.infixe())

liste=[5,3,4,5,6,6,7]
root=ABR(5)
root.insertData(3)
root.insertData(4)
root.insertData(5)
root.insertData(6)
root.insertData(6)
root.insertData(7)