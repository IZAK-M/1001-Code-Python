class Compte:
    nombre_comptes = 0
    taux_interet = 0.02
    def __init__(self, titulaire: str, num_compte: str, solde: float = 0):
        self.titulaire = titulaire
        self.num_compte = num_compte
        self.solde = solde
        self.historique = []
        Compte.nombre_comptes += 1

    def deposer(self, montant: float):
        if not isinstance(montant,(int, float)):
            raise TypeError("Le montant doit être un nombre")
        if montant <= 0:
            raise ValueError("Le montant doit être strictement positif")
        self.solde += montant
        self.historique.append({'type': 'dépôt', 'montant': montant, 'solde_apres': self.solde})

    def retirer(self, montant: float):
        if not isinstance(montant,(int, float)):
            raise TypeError("Le montant doit être un nombre")
        if self.solde <= 0:
            raise ValueError("Le montant doit être strictement positif")
        if self.solde < montant:
            raise ValueError(f"Solde insuffisant - disponible : {self.solde} €")
        self.solde -= montant

        self.historique.append({'type': 'retrait', 'montant': montant, 'solde_apres':self.solde})

    def afficher_solde(self):
        print(f"Compte {self.num_compte} — {self.titulaire} : {self.solde} €")

    def afficher_historique(self):
        print(f"--- Historique du compte {self.num_compte} ---")
        for i , e in enumerate(self.historique, start=1):
            if e["type"] == "dépôt":
                signe = "+"
            elif e["type"] == "retrait":
                signe = "-"
            else:
                signe = "*"
            print(f"{i}. {e['type']}   {signe}{e['montant']} -> solde : {e['solde_apres']}")

    def appliquer_interets(self):
        interets = round(self.solde * Compte.taux_interet, 2)
        self.solde += interets
        self.historique.append({'type': 'interet', 'montant': interets, 'solde_apres': self.solde})

