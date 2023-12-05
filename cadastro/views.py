from django.shortcuts import render
from cadastro.models import Usuarios

# Create your views here.

def index(request):
    return render( request, "cadastro/index.html")

def cadastrar(request):

    user =  Usuarios()
    user.nome = request.POST.get('Nome')
    user.idade = request.POST.get('Idade')
    user.save()

    return render(request, "cadastro/index.html")

def cadastrado(request):
    user = Usuarios.objects.all()
    context = {'user': user}
    return render(request, "cadastro/cadas.html", context)