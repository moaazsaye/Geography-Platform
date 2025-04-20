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
    app.run(debug=True)from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# إنشاء قاعدة البيانات
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# تسجيل مستخدم جديد
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data['name']
    email = data['email']
    password = data['password']

    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        conn.commit()
        conn.close()
        return jsonify({"message": "تم التسجيل بنجاح!"})
    except sqlite3.IntegrityError:
        return jsonify({"error": "البريد الإلكتروني مستخدم من قبل!"}), 400

# تسجيل الدخول
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    password = data['password']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({"message": "تم تسجيل الدخول!"})
    else:
        return jsonify({"error": "بيانات الدخول غير صحيحة!"}), 401

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
