class Date ():
    def __init__(self,jour,mois,ans):
        self.jour=jour                                                             #creation de la classe date 
        self.mois=mois
        self.ans=ans

    def Saisir_Date(self):
        self.jour=int(input("saisir le jour :"))
        self.mois=int(input("saisir le mois :"))
        self.ans=int(input("saisir l'année :"))
        return str(self.jour)+'/'+str(self.mois)+'/'+str(self.ans)

    def __str__(self):
        return str(self.jour)+'/'+str(self.mois)+'/'+str(self.ans)
    