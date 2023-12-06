import psycopg2
from psycopg2 import pool
import os

class DatabaseConnection:
    def __init__(self):
        self.connection_pool = None

    def initialize_connection_pool(self, minconn=1, maxconn=10):
        """
        Inicializa un pool de conexiones a la base de datos.

        Args:
            minconn (int): Número mínimo de conexiones permitidas.
            maxconn (int): Número máximo de conexiones permitidas.
        """
        try:
            self.connection_pool = psycopg2.pool.SimpleConnectionPool(
                minconn,
                maxconn,
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                database=os.getenv("DB_NAME")
            )
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error al conectar con la base de datos PostgreSQL", error)
            raise

    def get_connection(self):
        """
        Obtiene una conexión del pool de conexiones.

        Returns:
            connection: Una conexión a la base de datos.
        """
        return self.connection_pool.getconn()

    def put_connection_back(self, connection):
        """
        Devuelve una conexión al pool.

        Args:
            connection: Conexión a devolver al pool.
        """
        self.connection_pool.putconn(connection)

    def close_all_connections(self):
        """
        Cierra todas las conexiones del pool.
        """
        self.connection_pool.closeall()

# Ejemplo de uso
# db = DatabaseConnection()
# db.initialize_connection_pool()
# conn = db.get_connection()
# # Realiza operaciones con la base de datos...
# db.put_connection_back(conn)
# db.close_all_connections()
