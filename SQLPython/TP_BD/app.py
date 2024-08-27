from flask import Flask, request, jsonify, render_template
from new_backend import BD

app = Flask(__name__)
database = BD()

# Aplica o html do index.html na homepage do site
@app.route('/')
def index():
    return render_template('index.html')

# Rota pra criar uma tabela 
@app.route('/create_table', methods=['POST'])
def create_table():
    data = request.json
    table = data['table']
    columns = data['columns']
    database.create(table, columns)
    return jsonify({"message": "Tabela criada com sucesso"}), 201

# Rota pra inserir um registro
@app.route('/insert', methods=['POST'])
def insert():
    data = request.json
    table = data['table']
    values = data['values']
    database.insert(table, values)
    return jsonify({"message": "Registro inserido com sucesso"}), 201

# Rota pra dar SELECT
@app.route('/select', methods=['GET'])
def select():
    table = request.args.get('table')
    columns = request.args.getlist('columns')
    condition = request.args.get('condition', '1=1')  # Default condition to select all
    result = database.select(table, columns, condition)
    return jsonify(result), 200

# Rota pra atualizar valores
@app.route('/update', methods=['PUT'])
def update():
    data = request.json
    table = data['table']
    columns = data['columns']
    values = data['values']
    condition = data['condition']
    database.update(table, columns, values, condition)
    return jsonify({"message": "Registro alterado com sucesso"}), 200

@app.route('/delete', methods=['DELETE'])
def delete():
    data = request.json
    table = data['table']
    condition = data['condition']
    database.delete(table, condition)
    return jsonify({"message": "Registro removido com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True)