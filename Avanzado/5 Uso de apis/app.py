from flask import Flask, jsonify, request

productos = [
    {'name': "laptop" , "price": 800 ,"quantity":4},
    {'name': "mouse" , "price": 40 ,"quantity":8},
    {'name': "monitor" , "price": 200 ,"quantity":1}
]
app = Flask(__name__)
@app.route('/products',methods=['GET'])
def getProducts():
    return jsonify(productos)
@app.route('/products/<string:product_name>')
def getProduct(product_name):
    for dicionario in productos:
        if dicionario['name'] ==  product_name:
            return dicionario
@app.route('/products',methods=['POST'])
def addProduct():
    #print(request.json)
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity":request.json['quantity']
    }
    productos.append(new_product)
    return "Recibido"

if __name__ == '__main__':
    app.run(debug= True, port=5000)







