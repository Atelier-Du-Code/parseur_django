from django.shortcuts import get_object_or_404, render

from app_parseur.models import Evaluation
from app_upload.models import Document


def index(request):
    return render(request,"<h1>Page de la liste des documents parsés</h1>")
   

# Rendu des documents parsés
def liste_documents(request):
    documents = Document.objects.all()
    return render(request, 'display/liste_documents.html', {'documents': documents})

# Rendu de tous les audits
def liste_audits(request):
    audits = Evaluation.objects.all().order_by("-document__date_upload")
    return render(request, "display/liste_audits.html", {"audits": audits})

# Rendu d'un document complet
def afficher_document(request, evaluation_id):
   
    evaluation = get_object_or_404(Evaluation, id=evaluation_id)
    niveaux_eal = evaluation.niveaux_eal.all()

    return render(request, "display/doc_complet.html", {
        "evaluation": evaluation,
        "niveaux_eal": niveaux_eal
    })