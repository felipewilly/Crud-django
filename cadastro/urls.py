from django.urls import path
from cadastro import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('cadastrado/', views.cadastrado, name='cadastrado'),
]
