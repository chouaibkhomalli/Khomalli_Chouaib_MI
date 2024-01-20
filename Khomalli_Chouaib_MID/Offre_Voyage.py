class Offre_Voyage():
    def __init__(self, Ref_Offre, Ville_depart, Ville_arrivee):
        # création de la classe d'offre de voyage après avoir créé une fonction
        # afin que l'utilisateur saisisse les données et une fonction pour l'affichage
        self.Ref = Ref_Offre
        self.VID = Ville_depart
        self.VIA = Ville_arrivee
    
    def saisir(self):
        self.Ref = int(input("Entrer la nouvelle référence de l'offre: "))
        self.VID = input("Entrer la nouvelle ville de départ: ")
        self.VIA = input("Entrer la nouvelle ville d'arrivée: ")
    
    def affichage1(self):
        print("Référence de l'offre: ", str(self.Ref) + '\n'
              + "La Ville de Départ: ", self.VID + '\n'
              + "La Ville d'Arrivée: ", self.VIA)
    
    def Donnees(self):
        L = {'L\'offre de voyage est bien enregistrée:'}
        D = {'Référence de l\'offre': str(self.Ref),
             'La Ville de Départ': self.VID,
             'La Ville d\'Arrivée': self.VIA}
        return str(L) + '\n' + str(D)
    
    def sauvegarder1(self, NomFichier):
        with open(NomFichier, 'a') as file:
            file.write(self.Donnees() + '\n')
