from flask import Flask, request, jsonify

app = Flask(__name__)

# Define el endpoint del webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    print(f"Headers: {request.headers}")
    print(f"Body: {request.get_data(as_text=True)}")
    data = request.get_json()  # Obtiene el cuerpo del POST en formato JSON
    print(f"Datos recibidos: {data}")  # Imprime los datos para depuración
    return jsonify({"message": "Hola Mundo, webhook recibido correctamente!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
