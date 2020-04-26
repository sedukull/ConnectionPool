"""
Usage of simple connection pool class
"""

from lib.ConnectionPool import ConnectionPool

if "__name__" != "__main__":

    connection_pool = ConnectionPool.get_instance()

    # Get a connection.
    connection = connection_pool.get_connection()

    # Release a connection.
    connection_pool.release_connection(connection)

    ConnectionPool.metrics()
