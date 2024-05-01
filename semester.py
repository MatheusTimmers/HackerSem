class Semester:
    def __init__(self, nSemester, sProbability, nNext):
        ## Mais um pois o index começa em 0
        self.nSem  = int(nSemester)
        self.sProb = float(sProbability)
        
        if nNext == "Diploma":
            self.nNextSem = self.nSem + 1;
        else:
            self.nNextSem = int(nNext)
