all: hierarchical

PYTHON_VER := python

DIRSRC := src/
DIROUT := out/

gen_features:
	$(PYTHON_VER) $(DIRSRC)calculate_zones.py
	$(PYTHON_VER) $(DIRSRC)generate_feature.py

pca: gen_features
	$(PYTHON_VER) $(DIRSRC)pca.py

hierarchical: gen_features
	$(PYTHON_VER) $(DIRSRC)hierarchical.py

mkdir:
	mkdir -f $(DIROUT)/

clean:
	$(RM) $(DIROUT)*
