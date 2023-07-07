
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("",views.index, name="home"),
    path("signup/",views.signup, name="signup"),
    path("signin/",views.signin, name="signin"),
    path("logout/",views.signout,name="logout"),
    path("about/",views.about, name="about"),
    path("principal/",views.principal, name="principal"),

    #Inquilinos
    path("inquilinosinicial/", views.inquilinosinicial, name="inquilinosinicial"),
    path("inquilinos/",views.inquilinos, name="inquilinos"),
    
    

    #Visitantes

    #Trabajadores
    
   # Guia
    path("",views.IndexView.as_view(), name="home"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]