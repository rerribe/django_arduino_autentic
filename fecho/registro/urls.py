from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views
#from django.urls import include, re_path

from django.urls import re_path as url






urlpatterns = [
    path('', views.inicial, name='inicial'),
    path('registro',views.registro_page, name='registro'),
    url(r'^api/registro_user$',views.registro_user,name='registro_user'),
    path('resposta1',views.resposta1, name='resposta1'),
    path('resposta/', views.resposta, name='resposta'),
    path('resposta_arduino',views.resposta_arduino, name='resposta_arduino'),
]