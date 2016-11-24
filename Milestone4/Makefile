all: pca_hierarchical

PYTHON_VER := python

DIRSRC := src/
DIROUT := out/

gen_features:
	$(PYTHON_VER) $(DIRSRC)calculate_zones.py
	$(PYTHON_VER) $(DIRSRC)generate_features.py

pca_hierarchical: #gen_features
	$(PYTHON_VER) $(DIRSRC)pca_hierarchical.py

dir:
	mkdir -f $(DIROUT)/

clean:
	$(RM) $(DIROUT)*.csv
