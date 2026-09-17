import threading
import time


def hilo_archivo(texto):
    """
    Hilo 1: Escribe el texto proporcionado en el archivo 'datos.txt'.
    Se utiliza el modo 'a' (append) para concatenar información al final
    del archivo sin borrar ni sobrescribir el contenido previo.
    """
    with open("datos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(texto + "\n")
    print("[HILO 1] Texto guardado exitosamente en datos.txt.")


def hilo_ciclos():
    """
    Hilo 2: Ejecuta dos ciclos anidados con retardos específicos.
    - Ciclo externo: de 1 a 25 inclusive.
    - Ciclo interno: de 1 a 5000 inclusive.
    """
    for i in range(1, 26):
        for j in range(1, 5001):
            print(f"[HILO 2] Ciclo externo: {i} | Ciclo interno: {j}")
            # Delay de 2 segundos dentro de cada iteración del ciclo interno
            time.sleep(2)

        # Delay de 1 segundo al finalizar cada ciclo interno (perteneciente al ciclo externo)
        time.sleep(1)


def hilo_primos(inferior, superior):
    """
    Hilo 3: Recorre un rango inclusivo y encuentra los números primos.
    Los valores menores a 2 (incluyendo 0, 1 y negativos) no son primos.
    """
    for numero in range(inferior, superior + 1):
        es_primo = True

        # 0, 1 y negativos no son primos por definición
        if numero < 2:
            es_primo = False
        else:
            # Comprobación de divisores: si encontramos un divisor exacto, no es primo
            for divisor in range(2, numero):
                if numero % divisor == 0:
                    es_primo = False
                    break

        if es_primo:
            print(f"[HILO 3] {numero} es primo.")


def main():
    # Los datos se solicitan previamente desde el hilo principal para evitar
    # colisiones o competencia de múltiples hilos por la entrada estándar (input)
    texto = input("Ingrese la cadena de texto que quiere guardar en el archivo: ")
    inferior = int(input("Ingrese el rango inferior: "))
    superior = int(input("Ingrese el rango superior: "))

    # Creación de los tres hilos con sus respectivas funciones y argumentos
    hilo1 = threading.Thread(
        target=hilo_archivo,
        args=(texto,)
    )
    hilo2 = threading.Thread(
        target=hilo_ciclos
    )
    hilo3 = threading.Thread(
        target=hilo_primos,
        args=(inferior, superior)
    )

    # start() inicia la ejecución concurrente de cada hilo en paralelo
    hilo1.start()
    hilo2.start()
    hilo3.start()

    # join() bloquea el hilo principal esperando a que cada hilo termine su ejecución
    hilo1.join()
    hilo2.join()
    hilo3.join()


if __name__ == "__main__":
    main()
