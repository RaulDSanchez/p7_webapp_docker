# Raul Daniel Sanchez Sanchez | 2024-1755

from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

def connect_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "rootpass"),
        database=os.getenv("DB_NAME", "hola_mundo"),
        port=int(os.getenv("DB_PORT", "3306"))
    )

@app.route("/")
def home():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT 'Hola mundo desde Flask y MySQL' AS mensaje")
        row = cursor.fetchone()
        cursor.close()
        conn.close()

        return f"""
        <html>
            <head><title>Hola Mundo</title></head>
            <body>
                <h1>{row[0]}</h1>
                <p>La conexión a MySQL fue exitosa.</p>
            </body>
        </html>
        """
    except Exception as e:
        return f"""
        <html>
            <head><title>Error</title></head>
            <body>
                <h1>Hola mundo</h1>
                <p>Error al conectar con MySQL: {e}</p>
            </body>
        </html>
        """, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
