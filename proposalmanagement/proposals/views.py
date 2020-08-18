from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Proposal
from users.models import Student


class CreateProposal(CreateView):
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
    template_name = 'proposals/add.html'
    success_url = '/user/dashboard'

    def form_valid(self, form):
        form.instance.student = Student.objects.get(id=self.request.user.baseuser.id)
        return super().form_valid(form)
