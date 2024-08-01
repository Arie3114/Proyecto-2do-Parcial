import sys

from PySide6.QtWidgets import QApplication

from Servicios.persona_servicio import PersonaServicio

app = QApplication(sys.argv)
vtn_principal = PersonaServicio()
vtn_principal.show()
sys.exit(app.exec())

##Integrantes: Jhon Pazmiño Menozcal, Ariel Rivas Romero