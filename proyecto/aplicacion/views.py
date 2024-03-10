from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *

from django.views.generic import ListView, DeleteView, CreateView, UpdateView


# Create your views here.




def home(request):
    return render(request, "aplicacion/index.html") 

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

def SearchUser(request):
    return render(request, "aplicacion/search.html")

def SearchUsers(request):
    if request.GET["search"]:
        cadena = request.GET["search"]
        Users = User.objects.filter(nombre__icontains=cadena)
        context = {"User": Users}
        return render(request, "aplicacion/search.html", context)


    context = {'User': Users.objects.all()}
    return render(request, "aplicacion/search.html", context)

#def SearchUsers(request):
#    cadena = request.GET.get('search')  
#    if cadena:
#        users = User.objects.filter(nombre__icontains=cadena)
#    else:
#        users = User.objects.all()

#    context = {"users": users}
#    return render(request, "aplicacion/User_list.html", context)