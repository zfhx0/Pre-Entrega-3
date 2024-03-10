from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *

from django.views.generic import ListView, DeleteView, CreateView, UpdateView


# Create your views here.




def home(request):
    return render(request, "aplicacion/index.html") 

def users_search(request):
    return render(request, "users_search.html") 

#users
class UserList(ListView):
    model = User
    template_name = "aplicacion/User_list.html"
    context_object_name = 'User_list'

class UserCreate(CreateView):
    model = User
    fields = ["nombre", "apellido", "email", "dni"]
    success_url = reverse_lazy("users")

class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy("users")

class UserUpdate(UpdateView):
    model = User
    fields = ["nombre", "apellido", "email", "dni"]
    success_url = reverse_lazy("users")

def buscar(request):
    cadena = request.GET.get('cadena')
    if cadena:
        resultados = User.objects.filter(nombre__icontains=cadena)
    else:
        resultados = None
    return render(request, 'users_search.html', {'resultados': resultados})

#cheques
class ChequesList(ListView):
    model = Cheques
    template_name = "aplicacion/Cheques_list.html"
    context_object_name = 'Cheques_list'

class ChequesCreate(CreateView):
    model = Cheques
    fields = ["banco", "fecha", "monto", "numero", "perteneciente"]
    success_url = reverse_lazy("cheques")

class ChequesDelete(DeleteView):
    model = Cheques
    success_url = reverse_lazy("cheques")

class ChequesUpdate(UpdateView):
    model = Cheques
    fields = ["banco", "fecha", "monto", "numero", "perteneciente"]
    success_url = reverse_lazy("cheques")

#clientes
    
class ClienteList(ListView):
    model = Cliente
    template_name = "aplicacion/Clientes_list.html"
    context_object_name = 'Clientes_list'

class UserCreate(CreateView):
    model = Cliente
    fields = ["nombre", "apellido", "email", "dni"]
    success_url = reverse_lazy("clientes")

class UserDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy("clientes")

class UserUpdate(UpdateView):
    model = Cliente
    fields = ["nombre", "apellido", "email", "dni"]
    success_url = reverse_lazy("clientes")