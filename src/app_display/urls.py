
from django.urls import path
from app_display.views import afficher_document, index, liste_audits, liste_documents, create_audit, delete_audit


urlpatterns = [
    path('', index, name="index-display"),
    path('docs/', liste_documents, name="doc_parses"),
    path('audits/', liste_audits, name="liste_audits"),
    path('create_audit/', create_audit, name="create_audit"),
    path('delete_audit/<int:evaluation_id>/', delete_audit, name="delete_audit"),
    
    path('audit/<int:evaluation_id>/', afficher_document, name="afficher_document"),
]


