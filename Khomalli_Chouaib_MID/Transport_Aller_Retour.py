from Offre_Voyage import Offre_Voyage


class Transport_Aller_Retour(Offre_Voyage):
    def __init__(self,Ref_Offre,Ville_de_depart,Ville_d_arrivee,VilleDepart,VilleArrivee,Prix,Date_Depart,Date_Arrivee):             #creation de la classe Offre de transport Aller/Retour qui herite depuis la classe offre_voyage       
        super().__init__(Ref_Offre,Ville_de_depart,Ville_d_arrivee)
        self.VID2=VilleDepart
        self.VIA2=VilleArrivee
        self.P1=Prix
        self.D1=Date_Depart
        self.D2=Date_Arrivee
    def saisir2(self):
        self.VID2=input("Entrer le nouvelle ville de depart: ")
        self.VIA2=input("Entrer le nouvelle ville d'arrivee: ")
        self.P1=float(input("Entrer le prix: "))
        self.D1.saisir()
        self.D2.saisir()
    def affichage2(self):
        print("Votre informations est bien enregistres: \n"
              +"La Ville de Depart: ",self.VID2 + '\n'
              +"La Ville d'Arrivee: ",self.VIA2 + '\n'
              +"Le Prix: ", str(self.P1) + ' DH'+'\n'
              "La Date de Depart: ",self.D1.affichage()+ '\n'
              +"La Date d'arrivee: ",self.D2.affichage())
    def sauvegarder2(self,NomFichier):
        with open(NomFichier,'a') as f:
           f.write(self.Donnees3() + '\n')
    def Donnees2(self):
       L3={'Votre informations pour l\'offre de Transport Aller Retour est bien enregistres:'}
       D2={'La Ville de Depart ': self.VID2,
           'La Ville d\'Arrivee': self.VIA2,                                                         
           'Le Prix': str(self.P1),
           'La Date de Depart': self.D1.affichage(),
           'La Date d\'arrivee': self.D2.affichage()}
       return str(L3) + '\n' + str(D3)