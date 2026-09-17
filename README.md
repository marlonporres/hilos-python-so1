# Hilos en Python — Sistemas Operativos I

Aplicación de consola desarrollada en Python para demostrar el uso de hilos y la ejecución concurrente de diferentes tareas.

## Objetivo

Implementar tres hilos independientes y concurrentes utilizando el módulo `threading` de Python.

## Funcionalidades

### Hilo 1 — Escritura en archivo
Solicita un texto al usuario en el hilo principal y lo agrega al archivo `datos.txt` en modo *append* (`a`) codificado en UTF-8, garantizando que el contenido previo no sea eliminado ni sobrescrito.

### Hilo 2 — Ciclos anidados
Ejecuta dos ciclos anidados para simular una tarea prolongada en segundo plano:
- Ciclo externo: de 1 a 25 inclusive.
- Ciclo interno: de 1 a 5000 inclusive.
- Delay real de 2 segundos dentro de cada iteración del ciclo interno.
- Delay real de 1 segundo al finalizar cada ciclo interno.

> **Nota importante sobre el Hilo 2:** Siguiendo literalmente las especificaciones del docente, este hilo tiene una duración extremadamente larga (aproximadamente 69 horas) debido a las 25 × 5000 = 125,000 iteraciones con `sleep(2)` más 25 iteraciones con `sleep(1)`.

### Hilo 3 — Números primos
Solicita al usuario un rango inferior y superior (de forma inclusiva) y determina cuáles números son primos, descartando el 0, el 1 y cualquier número negativo. Los primos encontrados se imprimen claramente en consola.

## Ejecución

Ejecuta el programa desde la terminal:

```bash
python main.py
```

> **Nota:** Según el entorno del sistema operativo, el comando puede ser `python main.py` o `python3 main.py`.

## Arquitectura y Concurrencia

1. Las entradas del usuario (`input`) se solicitan en el hilo principal antes de iniciar los hilos secundarios, evitando colisiones o bloqueos en la consola estándar.
2. Los tres hilos se inician de forma concurrente con `start()` en el orden solicitado (Hilo 1, Hilo 2, Hilo 3).
3. El hilo principal espera la finalización de los tres hilos mediante `join()` (Hilo 1, Hilo 2, Hilo 3).
