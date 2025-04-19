from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "مرحبًا بكم في منصة الجغرافي معاذ السيد!"})

if __name__ == "__main__":
    app.run(debug=True)
