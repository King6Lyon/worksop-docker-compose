import os
import psycopg2 # type: ignore
from flask import Flask # type: ignore
app = Flask(__name__)
DATABASE_URL = os.environ.get("DATABASE_URL","postgresql://user:password@db:5432//demo")

@app.route('/')
def hello():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("SELECT name FROM users;")
    rows = cur.fetchall()

    user_list = "".join(f"<li>{row[0]}</li>" for row in rows)
    html = f"""
    <html>
        <head><tittle>Données de la DB</title><head/>
        <body>
            <h1>Liste des utilisateurs:</h1>
            <ul>
                {user_list}
            </ul>
        </body>
    </html>
    """

    cur.close()
    conn.close()
    return html
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
