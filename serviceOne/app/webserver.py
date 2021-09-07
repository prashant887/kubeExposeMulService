from flask import Flask, jsonify

app = Flask(import_name=__name__)


@app.route("/user")
def home():
    return jsonify('Calling User Home'), 200


@app.route("/user/getuser")
def user():
    data = {"name": "John", "Id": 1234, "loc": "usa"}
    return jsonify(data), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
