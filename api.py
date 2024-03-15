from flask import Flask, request, jsonify
from dml import DML

app = Flask(__name__)
dml = DML('localhost', 'root', '12345678', 'taller_vistas')  # Create a single DML instance

@app.route('/api/<name>')
def proveedor(name):
    if name == 'proveedor':
        dml.conectar()
        result = dml.consultar('SELECT * FROM proveedor')
        dml.cerrar()  # Close connection after query
        return jsonify(result)
    else:
        return 'Hola ' + name

@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()  # Use get_json() for JSON data
    dml.conectar()
    dml.crear(data['table'], data['columns'], data['values'])
    dml.cerrar()
    return jsonify({"message": "Record created successfully"})

@app.route('/read', methods=['GET'])
def read():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Missing query parameter"})
    dml.conectar()
    result = dml.consultar(query)
    dml.cerrar()
    return jsonify(result)

@app.route('/update', methods=['PUT'])
def update():
    data = request.get_json()
    dml.conectar()
    dml.actualizar(data['table'], data['columns'], data['values'], data['condition'])
    dml.cerrar()
    return jsonify({"message": "Record updated successfully"})

@app.route('/delete', methods=['DELETE'])
def delete():
    data = request.get_json()
    dml.conectar()
    dml.eliminar(data['table'], data['condition'])
    dml.cerrar()
    return jsonify({"message": "Record deleted successfully"})


@app.route('/close', methods=['GET'])
def close():
    dml.cerrar()
    return jsonify({"message": "Connection closed"})

if __name__ == '__main__':
    app.run(debug=True)
