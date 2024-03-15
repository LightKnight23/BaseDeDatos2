from dml import DML
if __name__ == '__main__':

    instancia = DML('localhost', 'root', '12345678', 'taller_vistas')
    instancia.conectar()
    instancia.consultar("SELECT * FROM proveedor")
    instancia.imprimir()

