
    
import oracledb
class OracleEmpleados:
    def __init__(self):
        self.connection=oracledb.connect(
            user="System", password="oracle",
            dsn="localhost/FREEPDB1")
    def eliminarEmpleados(self,id):
        cursor=self.connection.cursor()
        sql="delete from EMP where EMP_NO=:id"
        cursor.execute(sql, (id,))
        registros=cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros
        
