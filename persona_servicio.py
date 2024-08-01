from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox
import re

from Dominio.persona import Persona
from GUI.vtn_principal import Ui_vtn_principal
from Datos.persona_dao import PersonaDao

class PersonaServicio(QMainWindow):
    def __init__(self):
        super(PersonaServicio, self).__init__()
        self.ui = Ui_vtn_principal()
        self.ui.setupUi(self)
        self.ui.text_cedula.setValidator(QIntValidator())
        self.ui.text_edad.setValidator(QIntValidator(0, 999))
        self.ui.text_nombre.setMaxLength(50)
        self.ui.text_apellido.setMaxLength(50)
        self.ui.btn_guardar.clicked.connect(self.guardar)

    def validar_email(self, email):
        patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(patron, email) is not None

    def guardar(self):
        cedula = self.ui.text_cedula.text()
        nombre = self.ui.text_nombre.text().capitalize()
        apellido = self.ui.text_apellido.text().capitalize()
        correo = self.ui.text_correo.text()
        edad = self.ui.text_edad.text()

        if cedula == '' or len(cedula) < 10 or nombre == '' or apellido == '' or correo == '' or edad == '':
            QMessageBox.critical(self, 'Error', 'No se pudo guardar la persona.')
        elif not self.validar_email(correo):
            QMessageBox.critical(self, 'Error', 'Correo electrónico no válido.')
        else:
            persona = Persona(cedula=cedula, apellido=apellido, nombre=nombre, correo=correo, edad=edad)
            try:
                registro = PersonaDao.insertar_persona(persona)
                if registro != -1:
                    print('Se guardó la información')
                    self.ui.stb_estado.showMessage('Se guardó la persona.', 5000)
                    self.ui.text_cedula.setText('')
                    self.ui.text_apellido.setText('')
                    self.ui.text_nombre.setText('')
                    self.ui.text_edad.setText('')
                    self.ui.text_correo.setText('')
                else:
                    print('No se guardó')
                    QMessageBox.critical(self, 'Error', 'No se pudo guardar la persona.')
            except Exception as e:
                print(f'Error al insertar en la base de datos: {e}')
            print(persona)

    ##Integrantes: Jhon Pazmiño Menozcal, Ariel Rivas Romero