from django.db import models

class Document(models.Model):   
    nom_fichier = models.CharField(max_length=255)
    date_upload = models.DateTimeField(auto_now_add=True)
    fichier_pdf = models.FileField(upload_to='documents/')

