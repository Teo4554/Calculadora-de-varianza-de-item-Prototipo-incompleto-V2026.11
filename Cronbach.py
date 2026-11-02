#Esto es una calculadora de alfa de Cronbach para medir la consistencia interna de un conjunto de ítems en una prueba o cuestionario.

K = int(input("Ingrese el numero de items en su cuestionario: "))

N = int(input("Ingrese la muestra o numero de participantes de su cuestionario: "))

orden = ["primer", "segundo", "tercer", "cuarto", "quinto", "sexto", "septimo", "octavo", "noveno", "decimo"] #se pueden añadir mas a voluntad

resultados = []

for i in range(N):
    puntaje = int(input(f"Ingrese su {orden[i]} puntaje: "))
    resultados.append(puntaje)
    
promedio = sum(resultados) / len(resultados)

bases = []

for puntaje in resultados:
    diferencia = puntaje - promedio
    bases.append(diferencia)
print("Resultados:", resultados)
print("Promedio:", promedio)
print("Bases:", bases)

cuadrado = []

for diferencia in bases:
    posresta = diferencia * diferencia
    cuadrado.append (posresta)
print ("Resultados de multiplicacion posterior a resta de promedio para cada valor de puntaje individual: ", cuadrado)

varianza = sum(cuadrado) / (N - 1)
print (f"Su valor de varianza para este item es", {varianza})