from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def hello():
    return jsonify(message="Hola Mundo desde Flask + Docker + CI/CD!")

if __name__ == "__main__":
    # Para correr localmente: python app/app.py
    # Render usará gunicorn (ver Dockerfile)
    app.run(host="0.0.0.0", port=8080)
