# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
print("buenas tardes ingrese los numeros:")
numero_1 = int(input("coloque el primer numero:"))
numero_2 = int(input("coloque el segundo numero:"))
print("ingrese el numero para indicar que operacion matematica desea realizar:")
print("suma: 1")
print("resta: 2")
print("multiplicacion: 3")
print("divsion: 4 ")
print("potencia: 5")

z = int(input("coloque el numero aqui:"))
if z == 1:
    print(f"la suma de {numero_1} con {numero_2} es igual a {numero_1+numero_2}")
elif z == 2:
    print(f"la resta de {numero_1} con {numero_2} es igual a {numero_1-numero_2}")
elif z == 3:
    print(f"la multiplicacion de {numero_1} con {numero_2} es igual a {numero_1*numero_2}")
elif z == 4:
    print(f"la division de {numero_1} con {numero_2} es igual a {numero_1/numero_2}")
elif z == 5:
    print(f"la potencia de {numero_1} elevado a {numero_2} es igual a {numero_1**numero_2}")

'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia
- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio