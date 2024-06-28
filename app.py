from flask import Flask, request, jsonify

app = Flask(__name__)

# Datos de ejemplo para almacenar la IP
stored_ip = None

# Ruta para recibir y almacenar la IP mediante POST
@app.route('/ip', methods=['POST'])
def receive_ip():
    global stored_ip
    data = request.get_json()
    if 'ip' in data:
        stored_ip = data['ip']
        return jsonify({'message': 'IP almacenada correctamente'}), 200
    else:
        return jsonify({'error': 'Se requiere el parámetro "ip"'}), 400

# Ruta para obtener la IP almacenada mediante GET
@app.route('/ip', methods=['GET'])
def get_ip():
    global stored_ip
    if stored_ip:
        return jsonify({'ip': stored_ip}), 200
    else:
        return jsonify({'message': 'No hay IP almacenada'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)

