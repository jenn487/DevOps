from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Un saludo desde mi app Hola Mundo!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
