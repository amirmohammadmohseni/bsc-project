from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from proposals.models import Comment, Proposal
from .models import Student, Professor


def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def dashboard(request):
    user = request.user
    context = {'is_ST': user.baseuser.role == 'ST'}
    if context['is_ST']:
        context['requser'] = Student.objects.get(id=user.baseuser.pk)
        context['proposal'] = Proposal.objects.filter(student=context['requser']).first()
        context['NOComments'] = Comment.objects.filter(onProposal=context['proposal']).count()
    else:
        context['requser'] = Professor.objects.get(id=user.baseuser.id)
        context['is_manager'] = context['requser'].group.manager.id == context['requser'].id
        context['students'] = Student.objects.filter(advisorProf=context['requser'])
        context['sp_proposals'] = Proposal.objects.filter(student__in=context['students'])
        context['rvw_proposals'] = list(Proposal.objects.filter(arbiter1=context['requser'])) + list(
            Proposal.objects.filter(arbiter2=context['requser']))
        if context['is_manager']:
            context['proposals'] = Proposal.objects.all()
    print(context)
    return render(request, 'users/dashboard.html', context)
