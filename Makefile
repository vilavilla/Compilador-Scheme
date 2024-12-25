antlr:
	antlr4 -Dlanguage=Python3 -visitor Scheme.g4

build: antlr
	python3 -m pip install antlr4-python3-runtime

aux:
	java -jar aux/antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -no-listener Scheme.g4

test: antlr
	@echo "Ejecutando test..."
	
	@echo ""
	@echo "Test simples..."
	@echo ""
	
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
	
	@echo ""
	@echo "Test complejos..."
	@echo ""
	@python3 Scheme.py Juegos-prueba/prueba_orden_superior.scm > Juegos-prueba/prueba_orden_superior_test.out
	@diff -q Juegos-prueba/prueba_orden_superior_test.out Juegos-prueba/prueba_orden_superior.out && echo "Prueba prueba_orden_superior.scm completada correctamente" || echo "Error en prueba: prueba_orden_superior.scm"

	@python3 Scheme.py Juegos-prueba/prueba_recursiva.scm > Juegos-prueba/prueba_recursiva_test.out
	@diff -q Juegos-prueba/prueba_recursiva_test.out Juegos-prueba/prueba_recursiva.out && echo "Prueba prueba_recursiva.scm completada correctamente" || echo "Error en prueba: prueba_recursiva.scm"

	@python3 Scheme.py Juegos-prueba/main.scm > Juegos-prueba/main_test.out
	@diff -q Juegos-prueba/main.out Juegos-prueba/main_test.out && echo "Prueba main.scm completada correctamente" || echo "Error en prueba: main.scm"
	
	@python3 Scheme.py Juegos-prueba/extra.scm > Juegos-prueba/extra_test.out
	@diff -q Juegos-prueba/extra.out Juegos-prueba/extra_test.out && echo "Prueba prueba_orden_superior.scm completada correctamente" || echo "Error en prueba: prueba_orden_superior.scm"
	
	@echo ""
	@echo "Test errores..."
	@echo ""
	@python3 Scheme.py Juegos-prueba/errores1.scm > Juegos-prueba/errores1_test.out
	@diff -q Juegos-prueba/errores1_test.out Juegos-prueba/errores1.out && echo "Prueba errores1.scm completada correctamente" || echo "Error en prueba: errores1.scm"

	@python3 Scheme.py Juegos-prueba/errores2.scm > Juegos-prueba/errores2_test.out
	@diff -q Juegos-prueba/errores2_test.out Juegos-prueba/errores2.out && echo "Prueba errores2.scm completada correctamente" || echo "Error en prueba: errores2.scm"

	@python3 Scheme.py Juegos-prueba/errores3.scm > Juegos-prueba/errores3_test.out
	@diff -q Juegos-prueba/errores3_test.out Juegos-prueba/errores3.out && echo "Prueba errores3.scm completada correctamente" || echo "Error en prueba: errores3.scm"

	@python3 Scheme.py Juegos-prueba/errores4.scm > Juegos-prueba/errores4_test.out
	@diff -q Juegos-prueba/errores4_test.out Juegos-prueba/errores4.out && echo "Prueba errores4.scm completada correctamente" || echo "Error en prueba: errores4.scm"

	@python3 Scheme.py Juegos-prueba/errores5.scm > Juegos-prueba/errores5_test.out
	@diff -q Juegos-prueba/errores5_test.out Juegos-prueba/errores5.out && echo "Prueba errores5.scm completada correctamente" || echo "Error en prueba: errores5.scm"

	@python3 Scheme.py Juegos-prueba/errores6.scm < Juegos-prueba/errores6.inp > Juegos-prueba/errores6_test.out
	@diff -q Juegos-prueba/errores6_test.out Juegos-prueba/errores6.out && echo "Prueba errores6.scm completada correctamente" || echo "Error en prueba: errores6.scm"

	@python3 Scheme.py Juegos-prueba/errores7.scm > Juegos-prueba/errores7_test.out
	@diff -q Juegos-prueba/errores7_test.out Juegos-prueba/errores7.out && echo "Prueba errores7.scm completada correctamente" || echo "Error en prueba: errores7.scm"

	@python3 Scheme.py Juegos-prueba/errores8.scm > Juegos-prueba/errores8_test.out
	@diff -q Juegos-prueba/errores8_test.out Juegos-prueba/errores8.out && echo "Prueba errores8.scm completada correctamente" || echo "Error en prueba: errores8.scm"
	
	@echo ""
	@echo "Pruebas completadas."

