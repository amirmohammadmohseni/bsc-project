from django.urls import path

from .views import *

app_name = 'proposals'
urlpatterns = [
    path("add/", CreateProposal.as_view(), name="add"),
    path("edit/<int:pk>", EditProposal.as_view(), name="edit"),
    path("<int:id>/comments", showComments, name="comments")
]
