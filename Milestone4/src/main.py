#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Andrés Montoro Montarroso
@author: Pedro Manuel Gómez-Portillo
"""

"""
Tasks to achieve:
    * Number of accidents per town
    * Number of accidents per reason
    * Number of accidents per traffic level
    * Number of accidents in winter (enero2006 - 21 marzo2006 && 22 diembre2006 - 31dic2006)
    * Number of accidents in summer (20 junio - 23 septiembre)
    * Number of accidents from 8.00am to 15.00pm
    * Number of accidents from 15.00pm to 20.00pm
    * Number of accidents from 20.00pm to 3.00am
    *
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
fecha_ini = 10
autonomia = 11
longitud = 12
poblacion = 13
zona = 14

dict_town = {}
dict_reason = {}
dict_traffic_level = {}
acc_winter = 0
acc_summer = 0
acc_8_15 = 0
acc_15_20 = 0
acc_20_3 = 0

lines = []

def calculate_poblacion(current_zona, current_poblacion):
    if current_poblacion != '':
        try:
            dict_town[current_poblacion, current_zona] += 1
        except KeyError:
            dict_town[current_poblacion, current_zona] = 1

def calculate_reason(current_zona, current_causa):
    if current_causa != '':
        try:
            dict_reason[current_causa, current_zona] += 1
        except KeyError:
            dict_reason[current_causa, current_zona] = 1


with open('data/inc2006zone.csv') as f_in:
    for line in f_in:
        lines.append(line.split(";"))

for i in xrange(len(lines)):
    current_zona = int(lines[i][zona].replace("\n", ""))
    current_poblacion = lines[i][poblacion]
    current_causa = lines[i][causa]
    current_traffic_level = lines[i][nivel]

    calculate_poblacion(current_zona, current_poblacion)
    calculate_reason(current_zona, current_causa)
    calculate_traffic_level(current_zona, current_traffic_level) #<- por hacer!

all_towns = {}
for i in xrange(len(dict_town.keys())):
    all_towns[dict_town.keys()[i][0]] = 1

all_reasons = {}
for i in xrange(len(dict_reason.keys())):
    all_reasons[dict_reason.keys()[i][0]] = 1

all_traffic_level = {}
for i in xrange(len(dict_traffic_level.keys())):
    all_traffic_level[dict_traffic_level.keys()[i][0]] = 1


print all_reasons.keys()
print all_towns.keys()
print all_traffic_level.keys()
