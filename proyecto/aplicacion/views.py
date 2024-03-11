from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *

from django.views.generic import ListView, DeleteView, CreateView, UpdateView


# Create your views here.

def buscar(request):
    if request.methon == "POST":
        buscar = request.POST['buscar']
        return render(request, "aplicacion/templates/aplicacion/users_search.html", {'buscar':buscar})
    else:
        return render(request, "aplicacion/templates/aplicacion/users_search.html")



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

class ClienteCreate(CreateView):
    model = Cliente
    fields = ["nombre", "apellido", "email", "dni", "empresa"]
    success_url = reverse_lazy("clientes")

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy("clientes")

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ["nombre", "apellido", "email", "dni", "empresa"]
    success_url = reverse_lazy("clientes")

#pagos
class PagoList(ListView):
    model = PagoPendiente
    template_name = "aplicacion/pagos_list.html"
    context_object_name = 'pagos_list'

class PagoCreate(CreateView):
    model = PagoPendiente
    fields = ["deudor", "vencimiento", "monto", "numero", "perteneciente"]
    success_url = reverse_lazy("pagos")

class PagoDelete(DeleteView):
    model = PagoPendiente
    success_url = reverse_lazy("pagos")

class PagoUpdate(UpdateView):
    model = PagoPendiente
    fields = ["deudor", "vencimiento", "monto", "numero", "perteneciente"]
    success_url = reverse_lazy("pagos")