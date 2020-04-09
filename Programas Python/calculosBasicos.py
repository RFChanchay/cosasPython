"""
la division de enteros produce un float
potencia                                      **
residuo                                        %
para ver el tipo de dato usamos            type ()
para una declarar una string es recomendable usar 'una sola comilla'
si queremos decir  Let's deberiamos poner print('Let/'s')
podemos generar un parrafo de string usando triple comilla """ """
para transformar una dato en otro tipo de dato lo declaramos como otroname=int(elDatoAnterior)
float() str()
, nos permite concatenar con espacios
input() permite obtener datos del teclado en forma de string
"""
print("Bienvenido a Calculadora Rapida de enteros")
x=input("Ingrese el primer valor:")
x=int(x)
y=input("Ingrese el segundo valor:")
y=int(y)
print("Se registro el primer valor que es igual a: ")
print(x)
print("Se registro el segundo valor que es igual a: ")
print(y)
suma=str(x+y)
resta=str(x-y)
multiplicacion=str(x*y)
div=x/y
division=str(div)
potencia=str(x**y)
residuo=str(x%y)
print("El resultado de la suma es: "+suma)
print('El resultado de la resta es: '+resta)
print('El resultado de la multiplicacion es: '+multiplicacion)
print("El resultado de la division es: "+division+'con un resto de '+residuo)
x=str(x)
y=str(y)
print(x+" Elevado a la "+y+' es igual a: '+potencia)
