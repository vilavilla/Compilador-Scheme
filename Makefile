antlr:
	antlr4 -Dlanguage=Python3 scheme.g4

build: antlr
	python3 -m pip install antlr4-python3-runtime

run: build
	python3 scheme.py programa.scm

aux:
	java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -no-listener scheme.g4
