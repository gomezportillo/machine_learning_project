class Incidencia():
    def __init__(self, tipo, autonomia, provincia, matricula, causa, poblacion, fecha, nivel, pk_ini, pk_fin, sentido, nombre, longitud, latitud):
        self.tipo = tipo
        self.autonomia = autonomia
        self.provincia = provincia
        self.matricula = matricula
        self.causa = causa
        self.poblacion = poblacion
        self.fecha = fecha
        self.nivel = nivel
        self.pk_ini = pk_ini
        self.pk_fin = pk_fin
        self.sentido = sentido
        self.nombre = nombre
        self.longitud = longitud
        self.latitud = latitud

    def toCSV(self):
        return self.tipo+";"+self.autonomia+";"+self.provincia+";"+self.matricula+";"+self.causa+";"+self.poblacion+";"+self.fecha+";"+self.nivel+";"+self.pk_ini+";"+self.pk_fin+";"+self.sentido+";"+self.nombre+";"+self.longitud+";"+self.latitud+"\n"

    def toString(self):
        return self.tipo + " " + self.provincia

    def printAll(self):
        print self.tipo
        print self.autonomia
        print self.provincia
        print self.matricula
        print self.causa
        print self.poblacion
        print self.fecha
        print self.nivel
        print self.pk_ini
        print self.pk_fin
        print self.sentido
        print self.nombre
        print self.longitud
        print self.latitud
