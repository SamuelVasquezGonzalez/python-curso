seguirChateando = True
while seguirChateando:
    print('Escribe "Salir" para terminar el chat')
    texto = input('>')
    if texto == 'salir' or texto == 'Salir':
        print("Esperamos que vuelvas pronto")
        seguirChateando = False
    texto = texto.replace(':)', '😀')
    texto = texto.replace(':p', '😛')
    texto = texto.replace(':P', '😛')
    texto = texto.replace(':(', '😔')
    texto = texto.replace(':*', '😘')
    texto = texto.replace(';(', '😠')

    print(texto)