# Clase principal
class Persona:
    def __init__(self, nombre, apellido, identificacion, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.identificacion = identificacion
        self.telefono = telefono

# Clase empleado con la herencia de la clase "Persona"
class Empleado(Persona):
    def __init__(self, nombre, apellido, identificacion, telefono, salario):
        super().__init__(nombre, apellido, identificacion, telefono)
        self.salario = salario

# Clase Cliente con la herencia de la clase "Persona"
class Cliente(Persona):
    def __init__(self, nombre, apellido, identificacion, telefono, categoria):
        super().__init__(nombre, apellido, identificacion, telefono)
        self.categoria = categoria

# Creamos una funcion para agregar los datos a los objetos
def cargarDatos ():
    # La diferencia entre empleado y cliente es que empleado tiene salario y cliente tiene categoria. Preguntamos si es empleado
    respuesta = input('¿Va a agregar un empleado?')
    
    # Si la respuesta es si, ejecutamos el bloque que agrega los empleado por medio de input´s
    if respuesta == 'si' or respuesta == 'SI' or respuesta == 'Si':
        
        nombre = input('Ingrese su nombre')
        apellido = input('Ingrese su apellido')
        identificacion = input('Ingrese su indentificacion')
        telefono = input('Ingrese su telefono')
        salario = input('Ingrese su salario')
        
        emp = Empleado(nombre, apellido, str(identificacion), str(telefono), str(salario))
        # Preguntamos si quiere ver el empleado agregado, si la respuesta es si, lo muetra y acaba el programa, si es no, aaba el programa directamente
        pregunta = input('Empleado agregado correctamente, desea verlo?')
        
        if pregunta == 'si' or pregunta == 'Si' or pregunta == 'SI':
        # Mostramos los datos del empleado
                print('Nombre: ' + emp.nombre)
                print('Apellido: ' + emp.apellido)
                print('Identificacion: ' + emp.identificacion)
                print('Telefono: ' + emp.telefono)
                print('Salario: ' + emp.salario)
        
        else:
                print('Esta bien')

    # En caso de no ser empleado, ejecutamos el segundo if, que ejecuta el bloque de cliente
    elif respuesta == 'no' or respuesta == 'NO' or respuesta == 'No':
        # Se ingresan los datos por medio de input´s
        nombre = input('Ingrese su nombre')
        apellido = input('Ingrese su apellido')
        identificacion = input('Ingrese su indentificacion')
        telefono = input('Ingrese su telefono')
        # Preguntamos la categoria del cliente por medio de un input que pregunta true/false, true para vip, false para no-vip
        categoria = input('ingrese true/false')
        
        # Validamos la respuesta
        # si se eligio true, ejecuta el codigo y agrega la categoria "vip"
        if categoria == 'true' or categoria == 'TRUE' or categoria == 'True':
            
            cli = Cliente(nombre, apellido, str(identificacion), str(telefono), 'vip')
            # preguntamos si quiere ver los datos, si responde sí, muetra los datos y acaba el programa, si dice no, acaba de programa
            pregunta = input('Se ha agregado el cliente correctamente, desea Verlo?')
            
            if pregunta == 'si' or pregunta == 'Si' or pregunta == 'SI':
                print('Nombre: ' + cli.nombre)
                print('Apellido: ' + cli.apellido)
                print('Identificacion: ' + cli.identificacion)
                print('Telefono: ' + cli.telefono)
                print('Categoria: ' + cli.categoria)
            
            else:
                print('Esta bien')
        
        # Si elije false, agrega los datos y por defecto agrega la categoria "no-vip"
        elif categoria == 'false' or categoria == 'FALSE' or categoria == 'False':
            
            cli = Cliente(nombre, apellido, str(identificacion), str(telefono), 'no-vip')
            # preguntamos si quiere ver los datos, si responde si, muestra los datos y acaba el programa, si dice no, acaba el programa
            pregunta = input('Se ha agregado el cliente correctamente, desea Verlo?')
            
            if pregunta == 'si' or pregunta == 'Si' or pregunta == 'SI':
                print('Nombre: ' + cli.nombre)
                print('Apellido: ' + cli.apellido)
                print('Identificacion: ' + cli.identificacion)
                print('Telefono: ' + cli.telefono)
                print('Categoria: ' + cli.categoria)
            else:
                print('Esta bien')
    
    # Si se ingresn datos incorrectos, mostramos mensaje
    else:
        print('Ha ocurrido un error al momento de agregar un tipo de persona, intentelo luego')
        

# Ejecutamos la función
cargarDatos()