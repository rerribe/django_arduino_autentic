from django.urls import path
from django.views.decorators.csrf import csrf_exempt
#from django.conf.urls import url
from . import views



urlpatterns = [
    path('', views.inicial, name='inicial'),
    path('registro',views.registro_page, name='registro'),
    path('resposta1',views.resposta1, name='resposta1'),
    path('resposta/', views.resposta, name='resposta'),
    path('resposta_arduino',views.resposta_arduino, name='resposta_arduino')
]