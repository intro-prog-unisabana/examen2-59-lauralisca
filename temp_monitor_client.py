# temp_monitor_client.py
# Programa cliente que lee temperaturas de un archivo
# e imprime la racha creciente mas larga.

import temp_monitor
def main():
    nombre = input("Ingrese el nombre del archivo: ")
    archivo = open(nombre, "r")
    n = int(archivo.readline())
    monitor = temp_monitor.init(n)
    for i in range(n):
        linea = archivo.readline()
        temp = float(linea)
        monitor = temp_monitor.add_reading(monitor, temp)

    archivo.close()

    resultado = temp_monitor.longest_rising_streak(monitor)
    print("Racha creciente mas larga:", resultado)

if __name__ == "__main__":
    main()
