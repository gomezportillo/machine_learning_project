all: main

PYTHON_VER := python

DIRSRC := src/
DIROUT := out/

main:
	$(PYTHON_VER) $(DIRSRC)decision_tree.py

clean:
	$(RM) $(DIROUT)*

install:
	pip install graphviz
	sudo apt-get install python-pydot
