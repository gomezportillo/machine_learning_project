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

km_ini = 0
tipo = 1
latitud = 2
causa = 3
km_final = 4
matricula = 5
nivel = 6
sentido = 7
provincia = 8
carretera = 9
fecha = 10
autonomia = 11
longitud = 12
poblacion = 13
zona = 14

dic_reason = {}
dic_traffic_level = {}
dic_winter_acc = {}
dic_summer_acc = {}
dic_8_15_accidents = {}
dic_15_20_accidents = {}
dic_20_3_accidents = {}

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

lines = []
with open('data/inc2006zone.csv') as f_in:
    for line in f_in:
        lines.append(line.split(";"))

for i in xrange(len(lines)):
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
for i in xrange(len(dic_reason.keys())):
    all_reasons[dic_reason.keys()[i][0]] = 1

all_traffic_level = {}
for i in xrange(len(dic_traffic_level.keys())):
    all_traffic_level[dic_traffic_level.keys()[i][0]] = 1

all_colums = []

for r in all_reasons.keys():
    all_colums.append(r)

for t in all_traffic_level.keys():
    all_colums.append(t)

all_colums.append("Winter accidents")
all_colums.append("Summer accidents")
all_colums.append("8-15 accidents")
all_colums.append("15-20 accidents")
all_colums.append("20-3 accidents")

print all_colums

line = ""
with open('out/my_data.csv', 'w') as f_out:
    f_out.write(str(all_colums) + "\n")
    for zone in xrange(158):
        try:
            line = str(dic_reason['Alcance', zone]) + ";"
        except KeyError:
            line = "0;"

        try:
            line += str(dic_reason['Atropello', zone]) + ";"
        except KeyError:
            line += "0;"

        try:
            line += str(dic_reason['Vuelco', zone]) + ";"
        except KeyError:
            line += "0;"

        try:
            line += str(dic_reason['Tijera camin', zone]) + ";"
        except KeyError:
            line += "0;"

        try:
            line += str(dic_reason['Salida', zone]) + ";"
        except KeyError:
            line += "0;"

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
            line += "0;"

        f_out.write(line + "\n")
