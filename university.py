from   semester   import Semester
from   file_reader import FileReader
import re

class University:
    def __init__(self, file):
        self.lstSemester  = []
        self.nStudents    = 0 
        self.numSemesters = 0 
        
        self.GetStudents(file)
        self.GetSemester(file)
    
    def GetStudents(self, file: FileReader):
        line  = file.ReadLine(0)
        infos = line.split()
        ## A partir do indice 3 para pegar a quantidade de alunos
        self.nStudents = int(infos[3])
    
    def GetSemester(self, file: FileReader):
        lines   = file.ReadLines()
        pattern = r"Sem_(\d+) -> (\d+\.\d+) -> Sem_(\d+)"
        
        for line in lines:
            match = re.match(pattern, line)
            
            if match:
                if self.numSemesters  < (int(match.group(1))):
                    self.numSemesters = int(match.group(1))
                
                sem = Semester(match.group(1), match.group(2), match.group(3))
                self.lstSemester.append(sem)
            else:
                pattern_diploma = r"Sem_(\d+) -> (\d+\.\d+) -> Diploma"
                match = re.match(pattern_diploma, line)
                if match:
                    sem = Semester(match.group(1),  match.group(2), "Diploma")
                    self.lstSemester.append(sem)