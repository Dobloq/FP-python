'''
Created on 24 sept. 2017

@author: X2835
'''
from time import localtime

class Tutoria(object):
    '''
    classdocs
    '''
    diaSemana = None
    horaComienzo, horaFin = None
    
    def checkDiaSemana(self, diaSemana, msg):
        if (diaSemana.value == 6 or diaSemana.value == 7):
            raise Exception(msg)
        
    def checkHoraComienzo(self, horaComienzo, msg):
        hora = localtime("08:30")
        if(horaComienzo.__lt__(hora)):
            raise Exception(msg)

    def checkHoraFin(self, horaFin, msg):
        hora = localtime("21:30")
        if(horaFin.__gt__(hora)):
            raise Exception(msg)
        
    def checkDuracion(self, horaComienzo, horaFin, msg):
        pass
        
    def __init__(self, diaSemana, horaComienzo, horaFin):
        '''
        Constructor
        '''
        self.checkDiaSemana(diaSemana, "Las tutorias solo pueden ser de lunes a viernes --->" + diaSemana)
        self.checkHoraComienzo(horaComienzo, "Las tutorias solo pueden ser a partir de las 08:30 --->" + horaComienzo)
        self.checkHoraFin(horaFin, "Las tutorias solo pueden ser antes de las 21:30 --->" + horaFin)
        self.diaSemana = diaSemana
        self.horaComienzo = horaComienzo
        self.horaFin = horaFin
        
from enum import Enum        
        
class DiaDeLaSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7