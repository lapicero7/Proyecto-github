Algoritmo ImpuestoIva
	definir a Como Real
	escribir "Ingrese el número de articulos comprados"
	leer a 
	Si a=5 Entonces
		articulo1=33.44
		articulo2=28.59
		articulo3=10
		articulo4=42.23
		articulo5=12.50
		totalcom=(articulo1+articulo2+articulo3+articulo4+articulo5)
		IVA=totalcom*0.12
		totalcan=totalcom+IVA
		escribir "Total de la compra: " , totalcom
		escribir "IVA: " , IVA
		escribir "El total a cancelar es de: ", totalcan
	Fin Si
FinAlgoritmo
