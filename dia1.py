# VARIABLES - ESPACIOS DE MEMORIA

# String - Cadena de caracteres
nombre = "Nacho"

# Integer - Numeros redondos
edad = 21

# Float - Numeros con coma
precio = 10.99

# Boolean - Condicional
es_mayor_de_edad = True


# CONVERTIR VARIABLES DE UN TIPO A OTRO

# Ver el tipo de dato de una variable
type(nombre) # String
type(edad) # Integer
type(precio) # float
type(es_mayor_de_edad) #Boolean

# Transformar en tipo de dato string 
str()

# Transformar en tipo de dato integer
int()

# Transformar en tipo de dato float
float()

# Transformar en tipo de dato boolean
bool()
# Importante:
# String vacio = False, String con caracteres = True
# Int 0 = False, Int que no sea 0 = True


# INPUT - EL USUARIO INGRESA DATA

# Guardar lo que ingresa el usuario en una variable
nombre2 = input("Ingresa tu nombre: ")

# Guardar lo que ingresa el usuario como tipo de dato int
edad2 = int(input("Ingresa tu edad: "))
# Se puede hacer con cualquier tipo de dato