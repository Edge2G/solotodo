from flask import Flask, render_template
from configuraciones import *
import psycopg2


app = Flask(__name__)

conn = psycopg2.connect("dbname='%s' user='%s' password='%s'"%(database,user,passwd))
cur = conn.cursor()

@app.route('/')
def index():
    sql = """
    select nombre from productos;
    """
    cur.execute(sql)
    result = cur.fetchall()
    print(result)
    return result

if __name__ == '__main__':
    app.run(debug=True)
