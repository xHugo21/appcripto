'''Clase que contiene el rol "Super". Es el rol con más permisos y se le permite añadir doctores y pacientes'''

# Imports
from checks import Checks
from json_things.jsonmethods import JsonMethods


class Super:
    def __init__(self, cuenta):
        self.cuenta = cuenta  # JSON que contiene la información de super
        self.datos = JsonMethods.obtener_datos(cuenta)  # Almacena los datos de super

        # ¿Mover a interfaz.py?
        # Bucle de la interfaz de super
        while True:
            print('BIENVENIDO ' + self.cuenta['Nombre'] + ' ' + self.cuenta["Apellidos"])
            print('¿Qué desea hacer?\n'
                  '0. Atrás\n'
                  '1. Mis pacientes\n'
                  '2. Buscar paciente\n')
            decision = Checks.check_numero_teclado(2)  # Obtener input
            print(decision)
            # Si decision == 0 -> Atrás
            if decision == 0:
                print('Atrás')
                break
            # Si decision == 1 -> Mis pacientes
            elif decision == 1:
                print('aqui')
                self.paciente(self.lista_pacientes())
                # Si decision == 2 -> Buscar paciente
            elif decision == 2:
                self.paciente(self.buscar_paciente())

    def lista_pacientes(self):
        '''Método que devuelve la lista de pacientes asociados a un doctor'''
        id_doctor = self.cuenta["ID"]
        contador = 0
        pacientes = []
        for i in range(len(self.datos)):
            if int(self.datos[i]['Nivel']) == 0:
                contador += 1
                pacientes.append(self.datos[i]['ID'])
                print(str(contador) + '. ' + self.datos[i]['Nombre'] + ' ' + self.datos[i]['Apellidos'])
        return pacientes[Checks.check_numero_teclado(len(pacientes)) - 1]

    def paciente(self, id_paciente):
        for i in range(len(self.datos)):
            if self.datos[i]['ID'] == id_paciente:
                print(self.datos[i]['Expediente'])
        print('0. Atras')
        Checks.check_numero_teclado(0)

    def buscar_paciente(self):
        '''Método que permite buscar un paciente en concreto'''
        busqueda = input('buscar: ')
        contador = 0
        pacientes = []
        for i in range(len(self.datos)):
            if (int(self.datos[i]['Nivel']) == 0 and
                    (busqueda == self.datos[i]['Nombre'] or
                     busqueda == self.datos[i]['Apellidos'] or
                     busqueda == self.datos[i]['ID'])):
                contador += 1
                pacientes.append(self.datos[i]['ID'])
                print(str(contador) + '. ' + self.datos[i]['Nombre'] + ' ' + self.datos[i]['Apellidos'])
        return pacientes[Checks.check_numero_teclado(len(pacientes)) - 1]

    def añadir_doctor(self):
        '''Método que permite añadir doctores'''
        pass
    #Añadir doctores