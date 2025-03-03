
from django.shortcuts import render, redirect
from .models import Document
from app_parseur.utils import parse_pdf
from app_parseur.models import Evaluation, NiveauEAL

def upload_document(request):
    if request.method == "POST":
        fichier = request.FILES.get("fichier_pdf")
        if fichier:         
            document = Document.objects.create(nom_fichier=fichier.name, fichier_pdf=fichier)
           
            parsed_data = parse_pdf(document.fichier_pdf.path)

            evaluation = Evaluation.objects.create(
                document=document,
                nom_produit=parsed_data["nom_produit"],
                editeur=parsed_data["editeur"],
                version_produit=parsed_data["version"],
               
            )

            for niveau_data in parsed_data["niveaux_eal"]:
                NiveauEAL.objects.create(
                    evaluation=evaluation,
                    niveau=niveau_data["niveau"],
                    description=niveau_data["description"]
                )

            return redirect("doc_parses")

    return render(request, "upload/upload_docs.html")



def index(request):
    noDoc = 3
    return render(request,"upload/index.html", {"noDoc": noDoc})

