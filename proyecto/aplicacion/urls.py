from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
##########################################################################
#                               Users                                    #
##########################################################################
    path('users', UserList.as_view(), name="users"),
    path('user_create', UserCreate.as_view(), name="user_create"),
    path('user_delete/<int:pk>', UserDelete.as_view(), name="user_delete"),
    path('user_update/<int:pk>', UserUpdate.as_view(), name='user_update'),
##########################################################################
#                               Search                                   #
##########################################################################
    path('search_user/', SearchUser, name="search_user"),
    path('search_users/', SearchUsers, name="search_users"),
]
