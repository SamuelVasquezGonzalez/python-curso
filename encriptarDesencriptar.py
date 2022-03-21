def encriptar(texto):
    textoFinal = ''
    for letra in texto:
        textoFinal += letra + 'x'
    return textoFinal


def desencriptar(texto):
    textoFinal = ''
    contador = 0
    for letra in texto:
        if contador % 2 == 0:
            textoFinal += letra
        contador += 1
    return textoFinal


def encriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)
    
    archivo = open(rutaArchivo, 'w')
    archivo.write(textoEncriptado)
    archivo.close()


def desencriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)
    
    archivo = open(rutaArchivo, 'w')
    archivo.write(textoDesencriptado)
    archivo.close()


respuesta = input('Presione la letra E para encriptar, o D para desencriptar')
rutaArchivo = input('Ingrese la ruta del archivo')

if respuesta == 'E' or respuesta == 'e':
    encriptarArchivo(rutaArchivo)

if respuesta == 'D' or respuesta == 'd':
    desencriptarArchivo(rutaArchivo)

else:
    print('Solo presione la letra E o D')
