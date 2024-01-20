class Hebergement(Offre_voyage):
    def __init__(self , ref_offre , ville_depart , ville_arrivee, date_debut, nombre_nuit , type , prix_nuit):
        super().__init__(ref_offre , ville_depart , ville_arrivee)
        self.date_debut = Date(0,0,0)
        self.nombre_nuit = nombre_nuit                                                                                                                                                                                                                              #creation de la classe hebergement et qui herite depuis la classe offre_voyage et creation des fonctions de saisies et d'affichage et de sauvegarde des données dans le fichier 
        self.type = type
        self.prix_nuit = prix_nuit
        self.bloquer = False

    def affichage3(self):
        print(f"Type: Hebergement, Référence: {self.ref_offre}, Départ: {self.ville_depart}, Arrivée: {self.ville_arrivee}, Date de debut: {self.date_debut},Nombre de nuit: {self.nombre_nuit}, Type: {self.type},Prix par nuit: {self.prix_nuit}")

    def Saisir_Hebergement(self):
        self.Saisir_Offre_Voyage()
        self.date_debut=self.date_debut.saisir_date("Entrer la date du debut : ")
        self.nombre_nuit=input("Entrer le nombre de nuit  : ")
        self.type=input("Entrer le type : (déjeuner, demi-pension, pension complète)  ")
        self.prix_nuit=input("Entrer le prix de nuit : ")
                      
 
    def ligneHebergement(self):
            return (
                f"Reference du offre  : {self.ref_offre}, \n"
                f"Ville de depart : {self.ville_depart},\n "
                f"Ville d arrivee: {self.ville_arrivee},\n "
                f"Date de debut : {self.date_debut},\n "
                f"Nombre de nuit : {self.nombre_nuit},\n "
                f"Type : {self.type},\n "
                f"Prix par nuit :{self.prix_nuit},\n  ")
    
    def SauvegarderDansFichier(self, NomFichier):
         with open(NomFichier, 'a') as F:
             F.write(self.ligneHebergement())