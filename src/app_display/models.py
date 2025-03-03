from django.db import models
from app_parseur.models import Evaluation

class AffichageDocument(models.Model):
    evaluation = models.OneToOneField(Evaluation, on_delete=models.CASCADE)
    date_affichage = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)

 
