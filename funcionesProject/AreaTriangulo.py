#Ejemplo para calcular el area del triangulo

#Variables de entrada
base = int(input("Ingrese la base:" ))
altura = int(input("Ingrese la altura:" ))

#Proceso
def calcularAreaTriangulo(base, altura):
    area = (base * altura) / 2
    return area

#Invocar la funcion
resultado = calcularAreaTriangulo(base, altura)

#Salida
print(f"El area del triangulo cuya base {base} y altura {altura} es:", {resultado})

#Funcion con argumentos predeterminados
def my_fuction (country = "Colombia"):
    print("i am from"+country)

#Invocar funcion
my_fuction()
my_fuction("Sweden")
my_fuction("Argentina")
my_fuction("España")

#funcion con argumentos arbitrarios
def mostrarEstudiantes(*args):
    print("El estudiante:"+args[2])
#Invicamos la funcion
mostrarEstudiantes(
        "Erick","email","Pri pra",)

#
def mostrarCarros(carro1, carro2, carro3):
    print("el carro es"+carro1)
#Invovamos la funcion

mostrarCarros(carro1=" Mazda ", carro2=" Renault ", carro3=" BMW ")

#funcion con argumentos arbitario **kwargs
def mostrarCliente(**kwargs):
    print("Su apellidos es :"+ kwargs["apellido"])

#Invocar la funcion
mostrarCliente(
        nombre="Erick", apellido="Garcia")

#funcion con declaracion de paso
def miFuncion():
    pass

#funciones integradas
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#funcion pow(x,y)
num1 = pow(2,3)

print(num1)

#Modulo de matematicas
#funcionmath.sqrt
import math
num2 = math.sqrt(34)
print(num2)

#funcion math.ceil()
import math
num3 = math.ceil(3.7)
num4 = math.ceil(3.7)

print(num3)
print(num4)
