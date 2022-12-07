import subprocess

def captura():
	teste = subprocess.run(["./registro/receive"])
	return teste

#captura()