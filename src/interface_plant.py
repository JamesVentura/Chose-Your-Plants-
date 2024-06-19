"""Docstring
    @Description: Chose your Plant est une app qui vous aide à choisir votre plantes idéal ! 
    @Author: ELISE & MAXIME 
    @Make With IA 
"""

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

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
    
class InterfaceParam ():
    font_size_title=20
    font_size_txt=15


class PlanteExterieur(Plante):
    def __init__(self, name: str, type: str, description: str, uv: str):
        super().__init__(name, type, description, uv)

class PlanteInterieur(Plante):
    def __init__(self, name: str, type: str, description: str, uv: str):
        super().__init__(name, type, description, uv)

class PlantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Choose Your Plant")
        self.root.geometry("800x600")

        # Load images for background and buttons
        self.bg_image = ImageTk.PhotoImage(Image.open("src/background.jpg").resize((800, 600)))
        self.icon_image = ImageTk.PhotoImage(Image.open("src/icon.png").resize((20, 20)))

        self.background_label = tk.Label(self.root, image=self.bg_image)
        self.background_label.place(relwidth=1, relheight=1)

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

        self.main_menu()

    def main_menu(self):
        self.clear_frame()

        tk.Label(self.root, text="Bienvenue sur l'application Choose Your Plant", bg="white", font=("Helvetica", InterfaceParam.font_size_title)).pack(pady=10)

        self.create_button("Choisir une plante d'intérieur", lambda: self.choose_plant(self.plantes_interieur)).pack(pady=5)
        self.create_button("Choisir une plante d'extérieur", lambda: self.choose_plant(self.plantes_exterieur)).pack(pady=5)
        self.create_button("Filtrer les plantes", self.filter_plants).pack(pady=5)
        self.create_button("Quitter", self.root.quit).pack(pady=5)

    def create_button(self, text, command):
        button = tk.Button(self.root, text=text, command=command, compound="left", image=self.icon_image)
        return button

    def choose_plant(self, plantes):
        self.clear_frame()

        tk.Button(self.root, text="Retour au menu précédent", command=self.main_menu, compound="left", image=self.icon_image).pack(pady=5)

        tk.Label(self.root, text="Voici les plantes actuellement disponibles:", bg="white", font=("Helvetica", InterfaceParam.font_size_txt)).pack(pady=10)

        for i, plante in enumerate(plantes, 1):
            tk.Button(self.root, text=f"{i}) {plante.name}", command=lambda p=plante: self.display_plant_info(p), compound="left", image=self.icon_image).pack(pady=2)

    def filter_plants(self):
        self.clear_frame()

        tk.Button(self.root, text="Retour au menu précédent", command=self.main_menu, compound="left", image=self.icon_image).pack(pady=5)
        self.create_button("Filtrer par UV", self.filter_by_uv).pack(pady=5)
        self.create_button("Filtrer par type", self.filter_by_type).pack(pady=5)

    def filter_by_uv(self):
        self.clear_frame()
        all_plants = self.plantes_interieur + self.plantes_exterieur
        uv_levels = list(set(plante.uv for plante in all_plants))
        
        tk.Button(self.root, text="Retour au menu précédent", command=self.filter_plants, compound="left", image=self.icon_image).pack(pady=5)

        tk.Label(self.root, text="Voici les plantes actuellement disponibles par UV:", bg="white", font=("Helvetica", InterfaceParam.font_size_title)).pack(pady=10)

        for i, uv in enumerate(uv_levels, 1):
            tk.Button(self.root, text=f"{i}) {uv}", command=lambda u=uv: self.choose_plant([p for p in all_plants if p.uv == u]), compound="left", image=self.icon_image).pack(pady=2)

    def filter_by_type(self):
        self.clear_frame()
        all_plants = self.plantes_interieur + self.plantes_exterieur
        types = list(set(plante.type for plante in all_plants))
        
        tk.Button(self.root, text="Retour au menu précédent", command=self.filter_plants, compound="left", image=self.icon_image).pack(pady=5)

        tk.Label(self.root, text="Voici les plantes actuellement disponibles par type:", bg="white", font=("Helvetica", InterfaceParam.font_size_title)).pack(pady=10)

        for i, type in enumerate(types, 1):
            tk.Button(self.root, text=f"{i}) {type}", command=lambda t=type: self.choose_plant([p for p in all_plants if p.type == t]), compound="left", image=self.icon_image).pack(pady=2)

    def display_plant_info(self, plante):
        self.clear_frame()

        tk.Button(self.root, text="Retour au menu précédent", command=self.main_menu, compound="left", image=self.icon_image).pack(pady=5)

        tk.Label(self.root, text=f"Nom: {plante.name}", bg="white", font=("Helvetica",InterfaceParam.font_size_title)).pack(pady=2)
        tk.Label(self.root, text=f"Type: {plante.type}", bg="white", font=("Helvetica", InterfaceParam.font_size_title)).pack(pady=2)
        tk.Label(self.root, text=f"Description: {plante.description}", bg="white", font=("Helvetica", InterfaceParam.font_size_title)).pack(pady=2)
        tk.Label(self.root, text=f"UV: {plante.uv}", bg="white", font=("Helvetica", InterfaceParam.font_size_title)).pack(pady=2)

        buy_choice = tk.messagebox.askquestion("Achat", "Voulez-vous acheter cette plante ?")
        if buy_choice == 'yes':
            tk.messagebox.showinfo("Merci", "Merci pour votre achat!")
        else:
            tk.messagebox.showinfo("Retour", "D'accord, retour au menu principal.")

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.background_label = tk.Label(self.root, image=self.bg_image)
        self.background_label.place(relwidth=1, relheight=1)


def main():
    root = tk.Tk()
    app = PlantApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()