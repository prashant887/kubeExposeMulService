from flask import Flask, jsonify

app = Flask(import_name=__name__)


@app.route("/product")
def home():
    return jsonify('Calling Product Home'), 200


@app.route("/product/getproduct")
def user():
    data = {"name": "Toy", "Id": 1234, "price": 20.5}
    return jsonify(data), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
