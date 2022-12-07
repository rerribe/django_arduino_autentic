from django import forms

class Registro(forms.Form):
	nome = forms.CharField(label='nome',max_length=200)
	cargo = forms.CharField(label='cargo',max_length=200)
	cartao = forms.CharField(label='cartao',max_length=200)