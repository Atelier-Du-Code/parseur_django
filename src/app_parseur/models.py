from django.db import models
from app_upload.models import Document

class Evaluation(models.Model):
    document = models.OneToOneField(Document, on_delete=models.CASCADE)
    nom_produit = models.CharField(max_length=255)
    editeur = models.CharField(max_length=255) 
    version_produit = models.CharField(max_length=100, blank=True, null=True)  
  

class NiveauEAL(models.Model):
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE, related_name="niveaux_eal")
    niveau = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
