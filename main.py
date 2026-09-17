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

    for numero in range(a, b + 1):
        es_primo = True

        if numero < 2:
            es_primo = False
        else:
            for divisor in range(2, numero):
                if numero % divisor == 0:
                    es_primo = False
                    break
        if es_primo == True:
            print(f"{numero} es primo.")


def main():
    hilo1 = threading.Thread(
        target=hilo_archivo,
        args = (texto,)
    )
    hilo2 = threading.Thread(
            target=hilo_ciclos,
        )
    hilo3 = threading.Thread(
            target = hilo_primos,
            args = (inferior, superior)
        )

    texto = input("Ingrese la cadena de texto que quiere guardar en el archivo: ")
    inferior = int(input("Ingrese el rango inferior: "))
    superior = int(input("Ingrese el rango superior: "))

    hilo1.start()
    hilo2.start()
    hilo3.start()

    hilo1.join()
    hilo2.join()
    hilo3.join()
