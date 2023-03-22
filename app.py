from flask import Flask, jsonify, request

app=Flask(__name__)

from products import products

@app.route('/ping')
def ping():
    return jsonify({"mensaje":"este es un objeto json"})

@app.route('/products')
def getProducts():
    return jsonify({"products":products, "mensaje":"products list"})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if(len(productFound) > 0):
        return jsonify({"product":productFound[0]})
    return jsonify({"Mensaje":"ERROR AL INDTRODUCIR PRODUCTO"})

@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"messager":"product added Succesfully", "products":products})

@app.route('/products/<string:product_name>',methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name']==product_name]
    if (len (productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "messege": "Product Update",
            "product": productFound[0]
            })
    return jsonify({"messege":"Product Not Found"})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deletProduct(product_name):
    productFound=[product for product in products if product['name'] == product_name]
    if len(productFound) > 0:
        products.remove(productFound[0])
        return jsonify({
            "messege": "product delete",
            "products": products
        })
    return jsonify({"messege": "Product Not Found"})
        

if __name__ == "__main__":
    app.run(debug=True, port=4000)