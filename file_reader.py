class FileReader:
    def __init__(self, path):
        self.path = path
        self.file = open(self.path, 'r')

    # Retorno todas as linhas do arquivo
    def ReadLines(self): 
        return self.file.readlines() 
    
    # Retorno uma linha especifica do arquivo
    def ReadLine(self, nline): 
        self.file.seek(nline)
        return self.file.readline()
    
    # Fecha o arquivo
    def Close(self):
        self.file.close()