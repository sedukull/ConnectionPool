from DefaultConnection import DefaultConnection
from Configuration import CONNECTION_COUNT
import queue


'''
A singleton connection pool class.
Creates the queue of connections initially.
Provides the connection from the list of available connections.
Releases the connection.
'''


class ConnectionPool(object):

    __instance = None
    available_connections = None
    available_connections_count = 0
    inuse_connections_count = 0

    @staticmethod
    def get_instance():
        """ Static access method. """
        if ConnectionPool.__instance is None:
            ConnectionPool()
        return ConnectionPool.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if ConnectionPool.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ConnectionPool.__instance = self

        # Create list of connections based upon count.
        ConnectionPool.available_connections = queue.Queue(maxsize=CONNECTION_COUNT)

        for i in range(1, CONNECTION_COUNT+1):
            ConnectionPool.available_connections.put(self.create_connection())

    def create_connection(self):
        connection = DefaultConnection()
        connection.open()
        ConnectionPool.available_connections_count = ConnectionPool.available_connections_count + 1
        return connection

    def get_connection(self):
        connection = ConnectionPool.available_connections.get(timeout=2000)
        ConnectionPool.inuse_connections_count = ConnectionPool.inuse_connections_count + 1
        connection.mark_connection()
        return connection

    def release_connection(self, default_connection):
        if default_connection.in_use():
            default_connection.unmark_connection()
            ConnectionPool.available_connections.put(default_connection)
            ConnectionPool.inuse_connections_count = ConnectionPool.inuse_connections_count - 1

    @staticmethod
    def metrics():
        print('Available Connections: {}'.format(ConnectionPool.available_connections_count))
        print('InUse Connections: {}'.format(ConnectionPool.inuse_connections_count))
