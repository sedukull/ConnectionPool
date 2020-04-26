# ConnectionPool
* Initializes the queue of connections based upon configured CONNECTION_COUNT.

* ConnectionPool is a singleton implementation which provides the following:

        get_connection() : Retrieves a connection from the available connections.
        release_connection(connection): Releases a connection to the pool.

## Usage
    from lib.ConnectionPool import ConnectionPool

    connection_pool = ConnectionPool.get_instance()

    # Get a connection.
    connection = connection_pool.get_connection()

    # Release a connection.
    connection_pool.release_connection(connection)

    ConnectionPool.metrics()
    
## Metrics:
    ConnectionPool.metrics(): It provides the list of available_connections and inuse_connections.
