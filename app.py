from flask import Flask, jsonify
from products import products

app = Flask(__name__)

@app.route("/")
def ping():
    return jsonify({
        "msn": "It Works"
    })

@app.route("/get-products", methods=["GET"])
def get_products():
    return jsonify(products)

@app.route("/get-product-by-id/<int:id>", methods=["GET"])
def get_produc_by_id(id):
    product = [product for product in products if product["id"] == id]

    if (len(product) > 0):
        return jsonify(product[0])

    return jsonify({
        "msn": "Product with id: {id} not found!".format(id=id)
    })

if __name__ == "__main__":
    app.run(debug=True, port=3000)
