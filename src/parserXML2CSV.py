""" GIPUZKOA
"""
from incidencia import Incidencia

class Parser():

    def __init__(self, fin, fout):
        self.file_in = fin
        self.file_out = fout

    def parse(self):
        self.array = []
        self.n_elements = 0
        with open(self.file_in, 'r') as fin:
            with open(self.file_out, 'w') as fout:

                linea = fin.readlines()
                for i in range(len(linea)):
                    if "<incidenciaGeolocalizada" in linea[i]:
                            inci = Incidencia(self.removeTag(linea[i+1]),
                                        self.removeTag(linea[i+2]),
                                        self.removeTag(linea[i+3]),
                                        self.removeTag(linea[i+4]),
                                        self.removeTag(linea[i+5]),
                                        self.removeTag(linea[i+6]),
                                        self.removeTag(linea[i+7]),
                                        self.removeTag(linea[i+8]),
                                        self.removeTag(linea[i+9]),
                                        self.removeTag(linea[i+10]),
                                        self.removeTag(linea[i+11]),
                                        self.removeTag(linea[i+12]),
                                        self.removeTag(linea[i+13]),
                                        self.removeTag(linea[i+14]))

                            if inci.provincia == "GIPUZKOA":
                                self.n_elements += 1
                                fout.write(inci.toCSV())

    def removeTag(self, linea):
        return linea.split('>')[1].split('<')[0].replace('\n', '')

p = Parser("data/inc2006.xml", "out/inc2006.csv")
p.parse()
print ("Numero de elementos: ", p.n_elements)
