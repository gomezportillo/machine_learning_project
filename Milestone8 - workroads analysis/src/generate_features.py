#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Andrés Montoro Montarroso
@author: Pedro Manuel Gómez-Portillo
"""

"""
Tasks to achieve:
    * Number of accidents per reason
    * Number of accidents per traffic level
    * Number of accidents in winter (enero2006 - 21 marzo2006 && 22 diembre2006 - 31dic2006)
    * Number of accidents in summer (20 junio - 23 septiembre)
    * Number of accidents from 8.00am to 15.00pm
    * Number of accidents from 15.00pm to 20.00pm
    * Number of accidents from 20.00pm to 3.00am
"""

poblacion   = 0
nivel       = 1
latitud     = 2
provincia   = 3
tipo        = 4
autonomia   = 5
fecha       = 6
km_ini      = 7
sentido     = 8
causa       = 9
matricula   = 10
carretera   = 11
km_final    = 12
longitud    = 13
zona        = 14

dic_reason          = dict()
dic_traffic_level   = dict()
dic_winter_acc      = dict()
dic_summer_acc      = dict()
dic_8_15_accidents  = dict()
dic_15_20_accidents = dict()
dic_20_3_accidents  = dict()


def calculate_reason(current_zona, current_causa):
    if current_causa != '':
        try:
            dic_reason[current_causa, current_zona] += 1
        except KeyError:
            dic_reason[current_causa, current_zona] = 1

def calculate_traffic_level(current_zona, current_traffic_level):
    if current_traffic_level != '':
        try:
            dic_traffic_level[current_traffic_level, current_zona] += 1
        except KeyError:
            dic_traffic_level[current_traffic_level, current_zona] = 1

def calculate_accidents_by_date(current_zona, current_date):
    if current_date != '':
        fecha = current_date.split()[0]
        dia = int(fecha.split('-')[2])
        mes = int(fecha.split('-')[1])

        if mes in (1, 2, 12) or (mes == 3 and dia < 21):
            try:
                dic_winter_acc[current_zona] += 1
            except KeyError:
                dic_winter_acc[current_zona] = 1
        elif mes in (7, 8) or (mes == 6 and dia > 20) or (mes == 9 and dia < 23):
            try:
                dic_summer_acc[current_zona] += 1
            except KeyError:
                dic_summer_acc[current_zona] = 1

def calculate_accidents_by_hour(current_zona, current_date):
    if current_date != '':
        fecha = current_date.split()[1]
        hora = int(fecha.split(':')[0])

        if  hora >= 8 and hora <=14:
            try:
                dic_8_15_accidents[current_zona] += 1
            except KeyError:
                dic_8_15_accidents[current_zona] = 1

        if  hora >= 15 and hora <=19:
            try:
                dic_15_20_accidents[current_zona] += 1
            except KeyError:
                dic_15_20_accidents[current_zona] = 1

        if  hora >= 20 or hora <=3:
            try:
                dic_20_3_accidents[current_zona] += 1
            except KeyError:
                dic_20_3_accidents[current_zona] = 1

lines = list()
with open('data/datos2007filt_with_zones.csv') as f_in:
    for line in f_in:
        lines.append(line.split(";"))

for i in range(len(lines)):
    current_zona = int(lines[i][zona].replace("\n", ""))
    current_poblacion = lines[i][poblacion]
    current_causa = lines[i][causa]
    current_traffic_level = lines[i][nivel]
    current_date = lines[i][fecha]

    calculate_reason(current_zona, current_causa)
    calculate_traffic_level(current_zona, current_traffic_level)
    calculate_accidents_by_date(current_zona, current_date)
    calculate_accidents_by_hour(current_zona, current_date)

all_reasons = {}
for i in range(len(dic_reason.keys())):
    all_reasons[list(dic_reason.keys())[i][0]] = 1

all_traffic_level = {}
for i in range(len(dic_traffic_level.keys())):
    all_traffic_level[list(dic_traffic_level.keys())[i][0]] = 1


line = ""
with open('out/datos2007_features.csv', 'w') as f_out:
    for zone in range(158):
        try:
            line = str(dic_reason['Obras', zone]) + ";"
        except KeyError:
            line = "0;"

        try:
            line += str(dic_traffic_level['Rojo', zone]) + ";"
        except KeyError:
            line += "0;"

        try:
            line += str(dic_traffic_level['Amarillo', zone]) + ";"
        except KeyError:
            line += "0;"

        try:
            line += str(dic_traffic_level['Negro', zone]) + ";"
        except KeyError:
            line += "0;"

        try:
            line += str(dic_traffic_level['Blanco', zone]) + ";"
        except KeyError:
            line += "0;"

        try:
            line += str(dic_winter_acc[zone]) + ";"
        except KeyError:
            line += "0;"

        try:
            line += str(dic_summer_acc[zone]) + ";"
        except KeyError:
            line += "0;"

        try:
            line += str(dic_8_15_accidents[zone]) + ";"
        except KeyError:
            line += "0;"

        try:
            line += str(dic_15_20_accidents[zone]) + ";"
        except KeyError:
            line += "0;"

        try:
            line += str(dic_20_3_accidents[zone])
        except KeyError:
            line += "0"

        f_out.write(line + "\n")
