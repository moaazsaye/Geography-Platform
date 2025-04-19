from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "مرحباً بكم في الـ Backend الخاص بمنصة الجغرافي معاذ السيد!"

if __name__ == '__main__':
    app.run(debug=True)
