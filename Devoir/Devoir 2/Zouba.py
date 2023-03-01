from datetime import date

class Grade:
    def __init__(self, code, libelle, taux):
        self.code = code
        self.libelle = libelle
        self.taux = taux

    def getCode(self):
        return self.code

    def getLibelle(self):
        return self.libelle

    def tauxHoraire(self):
        return self.taux

class Employe:
    def __init__(self, numero, nom, grade, dateEmbauche):
        self.numero = numero
        self.nom = nom
        self.grade = grade
        self.dateEmbauche = dateEmbauche

    def coutHoraire(self):
        anciennete = self.getAnciennete(self.dateEmbauche)
        taux = self.grade.tauxHoraire()

        if anciennete >= 5 and anciennete <= 10:
            taux *= 1.05
        elif anciennete >= 11 and anciennete <= 15:
            taux *= 1.08
        elif anciennete > 15:
            taux *= 1.12

        return taux

    def getNumero(self):
        return self.numero

    def getNom(self):
        return self.nom

    def getQualification(self):
        return self.grade

    def getDateEmbauche(self):
        return self.dateEmbauche

    def getAnciennete(self, date):
        return date.today().year - int(date[-4:])

class Client:
    def __init__(self, numero, nom, adresse, codePostale, ville, nbKm):
        self.numero = numero
        self.nom = nom
        self.adresse = adresse
        self.codePostale = codePostale
        self.ville = ville
        self.nbKm = nbKm

    def distance(self):
        return self.nbKm

class Intervention:
    def __init__(self, numero, date, duree, tarifkm, technicien):
        self.numero = numero
        self.date = date
        self.duree = duree
        self.tarifkm = tarifkm
        self.technicien = technicien

    def affiche(self):
        print("intervention n°{} du {} : {} heures".format(self.numero, self.date, self.duree))
        print("Coût kilométrique : {}f".format(self.tarifkm))
     
    def fraisKm(self, dist):
        return dist * self.tarifkm

   

class Contrat:
    def __init__(self, numero, date, client, montantContrat):
        self.numero = numero
        self.date = date
        self.client = client
        self.montantContrat = montantContrat
        self.interventions = []
        self.nbIntervention = 0

    def montant(self):
        return self.montantContrat

   