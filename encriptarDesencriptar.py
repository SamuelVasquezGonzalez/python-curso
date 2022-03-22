def encriptar(texto):
    textoFinal = ''
    for letra in texto:
        ascii = ord(letra)
        ascii += 2
        textoFinal += chr(ascii)
    return textoFinal


def desencriptar(texto):
    textoFinal = ''
    for letra in texto:
        ascii = ord(letra)
        ascii -= 2
        textoFinal += chr(ascii)
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
    print('Ha sido Encriptado!!')
    encriptarArchivo(rutaArchivo)

if respuesta == 'D' or respuesta == 'd':
    print('Ha sido desencriptado!!')
    desencriptarArchivo(rutaArchivo)