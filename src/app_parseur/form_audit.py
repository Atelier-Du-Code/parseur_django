from django import forms
from .models import Evaluation, NiveauEAL
from django.forms import modelformset_factory

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['document', 'nom_produit', 'editeur', 'version_produit']
        widgets = {
            'document': forms.HiddenInput(),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['document'].required = False

class NiveauEALForm(forms.ModelForm):
    class Meta:
        model = NiveauEAL
        fields = ['niveau', 'description']

NiveauEALFormSet = modelformset_factory(NiveauEAL, fields=['niveau', 'description'], extra=3)
