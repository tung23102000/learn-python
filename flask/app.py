from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

stores=[
    {
        'name': 'MTP Store',
        'items':[
            {
                'name': 'My team',
                 'price': 15.99
            }
        ]
    }
]

#post /store data: {name:}
@app.route('/store', methods=['GET', 'POST'])
def create_store():
    request_data= request.get_json()
    new_store ={
        'name': request_data['name'],
         'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

#get /store/<string:name>
@app.route('/store/<string:name>')  #http://127.0.0.1:5000/store/some_name
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


#get /store
@app.route('/stores')
def get_stores():
  return jsonify({'stores':stores})

#post /store/<string:name>/item {name: , price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_store = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_store)
            return jsonify(new_store)
    return jsonify({'message': 'store not found'})

#get /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] ==name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})
app.run(port=5000)