from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "Hola desde mi API en la nube (v1)"}), 200


@app.route("/status", methods=["GET"])
def status():
    return jsonify({
        "status": "ok",
        "version": "v1",
        "time": datetime.datetime.utcnow().isoformat() + "Z"
    }), 200


@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json(silent=True) or {}
    return jsonify({
        "received": data
    }), 200


if __name__ == "__main__":
    # Esto es solo para pruebas locales
    app.run(host="0.0.0.0", port=5001)
