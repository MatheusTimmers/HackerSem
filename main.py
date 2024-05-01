from file_reader import FileReader
from university import University
from HackerProgram import HackerProgram
import os

while True:
    test = input("Digite o nome do teste: (caso1)")
    
    if os.path.isfile(f"cases/{test}.txt"):
        # Le o arquivo
        file = FileReader(f"cases/{test}.txt")
    
        # Cria universidade e o MarkovChain
        university = University(file)
        HackerProg = HackerProgram(university)
        
        # Quebra a segurança da universisade e descobre os alunos em cada semestre
        HackerProg.BreakSecurity()

        # Fecha o arquivo
        file.Close()
    else:
        print("Arquivo não encontrado. Tente novamente.")  