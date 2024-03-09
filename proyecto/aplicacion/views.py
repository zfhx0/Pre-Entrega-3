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