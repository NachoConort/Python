# MATEMATICAS - OPERADORES - ARITMETICA
import math # Contiene varias funciones matematicas utiles
# Incrementar
cantidadAmigos = 0
# Incrementa en uno la variable
cantidadAmigos += 1
# Se puede hacer con suma, resta, division, multiplicacion

# Se puede hacer con potencias y raices
cantidadAmigos **= 2 # Elevamos al cuadrado
cantidadAmigos //= 2 # Raiz de 2

# Obtener el resto de una disivion
resto = cantidadAmigos % 3 # Resto de dividir la variable en 3

# Redondear numeros
pi = 3.14
redondear = round(pi) # Devuelve 3

# Obtener valor absoluto
numeroNegativo = -4
valorAbsoluto = abs(numeroNegativo) # Devuelve 4

# Potencias
potencia = pow(4, 3) # Devuelve 4 elevado 3

# Retornar el maximo valor entre numeros
maximo = max(pi, numeroNegativo, potencia) # Devuelve el mayor

# Retornar el minimo valor entre numeros
minimo = min(pi, numeroNegativo, potencia) # Devuelve el menor

math.pi # El valor de pi
math.e # El valor de e

# Obtener raiz cuadrada
math.sqrt(9) # Devuelve 3

# Redondear hacia arriba
math.ceil(9.1) # Devuelve 10
# Redondear hacia abajo
math.floor(9.9) # Devuelve 9