from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My Online Beauty Store',
        'items': [
            {'name': 'Mascara',
             'price': 15.99}
        ]
    }]


# POST used to receive data
# GET used to send data back to browser.

# POST/store  data:{name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# POST /store/<string:name>/item{name:,price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'Store not found'})


# GET/store/<string:name>/item{name:,price:}
@app.route('/store/<string:name>/item', methods=['GET'])
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message': 'Store not found'})


app.run()
