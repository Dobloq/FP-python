'''
Created on 24 sept. 2017

@author: X2835
'''

class Alumno(object):
    asignaturas = []
    expediente = None
    '''
    classdocs
    '''
    def __init__(self):
        pass    

    def getAsignaturas(self):
        pass
    
    def getExpediente(self):
        pass
    
    def getCurso(self):
        pass
    
    def estaMatriculado(self, asignatura):
        pass
    
    def getCalificacionPorAsignatura(self):
        pass
    
    def getAsignaturasOrdenadasPorCurso(self):
        pass
    
    def eliminaAsignatura(self, asignatura):
        pass
    
    def matriculaAsignatura(self, asignatura):
        pass
    
    def evaluaAlumnoMH(self, asignatura, curso, convocatiora, nota, mencionHonor):
        pass
    
    def evaluaAlumno(self, asignatura, curso, convocatoria, nota):
        pass
    
