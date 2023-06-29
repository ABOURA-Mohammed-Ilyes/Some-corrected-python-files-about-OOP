# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

    def add_nom (noms, count) : 
        for i in range(count):
            nom = input(f"nom de la personne {i} : ")
            l.append(Personne(nom))

noms = []

l = []

for p in l:
    p.SePresenter()
    print()