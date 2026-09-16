import threading
import time


def hilo_archivo(texto):
    with open("datos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(texto + "\n")
def hilo_ciclos():
    for i in range(1, 26):
        for j in range(1, 5001):
            print(f"Ciclo externo: {i} | Ciclo interno: {j}")
            time.sleep(2)

    time.sleep(1)

def hilo_primos(a, b):
    pass

def main():
    texto = input("Ingrese la cadena de texto que quiere guardar en el archivo: ")
    inferior = int(input("Ingrese el rango inferior: "))
    superior = int(input("Ingrese el rango superior: "))
