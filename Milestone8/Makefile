all: main

PYTHON_VER := python

DIRSRC := src/
DIROUT := out/

main:
	$(PYTHON_VER) $(DIRSRC)main.py

parse:
	$(PYTHON_VER) $(DIRSRC)parserXML2CSV.py

pretty_xml:
	python3 $(DIRSRC)prettyXML.py

clean:
	$(RM) $(DIROUT)*
