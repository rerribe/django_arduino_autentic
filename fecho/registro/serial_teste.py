import subprocess

def captura():
    teste = subprocess.check_output(["./registro/receive"])
    return teste

#captura()