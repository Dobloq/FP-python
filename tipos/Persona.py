'''
Created on 24 sept. 2017

@author: X2835
'''
from datetime import date
import time
from operator import __lt__

class Persona(object):
    '''
    classdocs
    '''
    nombre = None
    apellidos = None
    dni = None
    email = None
    fechaNacimiento = None
    
    def checkDNI(self, dni, msg):
        correcto = len(dni) == 9 and dni[0:8].isdigit() and dni[8].isalpha()
        if correcto:
            letras = "TRWAGMYFPDXBNJZSQVHLCKE"
            numeroDni = int(dni[0:8])
            correcto = dni[8] == letras[(numeroDni % 23)]
        if not correcto:
            raise Exception(msg)

    def checkEmail(self, email, msg):
        if (email == None or email.find("@") == -1):
            raise Exception(msg)
        
    def checkFechaNacimiento(self, fechaNacimiento, msg):
        if(not date.fromtimestamp(time.time()) > fechaNacimiento):
            raise Exception(msg)
    
    def __init__(self, dni, nombre, apellidos, fechaNacimiento, email=""):
        self.checkDNI(dni, "El error en el dni NNNNNNNNA -->" + dni)
        self.checkEmail(email, "El error en el email -->" + email)
        self.checkFechaNacimiento(fechaNacimiento, "La fecha de nacimiento debe ser anterior a la actual -->" + str(fechaNacimiento))
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.email = email
        self.fechaNacimiento = fechaNacimiento
        
    def getEdad(self):
        today = date.fromtimestamp(time.time())
        born = self.getFechaNacimiento()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    
    def getNombre(self):
        return self.nombre


    def getApellidos(self):
        return self.apellidos


    def getEmail(self):
        return self.email


    def getFechaNacimiento(self):
        return self.fechaNacimiento

    def getDNI(self):
        return self.dni

    def setNombre(self, value):
        self.nombre = value


    def setApellidos(self, value):
        self.apellidos = value


    def setEmail(self, value):
        self.checkEmail(value, "El error en el email -->" + value)
        self.email = value


    def setFechaNacimiento(self, value):
        self.checkFechaNacimiento(value, "La fecha de nacimiento debe ser anterior a la actual -->" + value)
        self.fechaNacimiento = value
        
    def setDNI(self, dni):
        self.checkDNI(dni, "El error en el dni NNNNNNNNA -->" + dni)
        self.dni = dni

    def __str__(self):
        return self.getDNI() + " - " + self.getApellidos() + ", " + self.getNombre() + " - " + self.getFechaNacimiento().strftime("%d/%m/%Y")

    def __eq__(self, other):
        return self.getDNI().__eq__(other.getDNI()) and self.getNombre().__eq__(other.getNombre()) and self.getApellidos().__eq__(other.getApellidos)
    
    def __hash__(self):
        return self.getDNI().__hash__() + self.getNombre().__hash__() * 37 + self.getApellidos().__hash__() * 31
    
    def __lt__(self, other):
        respuesta = self.getApellidos().__lt__(other.getApellidos())
        if respuesta == 0:
            respuesta = self.getNombre().__lt__(other.getNombre())
            if respuesta == 0:
                respuesta = self.getDNI().__lt__(other.getDNI())
        return respuesta