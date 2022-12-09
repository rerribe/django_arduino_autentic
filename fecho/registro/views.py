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

from .forms import Registro

@csrf_exempt


def inicial(request):
	return render(request,'registro/inicial.html')


def registro_page(request):

	if request.method == 'POST':
		form = Registro(request.POST)
		if form.is_valid():
			render(request, 'registro/registro_page.html', {'form': form})
	else:
		form = Registro()

	return render(request, 'registro/registro_page.html', {'form': form})

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
        #print(valor.decode("utf-8"))
        tratado = valor.decode("utf-8")
        json_envio = json.loads(tratado)
        #print("valor tratado",tratado)
        return JsonResponse(json_envio)
        

# Create your views here.
