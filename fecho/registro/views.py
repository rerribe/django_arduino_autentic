from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .serial_teste import*

import os
import sys
import subprocess

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view
from registro.serializers import RegistroSerializer 
from registro.models import Registro

#from .forms import Registrar



@csrf_exempt


def inicial(request):
	return render(request,'registro/inicial.html')

@csrf_exempt
@api_view(['GET', 'POST', 'DELETE'])
def registro_user(request):
    if request.method == 'GET':
        registro = Registro.objects.all()
        
        nome = request.GET.get('nome', None)
        if nome is not None:
            registro = registro.filter(nome__icontains=nome)
        
        registro_serializer = RegistroSerializer(registro, many=True)
        return JsonResponse(registro_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        print(request)
        registro_data = JSONParser().parse(request)
        registro_serializer = RegistroSerializer(data=registro_data)
        if registro_serializer.is_valid():
            registro_serializer.save()
            return JsonResponse(registro_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(registro_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Registro.objects.all().delete()
        return JsonResponse({'message': '{} usuario excluido com sucesso'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

	

@csrf_exempt
def resposta1(request):
    if request.method == 'POST':
        getData = request.body
        print(request.body)
        return JsonResponse({'text': getData.body})
    else:
        return HttpResponse('teste')

@csrf_exempt
def resposta(request):
    if request.method == 'GET':
        return JsonResponse(valores)
        
    

@csrf_exempt
def resposta_arduino(request):
    #valor = []
    if request.method == 'GET':
        valor = subprocess.check_output(["./registro/receive"])
        tratado = valor.decode("utf-8")
        print(tratado)
        print(type(tratado))
        #tratado = 'texto_qualquer'
        json_envio = json.loads(tratado)
        #print("valor tratado",tratado)
        return JsonResponse(json_envio)
        

# Create your views here.


def registro_page(request):
    if request.method == 'POST':
        form = Registro(request.POST)
        if form.is_valid():
            render(request, 'registro/registro_page.html', {'form': form})
    else:
        form = Registro()

    return render(request, 'registro/registro_page.html', {'form': form})
