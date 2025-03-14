from django.db import models
from app_upload.models import Document

class Evaluation(models.Model):
    document = models.OneToOneField(Document, on_delete=models.CASCADE, blank=True, null=True)
    nom_produit = models.CharField(max_length=255)
    editeur = models.CharField(max_length=255) 
    version_produit = models.CharField(max_length=100, blank=True, null=True)  
  

class NiveauEAL(models.Model):
    DATA_NIVEAU = [
        ('EAL2+', 'EAL2+'),
        ('EAL3', 'EAL3'),
        ('EAL4', 'EAL4'),
    ]
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE, related_name="niveaux_eal")
    niveau = models.CharField(max_length=255, choices= DATA_NIVEAU, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
