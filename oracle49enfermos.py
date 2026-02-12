# Vamos a crear clases de acceso a datos, services.
# Separararemos la capa de acceso a datos del programa de 
# Python
# Vamos a repetir una lógica, como 
# eliminar un enfermo por su inscripción
# Vamos a tener dos programas
# 1. la clase de datos;  oracle49enfermos.py (que será este)
# 2. la clase del programa: python49eliminarenfermo.py 
import oracledb
class OracleEnfermos:
    # Declarar las propiedades en el constructor
    def __init__(self):
        self.connection= oracledb.connect(user="SYSTEM",
                            password="oracle",
                            dsn="localhost/FREEPDB1")
# A partir de aquí los métodos
# Cada método tendrá la norma de Entrar/Salir (abrir y cerrar). 
    # Ahora escribimos el método de eliminar enfermo
    def eliminarEnfermo(self, inscripcion):
        # Creamos un nuevo cursor
        cursor=self.connection.cursor()
        sql="delete from ENFERMO where INSCRIPCION=:inc"
        cursor.execute(sql, (inscripcion,))
        registros=cursor.rowcount
        self.connection.commit()
        # Cerramos el cursor
        cursor.close()
        # No hace falta cerrar aquí la conexión 
        # Opcional el devolver el nº de registros eliminados
        return registros

