from django.urls import path
from . import views

app_name = 'proposals'
urlpatterns = [
    path("add/", views.CreateProposal.as_view(), name="add"),
    path("<int:id>/comments", views.showComments, name="comments")
]
