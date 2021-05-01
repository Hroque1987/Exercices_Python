def connect(**options):
    conn_params = {
        'host': options.get('host', '127.0.0.1'),
        'port': options.get('port', 5432),
        'user': options.get('user', 'default'),
        'pwd': options.get('pwd', 'default')
        }
    print(conn_params)

    # we then connect to the db (commented out)
    # db.connect(**conn_params)

connect()
connect(host='127.0.0.42', port=5433)
connect(port=5431, user='fab', pwd='gandalf')
'''Note in the function we can prepare a dictionary of connection parameters
(conn_params) in the function using default values as fallback, allowing them to
be overwritten if they are provided in the function call.'''
