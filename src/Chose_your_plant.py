"""Docstring
    @Description: Chose your Plant est une app qui vous aide à choisir votre plantes idéal ! 
    @Author: ELISE & MAXIME
"""
import os
import sys

class Plante:
    def __init__(self, name: str, type: str, description: str, uv: str):
        self.name = name
        self.type = type
        self.description = description
        self.uv = uv

    # Getters & Setters
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @name.deleter
    def name(self):
        raise Exception("Tu ne peux supprimer le nom d'une plante!")
    
    @property 
    def type(self):
        return self._type
    
    @type.setter
    def type(self, value):
        self._type = value
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        self._description = value
    
    @property
    def uv(self):
        return self._uv
    
    @uv.setter
    def uv(self, value):
        self._uv = value
    

class PlanteExterieur(Plante):
    def __init__(self, name: str, type: str, description: str, uv: str):
        super().__init__(name, type, description, uv)

class PlanteInterieur(Plante):
    def __init__(self, name: str, type: str, description: str, uv: str):
        super().__init__(name, type, description, uv)

class Terminal: 
    def __init__(self):
        self.plantes_interieur = [
            PlanteInterieur("Figuier caoutchouc", "Arbuste", "Plante au feuillage épais et brillant, facile d'entretien, idéale pour les débutants.", "Faible à modérée"),
            PlanteInterieur("Langue de belle-mère", "Plante grasse", "Plante robuste aux feuilles verticales et rigides, connue pour sa capacité à purifier l'air.", "Modérée à forte"),
            PlanteInterieur("Pothos", "Plante grimpante", "Plante grimpante populaire avec des feuilles en forme de cœur, parfaite pour les suspensions.", "Faible à modérée"),
            PlanteInterieur("Aloe Vera", "Plante grasse", "Plante médicinale aux feuilles épaisses et gélatineuses, reconnue pour ses propriétés apaisantes.", "Forte"),
            PlanteInterieur("Dracaena marginata", "Arbuste", "Plante au port élancé avec des feuilles fines et bordées de rouge, apportant une touche exotique.", "Faible à modérée"),
            PlanteInterieur("Lys de paix", "Plante à fleurs", "Plante élégante avec des fleurs blanches délicates et des feuilles vert foncé, appréciée pour sa capacité à purifier l'air.", "Faible à modérée"),
            PlanteInterieur("Fleur de porcelaine", "Plante grimpante", "Plante grimpante avec des feuilles cireuses et des fleurs étoilées parfumées.", "Modérée"),
            PlanteInterieur("Zamioculcas zamiifolia", "Plante herbacée", "Plante robuste et facile d'entretien avec des feuilles lustrées, idéale pour les environnements à faible luminosité.", "Faible à modérée"),
            PlanteInterieur("Arbre de jade", "Plante grasse", "Plante succulente aux feuilles épaisses et charnues, symbolisant la chance et la prospérité.", "Forte"),
            PlanteInterieur("Cactus colonnaire", "Cactus", "Cactus imposant avec une forme colonnaire, idéal pour apporter une touche désertique à l'intérieur.", "Forte")
        ]
        
        self.plantes_exterieur = [
            PlanteExterieur("Rosier", "Arbuste à fleurs", "Arbuste classique aux fleurs parfumées et colorées, symbole de beauté et d'élégance.", "Forte"),
            PlanteExterieur("Lavande", "Plante herbacée", "Plante méditerranéenne aux fleurs mauves et parfumées, idéale pour les bordures et les jardins aromatiques.", "Forte"),
            PlanteExterieur("Lierre", "Plante grimpante", "Plante grimpante vigoureuse avec des feuilles persistantes, parfaite pour couvrir les murs et les clôtures.", "Faible à modérée"),
            PlanteExterieur("Buis", "Arbuste", "Arbuste à feuillage dense et persistant, souvent utilisé pour les haies et les topiaires.", "Modérée à forte"),
            PlanteExterieur("Hortensia", "Arbuste à fleurs", "Arbuste aux grandes inflorescences colorées, apportant une touche romantique aux jardins ombragés.", "Faible à modérée"),
            PlanteExterieur("Herbe des fontaines", "Plante herbacée", "Graminée ornementale avec des épis plumeux, ajoutant du mouvement et de la texture aux jardins.", "Forte"),
            PlanteExterieur("Sauge", "Plante herbacée", "Plante aromatique aux feuilles gris-vert et aux fleurs bleu-violet, souvent utilisée en cuisine et en médecine.", "Forte"),
            PlanteExterieur("Agapanthe", "Plante herbacée", "Plante avec de grandes ombelles de fleurs bleues ou blanches, idéale pour les massifs et les bordures.", "Modérée à forte"),
            PlanteExterieur("Genévrier commun", "Arbuste conifère", "Conifère résistant au feuillage persistant et aux baies décoratives, utilisé pour les haies et les rocailles.", "Forte"),
            PlanteExterieur("Achillée millefeuille", "Plante herbacée", "Plante vivace avec des tiges florales dressées et des fleurs en ombelles, attirant les pollinisateurs.", "Forte")
        ]

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def app_initialize(self):
        self.clear_terminal()

    def app_launch(self):
        print("Bienvenue sur l'application Choose Your Plant")

    def app_menu(self):
        while True:
            print("\nMenu Principal:")
            print("1) Choisir une plante d'intérieur")
            print("2) Choisir une plante d'extérieur")
            print("3) Filtrer les plantes")
            print("4) Quitter")
            user_choice = int(input("Faites votre choix: "))

            if user_choice == 1:
                self.choose_plant(self.plantes_interieur)
            elif user_choice == 2:
                self.choose_plant(self.plantes_exterieur)
            elif user_choice == 3:
                self.filter_plants()
            elif user_choice == 4:
                self.app_quit()
            else:
                print("Choix invalide. Veuillez réessayer.")

    def choose_plant(self, plantes):
        print("\nVoici les plantes actuellement disponibles:")
        print("\n0) Retour au menu précédent")
        for i, plante in enumerate(plantes, 1):
            print(f"{i}) {plante.name}")

        plant_choice = int(input("Choisissez une plante: ")) - 1

        if plant_choice == -1:
            return
        elif 0 <= plant_choice < len(plantes):
            chosen_plant = plantes[plant_choice]
            self.display_plant_info(chosen_plant)
        else:
            print("Choix invalide. Retour au menu principal.")

    def filter_plants(self):
        while True:
            print("\nFiltrer les plantes par:")
            print("0) Retour au menu précédent")
            print("1) Catégorie UV")
            print("2) Catégorie Type")
            filter_choice = int(input("Faites votre choix: "))

            if filter_choice == 0:
                return
            elif filter_choice == 1:
                self.filter_by_uv()
            elif filter_choice == 2:
                self.filter_by_type()
            else:
                print("Choix invalide. Veuillez réessayer.")

    def filter_by_uv(self):
        all_plants = self.plantes_interieur + self.plantes_exterieur
        uv_levels = list(set(plante.uv for plante in all_plants))
        print("\nVoici les plantes actuellement disponibles par UV:")
        print("\n0) Retour au menu précédent")
        for i, uv in enumerate(uv_levels, 1):
            print(f"{i}) {uv}")
        uv_choice = int(input("Choisissez un niveau UV: ")) - 1

        if uv_choice == -1:
            return
        elif 0 <= uv_choice < len(uv_levels):
            chosen_uv = uv_levels[uv_choice]
            filtered_plantes = [plante for plante in all_plants if plante.uv == chosen_uv]
            
            self.choose_plant(filtered_plantes)
        else:
            print("Choix invalide. Retour au menu principal.")

    def filter_by_type(self):
        all_plants = self.plantes_interieur + self.plantes_exterieur
        types = list(set(plante.type for plante in all_plants))
        print("\nVoici les plantes actuellement disponibles par type:")
        print("\n0) Retour au menu précédent")
        for i, type in enumerate(types, 1):
            print(f"{i}) {type}")
        type_choice = int(input("Choisissez un type de plante: ")) - 1

        if type_choice == -1:
            return
        elif 0 <= type_choice < len(types):
            chosen_type = types[type_choice]
            filtered_plantes = [plante for plante in all_plants if plante.type == chosen_type]
            
            self.choose_plant(filtered_plantes)
        else:
            print("Choix invalide. Retour au menu principal.")

    def display_plant_info(self, plante):
        print("\nInformations sur la plante choisie:")
        print(f"Nom: {plante.name}")
        print(f"Type: {plante.type}")
        print(f"Description: {plante.description}")
        print(f"UV: {plante.uv}")
        buy_choice = input("Voulez-vous acheter cette plante ? (oui/non) : ").strip().lower()
        if buy_choice == 'oui':
            print("Merci pour votre achat!")
        elif buy_choice == 'non':
            print("D'accord, retour au menu principal.")
        else:
            print("Réponse non valide. Retour au menu principal.")

    def app_quit(self):
        print("Merci d'avoir utilisé l'application. Au revoir!")
        sys.exit()

def main():
    app_instance = Terminal()
    app_instance.app_initialize()
    app_instance.app_launch()
    app_instance.app_menu()

if __name__ == "__main__":
    main()
