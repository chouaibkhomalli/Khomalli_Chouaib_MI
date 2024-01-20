from datetime import date  # Ajout de l'importation nécessaire pour la classe Date

class AllerSimple(Offre_voyage):
    def __init__(self, ref_offre, ville_depart, ville_arrivee, prix):
        super().__init__(ref_offre, ville_depart, ville_arrivee)
        self.date = date(1900, 1, 1)  # Initialisation de la date avec une valeur par défaut
        self.prix = prix

    def afficher(self):
        print(f"Type: Transport Aller Simple, Référence: {self.ref_offre}, Départ: {self.ville_depart}, Arrivée: {self.ville_arrivee}, Date: {self.date}, Prix: {self.prix}")

    def Saisie_Aller_simple(self):
        self.Saisir_Offre_Voyage()
        self.prix = float(input("Entrer le prix: "))  # Conversion de l'entrée en nombre à virgule flottante
        self.date = self.date.Saisir_Date("Entrer la date de départ : ")  # Suppression du "self."

    def update_prix(self, prix):
        self.prix = prix

    def update_date(self):
        self.date = date(1900, 1, 1)
        self.date = self.date.Saisir_Date("Entrez la nouvelle date : ")

    def ligneTransportAller(self):
        return (
            f"Reference du offre  : {self.ref_offre}, \n"
            f"Ville de depart : {self.ville_depart},\n "
            f"Ville d arrivee: {self.ville_arrivee},\n "
            f"Date de depart : {self.date},\n "
            f"Prix :{self.prix},\n  "
        )

    def SauvegarderDansFichier(self, NomFichier):
        with open(NomFichier, 'a') as F:
            F.write(self.ligneTransportAller())
