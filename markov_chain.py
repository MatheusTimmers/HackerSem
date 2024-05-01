import numpy as np
from university import University

class MarkovChain:
    def __init__(self, uni: University):
        self.npMatrix = np.zeros((uni.numSemesters + 1, uni.numSemesters + 1), dtype=float)
        self.uni = uni
        self.PopulateMatrix()
        
        self.InitialDistribution = np.zeros((self.uni.numSemesters + 1), dtype=int)
        self.InitialDistribution[0] = self.uni.nStudents
        
    def PopulateMatrix(self):
        for sem in self.uni.lstSemester:
            self.npMatrix[sem.nNextSem-1, sem.nSem-1] = sem.sProb
            
        print(self.npMatrix)

    def Simulation(self):
        num_students = self.InitialDistribution.copy()
        for _ in range(self.uni.numSemesters + 1):
            num_students = np.dot(self.npMatrix, num_students)
            
        self.Print(num_students)

    def Print(self, num_students):
        print("Número de alunos que se diplomarão ao final do curso:", (num_students[-1]))
        print("Número total de alunos que estarão na universidade:", np.sum(num_students))