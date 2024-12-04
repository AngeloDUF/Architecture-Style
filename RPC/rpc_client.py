import xmlrpc.client

# Conectar al servidor RPC
server = xmlrpc.client.ServerProxy('http://localhost:9000')

# Llamar al método remoto
result = server.add(10, 20)
print(f"El resultado de la suma es: {result}")
