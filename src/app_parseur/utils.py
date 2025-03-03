import pdfplumber
import re

def parse_pdf(file_path):   

    extracted_data = {
        "nom_produit": None,  
        "editeur": None,  
        "version": None,
        "description": None,
        "niveaux_eal": [] 
    }

    with pdfplumber.open(file_path) as pdf:
        page = pdf.pages[0]  # Cas dans lequel le PDF ne fait qu'une seule page
        texte = page.extract_text()

        if texte:
            # extracted_data["description"] = texte  # Stocke le texte complet
            
            # Extraction des informations générales
            match_nom = re.search(r"Nom du produit[:\s]*(.+)", texte)
            if match_nom:
                extracted_data["nom_produit"] = match_nom.group(1).strip()

            match_editeur = re.search(r"Éditeur[:\s]*(.+)", texte)
            if match_editeur:
                extracted_data["editeur"] = match_editeur.group(1).strip()

            match_version = re.search(r"Version du produit[:\s]*(.+)", texte)
            if match_version:
                extracted_data["version"] = match_version.group(1).strip()

        # Extraction des tableaux pour les niveaux EAL
        tables = page.extract_tables()
        if tables:
            for table in tables:
                for row in table[1:]:  # On ne récupère pas la première ligne 
                    if len(row) >= 2:  # Vérifie qu'il y a bien un niveau et une description sur la ligne
                        extracted_data["niveaux_eal"].append({ # Ajout des données au tableau
                            "niveau": row[0].strip(),  
                            "description": row[1].strip()  
                        })

    return extracted_data
