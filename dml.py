import pymysql


class DML:
    result = []

    def __init__(self, host, user, passwd, db):
        self.__host = host
        self.__user = user
        self.__passwd = passwd
        self.__db = db

    def conectar(self):
        self.db = pymysql.connect(host=self.__host, user=self.__user, password=self.__passwd, db=self.__db)
        self.cursor = self.db.cursor()

    def crear(self, table, columns, values):
        query = "INSERT INTO {} ({}) VALUES ({})".format(table, ', '.join(columns), ', '.join(map(str, values)))
        self.cursor.execute(query)
        self.db.commit()

    def consultar(self, query):
        self.cursor.execute(query)
        self.result = self.cursor.fetchall()

    def actualizar(self, table, columns, values, condition):
        set_values = ', '.join(['{}={}'.format(col, val) for col, val in zip(columns, values)])
        query = "UPDATE {} SET {} WHERE {}".format(table, set_values, condition)
        self.cursor.execute(query)
        self.db.commit()

    def eliminar(self, table, condition):
        query = "DELETE FROM {} WHERE {}".format(table, condition)
        self.cursor.execute(query)
        self.db.commit()

    def cerrar(self):
        self.db.close()

# Example usage:
# dml = DML('localhost', 'root', '12345678', 'taller_vistas')
#
# # Consult all rows from the "personas" table
# dml.consultar("SELECT * FROM personas")
#
# # Create a new row in the "personas" table
# nombre = "Juan"
# edad = 30
# dml.crear("personas", ["nombre", "edad"], [nombre, edad])
#
# # Update the row with ID 1 in the "personas" table
# id = 1
# nombre_nuevo = "Juan Pablo"
# edad_nueva = 35
# dml.actualizar("personas", ["nombre", "edad"], [nombre_nuevo, edad_nueva], "id={}".format(id))
#
# # Delete the row with ID 2 in the "personas" table
# id = 2
# dml.eliminar("personas", "id={}".format(id))
#
# # Close the database connection
# dml.cerrar()