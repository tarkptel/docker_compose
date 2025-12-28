from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/message")
def message():
    return jsonify({"msg": "Hello This is TS.."})

app.run(host="0.0.0.0", port=5000)
