all: main

PYTHON_VER := python

DIRSRC := src/
DIROUT := out/

knn:
	$(PYTHON_VER) $(DIRSRC)knn.py

filter:
	$(PYTHON_VER) $(DIRSRC)filter.py

parse:
	$(PYTHON_VER) $(DIRSRC)parserXML2CSV.py

pretty_xml:
	python3 $(DIRSRC)prettyXML.py #python3 as it solves natively codification issues

clean:
	$(RM) $(DIROUT)*

full: pretty_xml parse filter knn
