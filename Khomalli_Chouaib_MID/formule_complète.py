class formule_complète(Aller_Retour,hébergement):
    def _init_(self):
        Aller_Retour()._init_()
        hébergement()._init_()
        self.Type=''
        self.prix_total=0
        self.date=Date()
        self.DA=Date()                                                                                                               #creation de la classe formule comple qui herite depuis les classes ( transport_aller_retour et hebergement)
    def saisir4(self):
        print("Entrer les données d'Aller_Retour")
        super().saisir4()
        print("Entrer les données d'Hébergement")
        super().saisir3()
        self.Type=input("veuillez choisir votre type d'habitation (Week-End ou Semaine): ")
        self.prix_total=float(input("veuillez saisir le prix total: "))
    
    def affichage4(self):
        super().afficher3()
        super().afficher2()
        return print(f"Type (Week-End ou Semaine): {self.Type}\nLe prix totale:{self.prix_total}")                                  
    def bloquer(self):
       bloquer = input("Voulez-vous bloquer cette offre ? (Oui/Non) ")                                #creation d'une fonction bloquer qui permet à l'utilisateur de bloquer une offre  au lieu de lasupprimer du fichier          
       if bloquer.lower() == "oui":
         self.bloque = True
    def formule_complète(self):
        Dico_Aller_Retour= {'Ref_Offre' : self.Ref,
                      'Ville_départ': self.VD,
                      'Ville_arrivée':self.VA,
                      'Date_début': self.date.DateToStr(),
                      'Date_départ': self.date.DateToStr(),
                      'Date_arrivée': self.DA.DateToStr(),
                      'Prix':self.prix
                      
                      }
        return str(Dico_Aller_Retour)  