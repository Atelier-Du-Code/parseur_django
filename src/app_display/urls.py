
from django.urls import path
from app_display.views import afficher_document, index, liste_audits, liste_documents


urlpatterns = [
    path('', index, name="index-display"),
    path('docs/', liste_documents, name="doc_parses"),
    path('audits/', liste_audits, name="liste_audits"),
    path('audit/<int:evaluation_id>/', afficher_document, name="afficher_document"),
]


