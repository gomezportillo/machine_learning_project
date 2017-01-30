#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Andrés Montoro Montarroso
@author: Pedro Manuel Gómez-Portillo
"""

from random import randint

def generateZonesCSV():
	with open('data/inc2006zone.csv') as f_zones_in:
		with open('out/zones.csv', 'w') as f_zones_out:
			for line in f_zones_in:
				split_line = line.split(";")
				lat = split_line[2]
				lon = split_line[12]
				zone = split_line[14].replace('\n', '')

				f_zones_out.write("{};{};{}\n".format(lat, lon, zone))

def generateWorksCSV():
	with open('data/inc2006works.csv') as f_works_in:
		with open('out/works.csv', 'w') as f_works_out:
			for line in f_works_in:
				split_line = line.split(";")
				if 'Obras' in split_line[3]:
					lat = split_line[2]
					lon = split_line[12]

					f_works_out.write("{};{}\n".format(lat, lon))

def normaliseWorksCSV():
	dict_works = dict()
	with open('out/works.csv') as f_works_in:
		with open('out/works_normalised.csv', 'w') as f_works_out:
			for line in f_works_in:
				split_line = line.split(";")
				lat = split_line[0]
				lon = split_line[1]
				try:
					dict_works[lat, lon] += 1
				except KeyError:
					dict_works[lat, lon] = 1
					f_works_out.write(line)

def randomizeZonesCSV():
	with open('out/zones.csv') as f_zones_in:
		with open('out/zones_random_60.csv', 'w') as f_zones_out_60:
			with open('out/zones_random_40.csv', 'w') as f_zones_out_40:

				for line in f_zones_in:
					if randint(0,10) <= 6:
						f_zones_out_60.write(line)
					else:
						f_zones_out_40.write(line)


generateZonesCSV()
generateWorksCSV()
normaliseWorksCSV()
randomizeZonesCSV()
