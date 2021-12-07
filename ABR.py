class ABR: #Arbre Binaire de Recherche
    def __init__(self,v=None):
        self.data=v
        self.left=None
        self.right=None
    def insertData(self,x):
        if(not(isinstance(x,int)) and not(isinstance(x,float))):
            return("Must be an integer")
        else:
            if(x>self.data):
                if(self.right is None):
                    self.right=ABR(x)
                else:
                    self.right.insertData(x)
            elif(x<=self.data):
                if(self.left is None):
                    self.left=ABR(x)
                else:
                    self.left.insertData(x)
    def estVide(self):
        if(self.left is None and self.right is None and self.data is None):
            return(True)
        else:
            return(False)
    def search(self,x):
        if(self.estVide()):
            return("Empty")
        else:
            if(x==self.data):
                return(True)
            elif(self.left is not None and x<=self.data):
                return(self.left.search(x))
            elif(self.right is not None and x>self.data):
                return(self.right.search(x))
            else:
                return(False)
    def infixe(self):
        if(self.estVide()):
            return([])
        elif(self.left is None and self.right is None):
            return([self.data])
        else:
            if(self.left is None):
                return([self.data]+self.right.infixe())
            elif(self.right is None):
                return(self.left.infixe()+[self.data])
            else:
                return(self.left.infixe()+[self.data]+self.right.infixe())
    def affichage(self,decalage=""):
        if(self.estVide()):
            print(f"{decalage}-")
        else:
            print(f"{decalage}{str(self.valeur)}")
            if(self.left is not None):
                self.left.affichage(decalage+"   ")
            else:
                print(f"{decalage}   -")
            if(self.right is not None):
                self.right.affichage(decalage+"   ")
            else:
                print(f"{decalage}   -")
    def max(self):
        if(self.right is None):
            return(self.data)
        else:
            return(self.right.max())
    def min(self):
        if(self.left is None):
            return(self.data)
        else:
            return(self.left.min())

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
