antlr:
	antlr4 -Dlanguage=Python3 -visitor Scheme.g4

build: antlr
	python3 -m pip install antlr4-python3-runtime

run: build
	python3 Scheme.py programa.scm

aux:
	java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -no-listener Scheme.g4

test: aux
	@echo "Ejecutando pruebas..."
	@python3 Scheme.py Juegos-prueba/suma.scm > Juegos-prueba/suma_test.out
	@diff -q Juegos-prueba/suma_test.out Juegos-prueba/suma.out && echo "Prueba suma.scm completada correctamente" || echo "Error en prueba: suma.scm"

	@python3 Scheme.py Juegos-prueba/recursiva.scm > Juegos-prueba/recursiva_test.out
	@diff -q Juegos-prueba/recursiva_test.out Juegos-prueba/recursiva.out && echo "Prueba recursiva.scm completada correctamente" || echo "Error en prueba: recursiva.scm"

	@python3 Scheme.py Juegos-prueba/cond.scm > Juegos-prueba/cond_test.out
	@diff -q Juegos-prueba/cond_test.out Juegos-prueba/cond.out && echo "Prueba cond.scm completada correctamente" || echo "Error en prueba: cond.scm"

	@python3 Scheme.py Juegos-prueba/let.scm > Juegos-prueba/let_test.out
	@diff -q Juegos-prueba/let_test.out Juegos-prueba/let.out && echo "Prueba let.scm completada correctamente" || echo "Error en prueba: let.scm"

	@python3 Scheme.py Juegos-prueba/map.scm > Juegos-prueba/map_test.out
	@diff -q Juegos-prueba/map_test.out Juegos-prueba/map.out && echo "Prueba map.scm completada correctamente" || echo "Error en prueba: map.scm"

	@python3 Scheme.py Juegos-prueba/entrada.scm < Juegos-prueba/entrada.inp > Juegos-prueba/entrada_test.out
	@diff -q Juegos-prueba/entrada_test.out Juegos-prueba/entrada.out && echo "Prueba entrada.scm completada correctamente" || echo "Error en prueba: entrada.scm"

	@echo "Pruebas completadas."

test2: aux
	@echo "Ejecutando pruebas adicionales..."

	@python3 Scheme.py Juegos-prueba2/prueba_compleja.scm > Juegos-prueba2/prueba_compleja_test.out
	@diff -q Juegos-prueba2/prueba_compleja_test.out Juegos-prueba2/prueba_compleja.out && echo "Prueba prueba_compleja.scm completada correctamente" || echo "Error en prueba: prueba_compleja.scm"

	@python3 Scheme.py Juegos-prueba2/prueba_errores.scm > Juegos-prueba2/prueba_errores_test.out
	@diff -q Juegos-prueba2/prueba_errores_test.out Juegos-prueba2/prueba_errores.out && echo "Prueba prueba_errores.scm completada correctamente" || echo "Error en prueba: prueba_errores.scm"

	@python3 Scheme.py Juegos-prueba2/prueba_orden_superior.scm > Juegos-prueba2/prueba_orden_superior_test.out
	@diff -q Juegos-prueba2/prueba_orden_superior_test.out Juegos-prueba2/prueba_orden_superior.out && echo "Prueba prueba_orden_superior.scm completada correctamente" || echo "Error en prueba: prueba_orden_superior.scm"

	@python3 Scheme.py Juegos-prueba2/prueba_recursiva.scm > Juegos-prueba2/prueba_recursiva_test.out
	@diff -q Juegos-prueba2/prueba_recursiva_test.out Juegos-prueba2/prueba_recursiva.out && echo "Prueba prueba_recursiva.scm completada correctamente" || echo "Error en prueba: prueba_recursiva.scm"

	@echo "Pruebas adicionales completadas."
