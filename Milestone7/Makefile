all: main

PYTHON_VER := python

DIRSRC := src/
DIROUT := out/
FILENAME := decision_tree

main:
	$(PYTHON_VER) $(DIRSRC)decision_tree.py
	convert $(DIROUT)$(FILENAME).pdf $(DIROUT)$(FILENAME).png

clean:
	$(RM) $(DIROUT)*

install:
	pip install graphviz
	sudo apt-get install python-pydot
