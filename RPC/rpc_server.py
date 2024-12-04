from xmlrpc.server import SimpleXMLRPCServer

# Función que el servidor va a exponer
def add(x, y):
    return x + y

# Configurar el servidor RPC
server = SimpleXMLRPCServer(('localhost', 9000))
server.register_function(add, 'add')

# Ejecutar el servidor
print("Servidor RPC corriendo en el puerto 9000...")
server.serve_forever()
