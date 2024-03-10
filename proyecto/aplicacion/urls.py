from django.urls import path, include
from .views import *

urlpatterns = [
##########################################################################
    path('', home, name="home"),
##########################################################################
#                               Search                                   #
##########################################################################
    path('search_users/', buscar, name="search_users"),
    path('search_user/', users_search, name="search_users"),
##########################################################################
#                               Users                                    #
##########################################################################
    path('users', UserList.as_view(), name="users"),
    path('user_create', UserCreate.as_view(), name="user_create"),
    path('user_delete/<int:pk>', UserDelete.as_view(), name="user_delete"),
    path('user_update/<int:pk>', UserUpdate.as_view(), name='user_update'),
##########################################################################
#                               Cheques                                  #
##########################################################################
    path('cheques', ChequesList.as_view(), name="cheques"),
    path('cheques_create', ChequesCreate.as_view(), name="cheques_create"),
    path('cheque_delete/<int:pk>', ChequesDelete.as_view(), name="cheque_delete"),
    path('cheques_update/<int:pk>', ChequesUpdate.as_view(), name='cheques_update'),
##########################################################################
#                               Clientes                                 #
##########################################################################
    path('clientes', ClienteList.as_view(), name="clientes"),
    path('cliente_create', ClienteCreate.as_view(), name="cliente_create"),
    path('cliente_update/<int:pk>', ClienteUpdate.as_view(), name="cliente_update"),
    path('cliente_delete/<int:pk>', ClienteDelete.as_view(), name="cliente_delete"),
]
