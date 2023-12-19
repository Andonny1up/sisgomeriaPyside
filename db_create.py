import sqlite3
from sqlite3 import Error
from helpers import absPath

def crear_conexion(db_file):
    """ Crear una conexión de base de datos a una base de datos SQLite """
    conexion = None
    try:
        conexion = sqlite3.connect(db_file)
        print(f"Conexión exitosa a SQLite con sqlite3 versión: {sqlite3.version}")
    except Error as e:
        print(e)

    return conexion

def crear_tabla(conexion, crear_tabla_sql):
    """ Crear una tabla desde el crear_tabla_sql statement """
    try:
        c = conexion.cursor()
        c.execute(crear_tabla_sql)
    except Error as e:
        print(e)

def main():
    database = absPath("gomeria.db")

    sql_crear_tabla_clientes = """ CREATE TABLE IF NOT EXISTS clientes (
                                        id integer PRIMARY KEY,
                                        nombre text NOT NULL,
                                        ci text,
                                        telefono text
                                    ); """
    
    sql_crear_tabla_productos = """ CREATE TABLE IF NOT EXISTS productos (
                                        id integer PRIMARY KEY,
                                        descripcion text NOT NULL,
                                        marca text,
                                        precio REAL
                                    ); """
    
    sql_crear_tabla_servicios = """ CREATE TABLE IF NOT EXISTS servicios (
                                    id integer PRIMARY KEY,
                                    id_cliente integer NOT NULL,
                                    vehiculo text,
                                    descripcion text,
                                    precio REAL,
                                    precio_total REAL,
                                    pagado BOOLEAN DEFAULT FALSE,
                                    FOREIGN KEY (id_cliente) REFERENCES clientes (id)
                                ); """

    sql_crear_tabla_productos_servicio = """ CREATE TABLE IF NOT EXISTS productos_servicio (
                                            id integer PRIMARY KEY,
                                            id_servicio integer NOT NULL,
                                            id_producto integer NOT NULL,
                                            cantidad integer NOT NULL,
                                            precio REAL,
                                            FOREIGN KEY (id_servicio) REFERENCES servicios (id),
                                            FOREIGN KEY (id_producto) REFERENCES productos (id)
                                        ); """
    # crear una conexión de base de datos
    conexion = crear_conexion(database)

    # crear tablas
    if conexion is not None:
        # crear tabla clientes
        crear_tabla(conexion, sql_crear_tabla_clientes)
        # crear tabla productos
        crear_tabla(conexion, sql_crear_tabla_productos)
        # crear tabla servicios
        crear_tabla(conexion, sql_crear_tabla_servicios)
        # crear tabla productos_servicio
        crear_tabla(conexion, sql_crear_tabla_productos_servicio)
    else:
        print("Error! No se pudo conectar a la base de datos.")

if __name__ == '__main__':
    main()