from   semester   import Semester
from   file_reader import FileReader
import re

class University:
    def __init__(self, file):
        # Informações da Universidade
        self.lstSemester  = []
        self.nStudents    = 0 
        self.numSemesters = 0 
        
        # Hackeia e descobre o numero de alunos e o numero de semestres 
        self.GetStudents(file)
        self.GetSemester(file)
    
    def GetStudents(self, file: FileReader):
        # Le a primeira linha do arquivo
        line  = file.ReadLine(0)
        
        # Faz o split
        infos = line.split()
        
        ## Iindice 3 para pegar a quantidade de alunos
        self.nStudents = int(infos[3])
    
    def GetSemester(self, file: FileReader):
        # Pega as informações dos semestres e salva o semestre na lista de semestres
        # paga todas as linhas do arquivo
        lines   = file.ReadLines()
        # Regex para pegar as informações importantes
        pattern = r"Sem_(\d+) -> (\d+\.\d+) -> Sem_(\d+)"
        
        for line in lines:
            # Faz pesquisa em cada linha pelo regex
            match = re.match(pattern, line)
            
            if match:
                # Para descobrir o numeoro semestres, guarda o maior em uma variavel
                if self.numSemesters  < (int(match.group(1))):
                    self.numSemesters = int(match.group(1))
                
                # Cria um objeto semestre com as informações
                #                 Semestre   ->  Probabilidade -> Proximo semestre
                sem = Semester(match.group(1), match.group(2), match.group(3))
                # Coloca na lista
                self.lstSemester.append(sem)
            else:
                # Caso seja a linha do diploama, faz as devidades tratativas
                pattern_diploma = r"Sem_(\d+) -> (\d+\.\d+) -> Diploma"
                match = re.match(pattern_diploma, line)
                if match:
                    sem = Semester(match.group(1),  match.group(2), "Diploma")
                    self.lstSemester.append(sem)