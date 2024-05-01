from file_reader import FileReader
from university import University
from markov_chain import MarkovChain
import os

while True:
    test = input("Digite o nome do teste: (caso1)")
    
    if os.path.isfile(test):
        file = FileReader(f"cases/{test}.txt")
    
        # Cria universidade e o MarkovChain
        university = University(file)
        markov = MarkovChain(university)
        
        # Calcula a matriz de transição
        markov.Simulation()

        # Fecha o arquivo
        file.Close()
    else:
        print("Arquivo não encontrado. Tente novamente.")
    
    # Para alterar o arquivo de testes, basta trocar o caminho aqui    



