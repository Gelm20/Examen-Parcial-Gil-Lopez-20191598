import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la multiplicacion de 2 numeros
2*4 = 8
"""


# start-->
def multiplicar(num1, num2):
    return num1*num2


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros divisibles entre 3 y 5 del 1 al 1000
"""


# start-->
def sumaDivTresYCinco():
    contador = 1
    result = 0
    while contador <= 1000:
        if contador % 3 == 0 or contador % 5 == 0:
            result += contador
    contador +=1
    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el generatriz, area y el volumen de un cono
radio = 5 m
altura = 11 m

generatriz: square_root(altura^2 + radio^2)
area: pi*radio*(radio+generatriz)
volumen: (1/3)*pi*radio^2*altura
"""


# start-->
def obtenerGeneratriz(radio, altura):
    result = (altura**2 + radio**2)**0.5
    return result

def obtenerArea(radio, altura):
    result = math.pi*radio*(radio+obtenerGeneratriz(radio, altura))
    return result

def obtenerVolumen(radio, altura):
    result = (1.0/3.0)*math.pi*radio*radio*altura
    return result

def definicionCono(radio, altura):
    generatriz = 0+obtenerGeneratriz(radio, altura)
    area = 0+obtenerArea(radio, altura)
    volumen = 0+obtenerVolumen(radio, altura)

    result = {"generatriz": generatriz, "area": area, "volumen": volumen}

    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Cono:
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def definicionCono(self):
        generatriz = 0+obtenerGeneratriz(self.radio, self.altura)
        area = 0+obtenerArea(self.radio, self.altura)
        volumen = 0+obtenerVolumen(self.radio, self.altura)

        result = {"generatriz": generatriz, "area": area, "volumen": volumen}

        return result


"""
***************************************************************
@@ ejercicio 5 @@
CentroMedico
Paciente
    nombre
    lugar
    descripcion
    costo
    conDescuento
    descuento
"""


class Paciente:
    def __init__(self, nombre, lugar, descripcion, costo, conDescuento, descuento):
        self.nombre = nombre
        self.lugar = lugar
        self.descripcion = descripcion
        self.costo = costo
        self.conDescuento = conDescuento
        self.descuento = descuento
    
    def dicPaciente(self):
        return {'nombre': self.nombre, 'lugar': self.lugar, 'descripcion': self.descripcion, 'costo': self.costo, 'conDescuento':self.conDescuento, 'descuento':self.descuento}



class CentroMedico:
    def __init__(self):
        self.lista = []

    def registrar(self, paciente):
        self.lista.append(paciente.dicPaciente())


    def totalCostoSanSalvador(self):
        sumaSanSalvador = 0
        for elemento in self.lista:
            if elemento["lugar"] == "san salvador":
                sumaSanSalvador += elemento["costo"]

        return "$"+"{:.2f}".format(sumaSanSalvador)

    def totalCostoConDescuento(self):
        costoConDescuento = 0
        for elemento in self.lista:
            costoConDescuento += elemento["costo"]
            costoConDescuento -= elemento["descuento"]
            retorno = "$"+"{:.2f}".format(costoConDescuento)
        return retorno



"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return "https://github.com/Gelm20/Examen-Parcial-Gil-Lopez-20191598.git"
