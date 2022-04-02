class Persona:
    def __init__(self, nombre, apellido, identificacion, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.identificacion = identificacion
        self.telefono = telefono

class Empleado(Persona):
    def __init__(self, nombre, apellido, identificacion, telefono, salario):
        super().__init__(nombre, apellido, identificacion, telefono)
        self.salario = salario


class Cliente(Persona):
    def __init__(self, nombre, apellido, identificacion, telefono, categoria):
        super().__init__(nombre, apellido, identificacion, telefono)
        self.categoria = categoria


def cargarDatos ():
    respuesta = input('¿Va a agregar un empleado?')
    
    if respuesta == 'si' or respuesta == 'SI' or respuesta == 'Si':
        
        nombre = input('Ingrese su nombre')
        apellido = input('Ingrese su apellido')
        identificacion = input('Ingrese su indentificacion')
        telefono = input('Ingrese su telefono')
        salario = input('Ingrese su salario')
        
        emp = Empleado(nombre, apellido, str(identificacion), str(telefono), str(salario))
        pregunta = input('Empleado agregado correctamente, desea verlo?')
        
        if pregunta == 'si' or pregunta == 'Si' or pregunta == 'SI':
                print('Nombre: ' + emp.nombre)
                print('Apellido: ' + emp.apellido)
                print('Identificacion: ' + emp.identificacion)
                print('Telefono: ' + emp.telefono)
                print('Salario: ' + emp.salario)
        
        else:
                print('Esta bien')

    elif respuesta == 'no' or respuesta == 'NO' or respuesta == 'No':
        
        nombre = input('Ingrese su nombre')
        apellido = input('Ingrese su apellido')
        identificacion = input('Ingrese su indentificacion')
        telefono = input('Ingrese su telefono')
        categoria = input('ingrese true/false')
        
        if categoria == 'true' or categoria == 'TRUE' or categoria == 'True':
            
            cli = Cliente(nombre, apellido, str(identificacion), str(telefono), 'vip')
            pregunta = input('Se ha agregado el cliente correctamente, desea Verlo?')
            
            if pregunta == 'si' or pregunta == 'Si' or pregunta == 'SI':
                print('Nombre: ' + cli.nombre)
                print('Apellido: ' + cli.apellido)
                print('Identificacion: ' + cli.identificacion)
                print('Telefono: ' + cli.telefono)
                print('Categoria: ' + cli.categoria)
            
            else:
                print('Esta bien')
        elif categoria == 'false' or categoria == 'FALSE' or categoria == 'False':
            
            cli = Cliente(nombre, apellido, str(identificacion), str(telefono), 'no-vip')
            pregunta = input('Se ha agregado el cliente correctamente, desea Verlo?')
            
            if pregunta == 'si' or pregunta == 'Si' or pregunta == 'SI':
                print('Nombre: ' + cli.nombre)
                print('Apellido: ' + cli.apellido)
                print('Identificacion: ' + cli.identificacion)
                print('Telefono: ' + cli.telefono)
                print('Categoria: ' + cli.categoria)
            else:
                print('Esta bien')
    
    else:
        print('Ha ocurrido un error al momento de agregar un tipo de persona, intentelo luego')
        


cargarDatos()