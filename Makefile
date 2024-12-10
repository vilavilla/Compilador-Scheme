antlr:
	antlr4 -Dlanguage=Python3 Scheme.g4

build: antlr
	python3 -m pip install antlr4-python3-runtime

run: build
	python3 Scheme.py programa.scm

aux:
	java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -no-listener Scheme.g4

test: build
	@echo "Ejecutando pruebas..."
	python3 Scheme.py Juegos-prueba/suma.scm > Juegos-prueba/suma_test.out
	@diff -q Juegos-prueba/suma_test.out Juegos-prueba/suma.out || echo "Error en prueba: suma.scm"

	python3 Scheme.py Juegos-prueba/recursiva.scm > Juegos-prueba/recursiva_test.out
	@diff -q Juegos-prueba/recursiva_test.out Juegos-prueba/recursiva.out || echo "Error en prueba: recursiva.scm"

	python3 Scheme.py Juegos-prueba/cond.scm > Juegos-prueba/cond_test.out
	@diff -q Juegos-prueba/cond_test.out Juegos-prueba/cond.out || echo "Error en prueba: cond.scm"

	python3 Scheme.py Juegos-prueba/let.scm > Juegos-prueba/let_test.out
	@diff -q Juegos-prueba/let_test.out Juegos-prueba/let.out || echo "Error en prueba: let.scm"

	python3 Scheme.py Juegos-prueba/map.scm > Juegos-prueba/map_test.out
	@diff -q Juegos-prueba/map_test.out Juegos-prueba/map.out || echo "Error en prueba: map.scm"

	python3 Scheme.py Juegos-prueba/entrada.scm < Juegos-prueba/entrada.inp > Juegos-prueba/entrada_test.out
	@diff -q Juegos-prueba/entrada_test.out Juegos-prueba/entrada.out || echo "Error en prueba: entrada.scm"

	@echo "Pruebas completadas."
