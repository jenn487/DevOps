from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        conn = mysql.connector.connect(
            host='db',
            user='user',
            password='userpass',
            database='testdb'
        )
        cursor = conn.cursor()
        cursor.execute('SELECT DATABASE();')
        db_name = cursor.fetchone()
        return f"Hola Mundo desde Flask 🚀 con BD: {db_name[0]}"
    except Exception as e:
        return f"Error al conectar con la base de datos: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
