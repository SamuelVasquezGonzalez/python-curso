numeros = {
    "0": "cero",
    "1": "uno",
    "2": "dos",
    "3": "tres",
    "4": "cuatro",
    "5": "cinco",
    "6": "seis",
    "7": "siete",
    "8": "ocho",
    "9": "nueve"
}

texto = input('Ingresa un numero: ')

textoFinal = ''
for letra in texto:  #Se intera cada posicion del numero que le pasamos y se guarda en la variable 'letra'
    textoFinal += numeros[letra] + ' ' #le estamos diciendo que texto final va a guardar todo el objeto con la posicion que esta guardada en la variable 'letra'
    
print(textoFinal) #Y la mostramos