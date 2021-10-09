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

# Ejercicios de práctica numérica y cadenas
print("buenas tardes, ingresen sus nombres completos")
a = str(input("ingrese el nombre completo del padre:"))
b = str(input("ingrese el nombre completo de la madre:"))
c = str(input("cual es el nombre del hijo:"))
papa = a .split()
camote = b.split()
zanahoria = c.split() 
print(f"el nombre completo del hijo es {zanahoria[0]} {papa[1]} {camote[2]}")
print(d)
'''
Enunciado:
Realice un programa que determine cual sería el apellido de una persona
al ingresara los dos nombres completos de sus padres.
En definitiva se solicita crear una variable nueva que reuna
los apellidos.
- Primero el programa debe consultar el nombre completo del padre_1
- Luego el programa debe consultar el nombre completo del padre_2
- Luego debe consultar el nombre del hijo/a
- Debe extraer los apellidos de los padres (ver la nota al final)
- Luego formar el nombre completo del hijo/a utilizando los apellidos
  de sus padres y el nombre ingresado de dicha persona
- Imprimir en pantalla el resultado
NOTA: Para extraer el apellido del nombre completo recomendamos usar
el método "split"
Mostraremos un ejemplo:
direccion_completa = 'Monroe 2716'
calle, altura = direccion_completa.split(' ')
Les dejo por su cuenta a que busquen un poco más acerca de este método
que seguramente utilizarán mucho de acá en adelante.
Les dejamos un link con algunos ejemplos más:
https://www.pythonforbeginners.com/dictionary/python-split
Cualquier duda con el método split pueden consultarla por el campus
'''

print('Jugando con texto')
# Empezar aquí la resolución del ejercicio