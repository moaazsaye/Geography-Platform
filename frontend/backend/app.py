from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def connect_db():
    return sqlite3.connect("platform.db")

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        conn.commit()
        response = {"message": "تم تسجيل المستخدم بنجاح"}
    except sqlite3.IntegrityError:
        response = {"message": "البريد الإلكتروني مستخدم بالفعل"}
    conn.close()
    return jsonify(response)

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({"message": "تم تسجيل الدخول بنجاح"})
    else:
        return jsonify({"message": "بيانات غير صحيحة"})

if __name__ == "__main__":
    app.run(debug=True)from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def connect_db():
    return sqlite3.connect("platform.db")

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        conn.commit()
        response = {"message": "تم تسجيل المستخدم بنجاح"}
    except sqlite3.IntegrityError:
        response = {"message": "البريد الإلكتروني مستخدم بالفعل"}
    conn.close()
    return jsonify(response)

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({"message": "تم تسجيل الدخول بنجاح"})
    else:
        return jsonify({"message": "بيانات غير صحيحة"})

if __name__ == "__main__":
    app.run(debug=True)
