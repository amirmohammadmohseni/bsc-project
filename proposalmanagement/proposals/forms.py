from django import forms
from .models import Proposal


class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = [
            'title',
            'titlePersian',
            'keywords',
            'researchType',
            'file',
            'tarifMasale',
            'pishinehPazhuhesh',
            'ruykardHal',
            'premises',
            'jadidBudan',
            'raveshVaAbzar',
            'marajeHami',
        ]