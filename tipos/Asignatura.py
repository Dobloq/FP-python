'''
Created on 24 sept. 2017

@author: X2835
'''
import enum

class Asignatura(object):
    nombre = None
    codigo = None
    creditos = None
    curso = None
    tipoAsignatura = None
    departamento = None
    
    def checkCreditos(self, creditos, msg):
        if(not(creditos > 0.0)):
            raise Exception(msg)
        
    def checkCodigo(self, codigo, msg):
        esCorrecto = len(codigo) == 7 and codigo.isdigit()
        if not esCorrecto:
            raise Exception(msg)
        
    def checkCurso(self, curso, msg):
        if (curso < 1 or curso > 4):
            raise Exception(msg)
    
    def checkTipoAsignatura(self, tipoAsignatura, msg):
        if(tipoAsignatura not in TipoAsignatura):
            raise Exception(msg)
    
    def __init__(self, nombre, codigo, creditos, tipoAsignatura, curso, departamento=""):
        self.checkCreditos(creditos, "Los creditos deben ser > 0 --->" + str(creditos))
        self.checkCodigo(codigo, "El codigo responde al formato NNNNNNN --->" + codigo)
        self.checkCurso(curso, "El curso debe estar entre 1 y 4 --->" + str(curso))
        self.checkTipoAsignatura(tipoAsignatura, "El tipo de asignatura no es correcto ---> " + str(tipoAsignatura))
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.curso = curso
        self.tipoAsignatura = tipoAsignatura
        self.departamento = departamento
    
    def getAcronimo(self):
        acronimo = ""
        for i in range(0, len(self.nombre)):
            c = self.nombre[i]
            if c.isupper():
                acronimo += c
        return acronimo
    
    def getCodigo(self):
        return self.codigo
    
    def getCreditos(self):
        return self.creditos
    
    def getCurso(self):
        return self.curso
    
    def getDepartamento(self):
        return self.departamento
    
    def getNombre(self):
        return self.nombre
    
    def getTipoAsignatura(self):
        return self.tipoAsignatura.name
    
    def setDepartamento(self, departamento):
        if departamento != self.departamento:
            antiguo = self.departamento
            self.departamento = departamento
            if antiguo != "":
                antiguo.eliminaAsignatura(self)
            if departamento != "":
                departamento.nuevaAsignatura(self)
                
    def __str__(self):
        return "(" + self.getCodigo() + ") " + self.getNombre()
    
    def __eq__(self, other):
        return self.getCodigo().__eq__(other.getCodigo())
    
    def __hash__(self):
        return self.getCodigo().__hash__()
    
    def __lt__(self, other):
        return self.getCodigo().__lt__(other.getCodigo())
    
class TipoAsignatura(enum.Enum):
    ANUAL = 1
    PRIMER_CUATRIMESTRE = 2
    SEGUNDO_CUATRIMESTRE = 3
