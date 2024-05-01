import numpy as np
import math
from university import University

class HackerProgram:
    def __init__(self, uni: University):
        # Cria a matriz de probabilidades, uma matriz do tipo float [numSemestre + 1][numSemestre + 1], 
        # Mais um porque tem o semestre de diploma
        self.npMatrix = np.zeros((uni.numSemesters + 1, uni.numSemesters + 1), dtype=float)
        # Objeto da universidade
        self.uni = uni
        # Pupula a matriz com as informações
        self.PopulateMatrix()
        
        # Cria uma matriz com as informações dos alunos que entram no semestre 1
        self.InitialDistribution = np.zeros((self.uni.numSemesters + 1), dtype=int)
        self.InitialDistribution[0] = self.uni.nStudents
        
    def PopulateMatrix(self):
        # Em cada semestre da lista, vai na sua respectiva posição da matriz e adiciona a sua probabilidade 
        for sem in self.uni.lstSemester:
            self.npMatrix[sem.nNextSem-1, sem.nSem-1] = sem.sProb

    def BreakSecurity(self):
        # Faz a multiplicação da matriz de propabilidades pelo alunos em cada semestre
        num_students = self.InitialDistribution.copy()
        for _ in range(self.uni.numSemesters): 
            num_students = np.dot(self.npMatrix, num_students)
            # Novos alunos entrando no semestre 1
            num_students[0] = num_students[0] + self.uni.nStudents
        
        self.Print(num_students)

    def Print(self, num_students):
        print("Número de alunos que se vão pegar o diploma ao final do curso:", math.floor(num_students[-1]))
        print("Número total de alunos que estarão na universidade:", math.floor(np.sum(num_students) - num_students[-1]))