class FileReader:
    def __init__(self, path):
        self.path = path
        self.file = open(self.path, 'r')

    def ReadLines(self): 
        return self.file.readlines() 
    
    def ReadLine(self, nline): 
        self.file.seek(nline)
        return self.file.readline()
    
    def Close(self):
        self.file.close()