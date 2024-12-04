from flask import Flask, jsonify

app = Flask(__name__)

# Definir el endpoint de la API REST
@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hola Mundo desde la API REST!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
