# temp_monitor.py
# Libreria de funciones para registrar lecturas de temperatura.
#
# Estructura del diccionario (monitor):
#   - 'max':      numero maximo de lecturas permitidas (int)
#   - 'readings': lista con las temperaturas de cada lectura (list)
#   - 'total':    suma total de todas las temperaturas (float)


def init(max_readings):
    return{
     'max': max_readings,
     'readings':[],
     'total':0.0
     }

def add_reading(monitor, temp):
    if len(monitor['readings']) < monitor['max']:
        monitor['readings'].append(temp)
        monitor['total'] += temp
    return monitor

def count(monitor):
 return len(monitor['readings'])

def average_temp(monitor):
   if count(monitor) == 0:
        return 0
   return monitor['total'] / count(monitor)

def format_readings(monitor):
    readings = monitor['readings']
    return "[" + ", ".join(str(t) for t in readings) + "]"

def highest_temp(monitor):
    if count(monitor) == 0:
      return None
    return max(monitor['readings'])



def coldest_window(monitor, k):
    readings = monitor['readings']

    if len(readings) < k:
        return None
    minimo = 999999
    for i in range(len(readings) - k + 1):
        suma = 0

        for j in range(i, i + k):
            suma = suma + readings[j]

        promedio = suma / k

        if promedio < minimo:
            minimo = promedio

    return minimo


def longest_rising_streak(monitor):
    readings = monitor['readings']
    if len(readings) == 0:
        return 0
    maxima = 1
    actual = 1
    for i in range(1, len(readings)):
        if readings[i] > readings[i-1]:
            actual = actual + 1
            if actual > maxima:
                maxima = actual
        else:
            actual = 1
        return maxima

def main():
    # crear un monitor para temperaturas de Bogota (12 horas, 6am-5pm)
    monitor = init(12)
    monitor = add_reading(monitor, 8.0)   # 6am
    monitor = add_reading(monitor, 9.5)   # 7am
    monitor = add_reading(monitor, 11.0)  # 8am
    monitor = add_reading(monitor, 13.5)  # 9am
    monitor = add_reading(monitor, 15.0)  # 10am
    monitor = add_reading(monitor, 17.5)  # 11am
    monitor = add_reading(monitor, 19.0)  # 12pm
    monitor = add_reading(monitor, 20.0)  # 1pm
    monitor = add_reading(monitor, 19.5)  # 2pm
    monitor = add_reading(monitor, 18.0)  # 3pm
    monitor = add_reading(monitor, 16.5)  # 4pm
    monitor = add_reading(monitor, 15.0)  # 5pm

    # imprimir estadisticas
    print("numero de lecturas =", count(monitor))               # 12
    print("temp promedio =", average_temp(monitor))             # 15.208...
    print("temp mas alta =", highest_temp(monitor))             # 20.0
    print("ventana mas fria (3) =", coldest_window(monitor, 3)) # 9.5
    print("racha creciente =", longest_rising_streak(monitor))  # 8

    # imprimir temperaturas
    print(format_readings(monitor))


if __name__ == "__main__":
    main()
