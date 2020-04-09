"""******CONDICIONALES*****
!=  < > <= >= ==
*if
if condicion:
    ---lineas de codigo
    para salir del if debemos salir de las lineas ya que aqui si importa el espacio
    usar el tab para ajustar el espacio

if condicion:
    lineas de codigo
else:
    lineas de codigo
"""
xi=input("Digite un numero: ")
x=float(xi)
if x>0:
    print("Su numero es positivo")
    nPar=x%2
    if nPar!=0:
        print("El numero es impar")
    else:
        print('El numero es par')
if  x<0:
    print("Su numero es negativo")
    nPar=x%2
    if nPar!=0:
        print('El numero es impar')
    else:
        print('El numero es par')
if x==0:
    print('El numero es 0')
