from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('users', UserList.as_view(), name="users"),
    path('user_create', UserCreate.as_view(), name="user_create"),
    path('user_delete/<int:pk>', UserDelete.as_view(), name="user_delete"),


]
