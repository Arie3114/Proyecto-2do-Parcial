class Persona:
    def __init__(self, cedula=None, nombre=None, apellido=None, correo=None, edad=None):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._edad = edad

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, nueva_cedula):
        self._cedula = nueva_cedula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, nuevo_correo):
        self._correo = nuevo_correo

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

    def __str__(self):
        return f'Persona: {self._nombre} {self._apellido}, Correo: {self._correo}, Edad: {self._edad}'

if __name__ == '__main__':
    # Ejemplo de uso:
    persona1 = Persona(cedula="123456789", nombre="Juan", apellido="Pérez", correo="juan.perez@example.com", edad=30)
    print(f"Cédula: {persona1.cedula}, Nombre: {persona1.nombre}, Apellido: {persona1.apellido}, Correo: {persona1.correo}, Edad: {persona1.edad}")
    print(persona1)

    ##Integrantes: Jhon Pazmiño Menozcal, Ariel Rivas Romero