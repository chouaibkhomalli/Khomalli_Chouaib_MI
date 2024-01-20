from datetime import datetime

class GestionnaireVoyages:
    def __init__(self):
        self.offres = []
        self.reservations = []

    def stats_nombre_offres_par_type(self):
        """
        Calcule le nombre d'offres par type.

        Returns:
            dict: Un dictionnaire contenant le nombre d'offres pour chaque type.
        """
        nombre_offres_par_type = {}
        for offre in self.offres:
            type_offre = offre.__class__.__name__
            if type_offre in nombre_offres_par_type:
                nombre_offres_par_type[type_offre] += 1
            else:
                nombre_offres_par_type[type_offre] = 1
        return nombre_offres_par_type

    def stats_nombre_offres_par_periode(self, debut, fin):
        """
        Calcule le nombre d'offres dans une période spécifiée.

        Args:
            debut (datetime): Date de début de la période.
            fin (datetime): Date de fin de la période.

        Returns:
            int: Le nombre d'offres dans la période.
        """
        nombre_offres_par_periode = 0
  

    def __init__(self):
        self.offres = []
        self.reservations = []

    def stats_nombre_offres_par_type(self):
        """
        #Calcule le nombre d'offres par type.

        Returns:
            dict: Un dictionnaire contenant le nombre d'offres pour chaque type.
        """
        nombre_offres_par_type = {}
        for offre in self.offres:
            type_offre = offre.__class__.__name__
            if type_offre in nombre_offres_par_type:
                nombre_offres_par_type[type_offre] += 1
            else:
                nombre_offres_par_type[type_offre] = 1
        return nombre_offres_par_type

    def stats_nombre_offres_par_periode(self, debut, fin):
        """
        Calcule le nombre d'offres dans une période spécifiée.

        Args:
            debut (datetime): Date de début de la période.
            fin (datetime): Date de fin de la période.

        Returns:
            int: Le nombre d'offres dans la période.
        """
        nombre_offres_par_periode = 0
        for offre in self.offres:
            if debut <= offre.date_depart <= fin:
                nombre_offres_par_periode += 1
        return nombre_offres_par_periode

    def stats_nombre_reservations(self, etat_reservation=None):
        """
        Calcule le nombre total de réservations ou le nombre de réservations pour un état spécifié.

        
        nombre_reservations = 0
        for reservation in self.reservations:
            if etat_reservation is None or reservation.etat_reservation == etat_reservation:
                nombre_reservations += 1
        return nombre_reservations

    def stats_nombre_reservations_par_periode(self, debut, fin):
        """
        Calcule le nombre de réservations dans une période spécifiée.

        
        nombre_reservations_par_periode = 0
        for reservation in self.reservations:
            if debut <= reservation.date_depart <= fin:
                nombre_reservations_par_periode += 1
        return nombre_reservations_par_periode

    def stats_chiffre_affaires_global(self):
        """
        Calcule le chiffre d'affaires global à partir des réservations.

        Returns:
            float: Le chiffre d'affaires total.
        """
        chiffre_affaires_global = 0
        for reservation in self.reservations:
            chiffre_affaires_global += reservation.total_a_payer
        return chiffre_affaires_global

    def stats_chiffre_affaires_par_periode(self, debut, fin):
        """
        Calcule le chiffre d'affaires dans une période spécifiée à partir des réservations.

        
        Returns:
            float: Le chiffre d'affaires dans la période spécifiée.
        """
        chiffre_affaires_par_periode = 0
        for reservation in self.reservations:
            if debut <= reservation.date_depart <= fin:
                chiffre_affaires_par_periode += reservation.total_a_payer
        return chiffre_affaires_par_periode


