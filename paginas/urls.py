from django.urls import path
from . import views
urlpatterns = {
    path('index.html/', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),


}