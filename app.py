from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "UP"})

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello REST API"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
