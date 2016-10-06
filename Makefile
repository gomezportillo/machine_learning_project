all: exec

exec:
	python src/parserXML2CSV.py

clean:
	rm out/* src/*.pyc
