"""
****elif
Nos sirve para tener una cadena de ifs pero si una condicion se cumple de varias, solo se
realizara esa accion por orden de cual fue escrita primero
if condicion:
    lineas de codigo
elif condicion:
    lineas de codigo
****try-except
Nos sirve para cuando sabemos que algo pude fallar y en caso de que eso ocurra nos envia a
otra parte de nuestro codigo saltando el error y continuando con el codigo
Si el try funciona correctamente omite el except

"""
xi=input('Digite un numero')
try:
    x=float(xi)
    if x>1:
        print("Digito un numero positivo mayor que 1")
    elif x>0:
        print('Digito un numero positivo menor que uno')
    elif x==0:
        print('Digito el 0')
    else:
        print('Digito un numero negativo')
except:
    print('No digito un numero, es un estupido o digito un decimal con coma')
