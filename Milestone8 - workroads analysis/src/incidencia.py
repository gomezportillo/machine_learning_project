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
        csv = ""
        for attr, value in self.__dict__.iteritems():
            csv += value+";"
        return csv[:-1]+"\n"
