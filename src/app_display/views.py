from django.shortcuts import get_object_or_404, redirect, render

from app_display.models import AffichageDocument
from app_parseur.models import Evaluation, NiveauEAL
from app_parseur.form_audit import EvaluationForm, NiveauEALForm, NiveauEALFormSet
from app_upload.models import Document 

def index(request):
    return render(request,"<h1>Page de la liste des documents parsés</h1>")
   

# Rendu des documents parsés
def liste_documents(request):
    documents = Document.objects.all()
    return render(request, 'display/liste_documents.html', {'documents': documents})

# Rendu de tous les audits
def liste_audits(request):   
    audits = Evaluation.objects.select_related("affichagedocument")\
    .filter(affichagedocument__visible=True)\
    .order_by("-affichagedocument__date_affichage")
    return render(request, "display/liste_audits.html", {"audits": audits})

# Rendu d'un document complet
def afficher_document(request, evaluation_id):
   
    evaluation = get_object_or_404(Evaluation, id=evaluation_id)
    niveaux_eal = evaluation.niveaux_eal.all()

    return render(request, "display/doc_complet.html", {
        "evaluation": evaluation,
        "niveaux_eal": niveaux_eal
    })

# Création d'un audit 
def create_audit(request):
    if request.method == "POST":
        form_eval = EvaluationForm(request.POST)
        form_niveaux = NiveauEALFormSet(request.POST)

        if form_eval.is_valid() and form_niveaux.is_valid():
         
            evaluation = form_eval.save()

            affichage_data = AffichageDocument.objects.create(evaluation=evaluation)
           
            for form in form_niveaux:
                if form.cleaned_data.get("niveau"): 
                    niveau = form.save(commit=False)
                    niveau.evaluation = evaluation
                    niveau.save()

            return redirect('liste_audits')

    else:
        form_eval = EvaluationForm()
        form_niveaux = NiveauEALFormSet(queryset=NiveauEAL.objects.none())

    return render(request, "display/create_audit.html", {
        'form_eval': form_eval,
        'form_niveaux': form_niveaux,
    })

# Archivage d'un audit
def delete_audit(request, evaluation_id):
    
    evaluation = get_object_or_404(Evaluation, id=evaluation_id)
    
    affichage_document = evaluation.affichagedocument
    if affichage_document.visible is True:
        affichage_document.visible = False  
        affichage_document.save()

    return redirect('liste_audits') 