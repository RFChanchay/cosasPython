""" ***def
    Es comunmente lo que llamas programacion estructurada donde definimos una funcion o codigo
    que posteriormente nos puede ser util
    se lo escribe:
    def nombreDeLaFuncion():
        lineas de codigo
    para llamar a la funcion escribimos
    nombreDeLaFuncion()

    """
def mensaje():
    print('Vales mucho cuidate guap@')

respuesta=input('Quiere ver un mensaje?')

if respuesta=='si':
    mensaje()
elif respuesta=="no":
    print("ya nada")
else:
    print('Escribe si o no chucha tu madre')
