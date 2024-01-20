class Reservation :
    def __init__(self, ref_reservation , type_offre , ref_offre , date_depart , date_retour, genre , nom , prenom , nationalite , num_passeport , etat_reservation , total_payer):
        self.ref_reservation = ref_reservation
        self.type_offre = type_offre
        self.ref_offre = ref_offre
        self.date_depart = date_depart
        self.date_retour = date_retour
        self.genre = genre
        self.nom = nom
        self.prenom = prenom
        self.nationalite = nationalite
        self.num_passeport = num_passeport
        self.etat_reservation = etat_reservation
        self.total_payer = total_payer

    def faire_reservation(self, gestionnaire):
        ref_reservation = input("Entrez la référence de la réservation : ")
        type_offre = input("Entrez le type d'offre (Transport Aller Simple, Transport Aller/Retour, Hebergement, Formule Complete) : ")
        ref_offre = input("Entrez la référence de l'offre associée à la réservation : ")
        date_depart = input("Entrez la date de départ (format JJ/MM/AAAA) : ")
        date_retour = input("Entrez la date de retour (format JJ/MM/AAAA) : ")
        genre = input("Entrez le genre (Homme/Femme) : ")
        nom = input("Entrez le nom : ")
        prenom = input("Entrez le prénom : ")
        nationalite = input("Entrez la nationalité : ")
        num_passeport = input("Entrez le numéro de passeport : ")
        etat_reservation = "en cours" 
        total_payer = 0  # a completer

        nouvelle_reservation = Reservation(ref_reservation, type_offre, ref_offre, date_depart, date_retour, genre, nom, prenom, nationalite, num_passeport, etat_reservation, total_payer)
        # Ajoutez la nouvelle réservation à la liste des réservations du gestionnaire
        gestionnaire.reservation.append(nouvelle_reservation)

    def confirmer_reservation(self):
        if self.etat_reservation == "en cours":
            self.etat_reservation = "confirmée"
            print("Réservation confirmée.")
        else:
            print("Impossible de confirmer cette réservation ")

    def annuler_reservation(self):
        if self.etat_reservation == "en cours":
            self.etat_reservation = "annulée"                                             #creation d'une fonction qui permert de savoir l'etat de la reservation
            print("Réservation annulée.")
        else:
            print("Impossible d'annuler cette réservation ")

    def ligneReservation(self):
        return (
            f"Reference de reservation : {self.ref_reservation}, \n"
            f"Type d offre : {self.type_offre},\n"
            f"Referene du offre : {self.ref_offre},\n"
            f"Date de depart : {self.date_depart},\n"
            f"Date de retour : {self.date_retour},\n"
            f"Le genre : {self.genre},\n"
            f"Le nom : {self.nom},\n"
            f"Le prenom : {self.prenom},\n"
            f"Nationalitee : {self.nationalite},\n"
            f"Num_Passport : {self.num_passeport},\n"
            f"Etat de reservation : {self.etat_reservation},\n"
            f"Total payer : {self.total_payer},\n"
            )
    def  SauvegarderDansFichier(self, NomFichier):
         with open(NomFichier, 'a') as F:
             F.write(self.ligneReservation())        
