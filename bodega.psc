Algoritmo bodega
	opciones = "a"
	Mientras opciones <> "salir" o opciones == "a" Hacer
		Escribir "Cantidad de Galones de Biox: "
		Leer cantidad_galones
		Escribir "Galones vendidos en el mes: "
		Leer galones_x_mes
		
		Si cantidad_galones > galones_x_mes Entonces
			stock = stock + cantidad_galones
			stock = stock - galones_x_mes
			porcentaje = stock * cantidad_galones / 100
			mes = galones_x_mes * 16
			semana = (galones_x_mes / 4) * 16
			dia = (galones_x_mes / 30) * 16
			
			Escribir "Total de ventas por mes de BIOX: $", mes
			Escribir "Total de ventas por semana de BIOX: $", semana
			Escribir "Total de ventas por dia de BIOX: $", dia
			Escribir "Porcentaje: ", porcentaje * 100
		FinSi

		Escribir "Para salir del programa escriba (salir): "
		Leer opciones
	Fin Mientras
FinAlgoritmo
