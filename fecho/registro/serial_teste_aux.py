import subprocess

def captura():
	teste = subprocess.check_output(["./static/registro/receive"])
	print(type(teste))
	print(teste)
	return teste

captura()