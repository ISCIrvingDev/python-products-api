from flask import Flask, jsonify, request
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

# @app.route("/get-product-by-id/<string:id>", methods=["GET"])
@app.route("/get-product-by-id/<int:id>", methods=["GET"])
def get_product_by_id(id):
    product = [product for product in products if product["id"] == id]

    if (len(product) > 0):
        return jsonify(product[0])

    return jsonify({
        "msn": "Product with id: {id} was not found!".format(id=id)
    })

@app.route("/create-product", methods=["POST"])
def create_product():
    print(request.json)

    new_product = {
        "id": request.json["id"],
        "name": request.json["name"],
        "price": request.json["price"],
        "quantity": request.json["quantity"]
    }

    products.append(new_product)

    return jsonify({
        "msn": "Product successfully saved"
    })

@app.route("/update-product-by-id/<int:id>", methods=["PUT"])
def update_product_by_id(id):
    product = [product for product in products if product["id"] == id]

    if (len(product) > 0):
        product[0]["name"] = request.json["name"]
        product[0]["price"] = request.json["price"]
        product[0]["quantity"] = request.json["quantity"]

        return jsonify({
            "msn": "Product successfully updated",
            "product": product[0]
        })

    return jsonify({
        "msn": "Product with id: {id} was not found!".format(id=id)
    })

@app.route("/delete-product-by-id/<int:id>", methods=["DELETE"])
def delete_product_by_id(id):
    product = [product for product in products if product["id"] == id]

    if (len(product) > 0):
        products.remove(product[0])

        return jsonify({
            "msn": "Product successfully deleted",
            "product": product[0]
        })

    return jsonify({
        "msn": "Product with id: {id} was not found!".format(id=id)
    })

if __name__ == "__main__":
    app.run(debug=True, port=3000)
