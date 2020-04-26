from Connection import Connection
from  Configuration import ConnectionStatus
import uuid

'''
Decorator for Connection information.
'''


class DefaultConnection(Connection):

    def __init__(self):
        self.connection_status = None
        self.id = uuid.uuid4()

    def open(self):
        super(DefaultConnection, self).open()
        self.connection_status = ConnectionStatus.OPEN

    def mark_connection(self):
        self.connection_status = ConnectionStatus.IN_USE

    def in_use(self):
        return self.connection_status == ConnectionStatus.IN_USE

    def unmark_connection(self):
        self.connection_status = ConnectionStatus.NOT_IN_USE

    def close(self):
        if self.connection_status != ConnectionStatus.CLOSED:
            super(DefaultConnection, self).close()
            self.connection_status = ConnectionStatus.CLOSED
            return True
        return False
