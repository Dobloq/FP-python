'''
Created on 24 sept. 2017

@author: X2835
'''

class Beca(object):
    '''
    classdocs
    '''
    codigo = None
    cuantiaTotal = None
    duracion = None
    tipoBeca = None
    cuantia_minima = 1500.0
    
    def checkCodigo(self, codigo, msg):
        esCorrecto = len(codigo) == 7 and codigo[0:3].isalpha() and codigo[4:].isdigit()
        if not esCorrecto:
            raise Exception(msg + "  " + codigo[0:3] + "   " + codigo[4:])
    
    def checkCuantia(self, cuantia, msg):
        if cuantia < self.cuantia_minima:
            raise Exception(msg)

    def checkDuracion(self, duracion, msg):
        if duracion < 1:
            raise Exception(msg)
        
    def checkTipoBeca(self, tipoBeca, msg):
        if tipoBeca not in TipoBeca:
            raise Exception(msg)

    def __init__(self, codigo, cuantiaTotal, duracion, tipoBeca):
        self.checkCodigo(codigo, "El codigo responde al patron AAANNNN -->" + codigo)
        self.checkCuantia(cuantiaTotal, "La cuantia debe ser >=" + str(self.cuantia_minima) + "  -->" + str(cuantiaTotal))
        self.checkDuracion(duracion, "La duracion debe ser >=1 -->" + str(duracion))
        self.checkTipoBeca(tipoBeca, "El tipo de la beca no es valido -->" + str(tipoBeca))
        self.codigo = codigo
        self.cuantiaTotal = cuantiaTotal
        self.duracion = duracion
        self.tipoBeca = tipoBeca
    
    def getCodigo(self):
        return self.codigo
    
    def getCuantiaMensual(self):
        return self.getCuantiaTotal() / self.getDuracion()
    
    def getCuantiaTotal(self):
        return self.cuantiaTotal
    
    def getDuracion(self):
        return self.duracion
    
    def getTipoBeca(self):
        return self.tipoBeca.name
    
    def setCuantiaTotal(self, cuantia):
        self.checkCuantia(cuantia, "La cuantia debe ser >=" + self.cuantia_minima + "  -->" + cuantia)
        self.cuantiaTotal = cuantia
        
    def setDuracion(self, d):
        self.checkDuracion(d, "La duracion debe ser >=1 -->" + d)
        self.duracion = d

    def __str__(self):
        return "[" + self.getCodigo() + ", " + self.getTipoBeca() + "]"
        
    def __lt__(self, other):
        if self.getCodigo() == other.getCodigo():
            return self.getTipoBeca() < other.getTipoBeca()
        return self.getCodigo() < other.getCodigo()
        
    def __hash__(self):
        return self.getCodigo().__hash__() + self.getTipoBeca().__hash__() * 53
    
    def __eq__(self, other):
        return self.getCodigo().__eq__(other.getCodigo()) and self.getTipoBeca().__eq__(other.getTipoBeca())
    
from enum import Enum

class TipoBeca(Enum):
    ORDINARIA = 1
    MOVILIDAD = 2
    EMPRESA = 3
