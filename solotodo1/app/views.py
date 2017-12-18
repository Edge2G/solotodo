
from app import app
from datetime import datetime
from flask import render_template,request,redirect
from configuraciones import *
import psycopg2

conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,passwd))
cur = conn.cursor()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='home')

@app.route('/index/hdd')
def hdd():

    return render_template('hdd.html',title='hdd')

@app.route('/index/mobo', methods = ["POST" , "GET"])
def mobo():
    sql = """
    select * from productos where categoria_id = 2;
    """
    cur.execute(sql)
    asd = cur.fetchall()

    return render_template('mobo.html',title='mobo', asd = asd)

@app.route('/index/cpu')
def cpu():
    return render_template('cpu.html',title='cpu')

@app.route('/index/gpu')
def gpu():
    return render_template('gpu.html',title='gpu')

@app.route('/index/ram')
def ram():
    return render_template('ram.html',title='ram')

@app.route('/index/manage')
def manage():
    return render_template('add_rm.html',title='manage')