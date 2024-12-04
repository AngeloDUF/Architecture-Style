from zeep import Client

# Conectar al servicio SOAP
wsdl = 'http://localhost:8000/?wsdl'
client = Client(wsdl)

# Invocar métodos del servicio
result_add = client.service.add(10, 5)
result_subtract = client.service.subtract(10, 5)

print(f"Resultado de 10 + 5: {result_add}")
print(f"Resultado de 10 - 5: {result_subtract}")
