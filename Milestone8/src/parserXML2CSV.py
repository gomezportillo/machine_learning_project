# -*- coding:utf-8 -*-

# Andrés Montoro - andres.montoro@alu.uclm.es
# Pedro Manuel Gómez-Portillo - pedromanuel.gomezportillo@alu.uclm.es

from incidencia import Incidencia

class Parser():

    def __init__(self, fin, fout):
        self.file_in = fin
        self.file_out = fout
        self.n_incidencias_gipuzkoa = 0

    def parse(self):
        with open(self.file_in, 'r') as f_in:
            with open(self.file_out, 'w') as f_out:

                lineas = f_in.readlines()
                for i in range(len(lineas)):
                    if "<incidenciaGeolocalizada>" in lineas[i]:
                        if "GIPUZKOA" in lineas[i+3]:

                            incidenc = Incidencia(self.removeTag(lineas[i+1]),
                                                self.removeTag(lineas[i+2]),
                                                self.removeTag(lineas[i+3]),
                                                self.removeTag(lineas[i+4]),
                                                self.removeTag(lineas[i+5]),
                                                self.removeTag(lineas[i+6]),
                                                self.removeTag(lineas[i+7]),
                                                self.removeTag(lineas[i+8]),
                                                self.removeTag(lineas[i+9]),
                                                self.removeTag(lineas[i+10]),
                                                self.removeTag(lineas[i+11]),
                                                self.removeTag(lineas[i+12]),
                                                self.removeTag(lineas[i+13]),
                                                self.removeTag(lineas[i+14]))
                            f_out.write(incidenc.toCSV())
                            self.n_incidencias_gipuzkoa += 1

    def removeTag(self, linea):
        return linea.split('>')[1].split('<')[0].replace('\n', '')

file_in = "data/datos2007_pretty.xml"
file_out = "out/datos2007.csv"
p = Parser(file_in, file_out)
p.parse()
print ("Numero de elementos: ", p.n_incidencias_gipuzkoa)
