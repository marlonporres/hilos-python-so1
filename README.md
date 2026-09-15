# Hilos en Python — Sistemas Operativos I

Aplicación de consola desarrollada en Python para demostrar el uso de hilos y la ejecución concurrente de diferentes tareas.

## Objetivo

Implementar tres hilos independientes utilizando el módulo `threading` de Python.

## Funcionalidades

### Hilo 1 — Escritura en archivo
Solicita un texto al usuario y lo agrega a un archivo existente sin eliminar su contenido anterior.

### Hilo 2 — Ciclos anidados
Ejecuta dos ciclos anidados:
- Ciclo externo de 1 a 25.
- Ciclo interno de 1 a 5000.
- Delay de 2 segundos en el ciclo interno.
- Delay de 1 segundo en el ciclo externo.

### Hilo 3 — Números primos
Solicita al usuario un rango inferior y superior, recorre los números comprendidos en dicho rango y determina cuáles son números primos.

## Tecnologías

- Python 3
- `threading`
- Manejo de archivos
- Programación concurrente

## Ejecución

```bash
python main.py
