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
    * Number of accidents in winter (22 diciembre - 21 marzo)
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

dic_town = {}
dict_reason = {}
dict_traffic_level = {}
acc_winter = 0
acc_summer = 0
acc_8_15 = 0
acc_15_20 = 0
acc_20_3 = 0

lines = []
with open('data/inc2006zone.csv') as f_in:
    for line in f_in:
        lines.append(line.split(";"))

for i in xrange(len(lines)):
    current_zona = int(lines[i][zona].replace("\n", ""))

    current_poblacion = lines[i][poblacion]
    if current_poblacion != '':
        try:
            dic_town[current_poblacion, current_zona] += 1
        except KeyError:
            dic_town[current_poblacion, current_zona] = 1

abc = {}
for i in xrange(len(dic_town.keys())):
    abc[dic_town.keys()[i][0]] = 1

print abc.keys()
