
from app import app
from datetime import datetime
from flask import render_template,request,redirect
from .configuraciones import *
import psycopg2

conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,passwd))
cur = conn.cursor()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title='home')

@app.route('/index/hdd', methods = ['POST' , 'GET'])
def hdd():
    return render_template('hdd.html',title='hdd')

@app.route('/index/mobo', methods = ['POST' , 'GET'])
def mobo():
    if request.method == 'POST':
        nomm = request.form['buscar_mobo_nombre']
        print (nomm)
        '''
        sql = """
        select * from productos where categoria_id =
        """ + nomm + """;"""
        '''
        sql = """
        select productos.nombre, especificacion, productos_detalle.detalle
        from productos, productos_detalle, especificaciones
        where productos.id = productos_detalle.producto_id
        and productos_detalle.especificacion_id = especificaciones.id
        and lower(productos.nombre) like lower('%""" + nomm +"""%');"""
        cur.execute(sql)
        asd = cur.fetchall()
        return render_template('mobo.html',title='mobo', asd = asd, nomm = nomm)
    return render_template('mobo.html', title='mobo')

@app.route('/index/cpu', methods = ['POST' , 'GET'])
def cpu():
    return render_template('cpu.html',title='cpu')

@app.route('/index/gpu', methods = ['POST' , 'GET'])
def gpu():
    return render_template('gpu.html',title='gpu')

@app.route('/index/ram', methods = ['POST' , 'GET'])
def ram():
    return render_template('ram.html',title='ram')

@app.route('/index/manage', methods = ['POST' , 'GET'])
def manage():
    return render_template('add_rm.html',title='manage')


'''
    cur.execute(sql)
    asd = cur.fetchall()
'''
