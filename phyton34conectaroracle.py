import oracledb
print ("Conectando Oracle")
# Tenemos un objeto connection que nos pedirá
# (user, password, system)
connetion=oracledb.connect(user="SYSTEM"
                           , password="oracle"
                           , dsn="localhost/FREEPDB1")
print("Estamos conectados!!!")
cursor=connetion.cursor()
cursor.execute(SQL)
