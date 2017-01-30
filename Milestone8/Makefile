all: main

PYTHON_VER := python

DIRSRC := src/
DIROUT := out/

decision_tree:
	$(PYTHON_VER) $(DIRSRC)decision_tree.py

hierarchical:
	$(PYTHON_VER) $(DIRSRC)hierarchical.py

gen_features:
	$(PYTHON_VER) $(DIRSRC)generate_features.py

knn:
	$(PYTHON_VER) $(DIRSRC)knn.py

filter:
	$(PYTHON_VER) $(DIRSRC)filter.py

parse:
	$(PYTHON_VER) $(DIRSRC)parserXML2CSV.py

pretty_xml:
	python3 $(DIRSRC)prettyXML.py #python3 as it solves natively codification issues

clean:
	$(RM) $(DIRSRC)*.pyc

full: pretty_xml parse filter knn gen_features hierarchical decision_tree
