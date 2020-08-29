from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Proposal)
admin.site.register(ProposalSubmission)
admin.site.register(Comment)
