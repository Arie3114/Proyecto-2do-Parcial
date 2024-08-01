from Datos.conexion import Conexion
from Dominio.persona import Persona


class PersonaDao:
    # _INSERTAR_PERSONA = "INSERT INTO Persona (nombre, apellido, cedula, correo, edad) VALUES (?, ?, ?, ?, ?)"
    _INSERTAR_PERSONA = "INSERT INTO Personas (nombre, apellido, cedula, email, edad) VALUES (?, ?, ?, ?, ?)"

    _SELECCIONAR_PERSONAS = 'select idPersona,Nombre,Apellido,Cedula,Email,Edad from Personas'
    @classmethod
    def insertar_persona(cls, persona):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (persona.nombre, persona.apellido, persona.cedula, persona.correo, persona.edad)
                registros = cursor.execute(cls._INSERTAR_PERSONA, datos)
                return registros
        except Exception as e:
            print(e)
            return -1

    @classmethod
    def seleccionar_personas(cls):
        personas = list()
        try:
            with Conexion.obtenerCursor() as cursor:
                registros = cursor.execute(cls._SELECCIONAR_PERSONAS).fetchall()
                for registro in registros:
                    persona = Persona()
                    persona.nombre = registro[1]
                    persona.apellido = registro[2]
                    persona.cedula = registro[3]
                    persona.correo = registro[4]
                    persona.edad = registro[5]
                    personas.append(persona)
                return personas
        except Exception as e:
            personas = None
            return personas
            print(e)


if __name__ == '__main__':
    personas = PersonaDao.seleccionar_personas()
    for persona in personas:
        print(persona)

    ##Integrantes: Jhon Pazmiño Menozcal, Ariel Rivas Romero
