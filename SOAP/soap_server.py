from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class CalculatorService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add(ctx, x, y):
        return x + y

    @rpc(Integer, Integer, _returns=Integer)
    def subtract(ctx, x, y):
        return x - y

# Definir el servicio y la aplicación
application = Application(
    [CalculatorService],
    'calculator.soap.example',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

# Crear el servidor
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('localhost', 8000, WsgiApplication(application))
    print("Servidor SOAP corriendo en http://localhost:8000")
    server.serve_forever()
