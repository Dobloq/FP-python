'''
Created on 24 sept. 2017

@author: X2835
'''

from tipos import Asignatura
from tipos import Beca
from tipos import Persona
from datetime import date
from time import time

if __name__ == '__main__':
    #===========================================================================
    # asignatura = Asignatura.Asignatura("Fundamentos de Programacion", "3561234", 3.5, Asignatura.TipoAsignatura.PRIMER_CUATRIMESTRE, 2)
    # print(asignatura)
    # print(asignatura.getAcronimo())
    # print(asignatura.getNombre())
    # print(asignatura.getCodigo())
    # print(asignatura.getCreditos())
    # print(asignatura.getTipoAsignatura())
    # print(asignatura.getCurso())
    # beca = Beca.Beca("ABB2025", 1800.0, 6, Beca.TipoBeca.EMPRESA)
    # print(beca)
    # print(beca.getCodigo())
    # print(beca.getCuantiaTotal())
    # print(beca.getDuracion())
    # print(beca.getTipoBeca())
    # print(beca.getCuantiaMensual())
    # print(beca.__hash__())
    # persona = Persona.Persona("12345678Z", "Juan", "Nadie Nadie", date(1980,7,13), "juan.nadie@gmail.com")
    # print(persona)
    # print(persona.getNombre())
    # print(persona.getApellidos())
    # print(persona.getDNI())
    # print(persona.getFechaNacimiento())
    # print(persona.getEmail())
    # print(persona.getEdad())
    #===========================================================================
    tuto = time("12:30")
    finTuto = time("12:40")
    horaInicio = time("7:30")
    horaFin = time("22:00")
    print(finTuto.__lt__(tuto))