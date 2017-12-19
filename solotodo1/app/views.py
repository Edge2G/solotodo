
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
    if request.method == 'POST':
        nomm = request.form['buscar_hdd_nombre']
        print (nomm)
        sql = """
        select productos.nombre, especificacion, productos_detalle.detalle
        from productos, productos_detalle, especificaciones
        where productos.id = productos_detalle.producto_id
        and productos.categoria_id = '1'
        and productos_detalle.especificacion_id = especificaciones.id
        and lower(productos.nombre) like lower('%""" + nomm +"""%')
        order by productos.nombre
        ;"""
        cur.execute(sql)
        data = cur.fetchall()
        prod = []
        temp = ''
        for x in data:
            if x[0] != temp:
                prod.append(x[0])
            temp = x[0]
        data2=[]
        for x in prod:
            sql = """
            select tiendas.nombre, precios.precio, productos.nombre
            from precios, tiendas, productos
            where productos.id = precios.producto_id
            and tiendas.id = precios.tienda_id
            and lower(productos.nombre) like lower('%""" + x +"""%')
            ;"""
            cur.execute(sql)
            data2.append(cur.fetchall())
        return render_template('hdd.html',title='hdd', data = data, data2 = data2, nomm = nomm)
    return render_template('hdd.html',title='hdd')

@app.route('/index/mobo', methods = ['POST' , 'GET'])
def mobo():
    if request.method == 'POST':
        nomm = request.form['buscar_mobo_nombre']
        print (nomm)
        sql = """
        select productos.nombre, especificacion, productos_detalle.detalle
        from productos, productos_detalle, especificaciones
        where productos.id = productos_detalle.producto_id
        and productos.categoria_id = '2'
        and productos_detalle.especificacion_id = especificaciones.id
        and lower(productos.nombre) like lower('%""" + nomm +"""%');"""
        cur.execute(sql)
        data = cur.fetchall()
        prod = []
        temp = ''
        for x in data:
            if x[0] != temp:
                prod.append(x[0])
            temp = x[0]
        data2=[]
        for x in prod:
            sql = """
            select tiendas.nombre, precios.precio, productos.nombre
            from precios, tiendas, productos
            where productos.id = precios.producto_id
            and tiendas.id = precios.tienda_id
            and lower(productos.nombre) like lower('%""" + x +"""%')
            ;"""
            cur.execute(sql)
            data2.append(cur.fetchall())
        return render_template('mobo.html',title='mobo', data = data, data2 = data2, nomm = nomm)
    return render_template('mobo.html', title='mobo')

@app.route('/index/cpu', methods = ['POST' , 'GET'])
def cpu():
    if request.method == 'POST':
        nomm = request.form['buscar_cpu_nombre']
        print (nomm)
        sql = """
        select productos.nombre, especificacion, productos_detalle.detalle
        from productos, productos_detalle, especificaciones
        where productos.id = productos_detalle.producto_id
        and productos.categoria_id = '4'
        and productos_detalle.especificacion_id = especificaciones.id
        and lower(productos.nombre) like lower('%""" + nomm +"""%');"""
        cur.execute(sql)
        data = cur.fetchall()
        prod = []
        temp = ''
        for x in data:
            if x[0] != temp:
                prod.append(x[0])
            temp = x[0]
        data2=[]
        for x in prod:
            sql = """
            select tiendas.nombre, precios.precio, productos.nombre
            from precios, tiendas, productos
            where productos.id = precios.producto_id
            and tiendas.id = precios.tienda_id
            and lower(productos.nombre) like lower('%""" + x +"""%')
            ;"""
            cur.execute(sql)
            data2.append(cur.fetchall())
        return render_template('cpu.html',title='cpu', data = data, data2 = data2, nomm = nomm)
    return render_template('cpu.html',title='cpu')

@app.route('/index/gpu', methods = ['POST' , 'GET'])
def gpu():
    if request.method == 'POST':
        nomm = request.form['buscar_gpu_nombre']
        print (nomm)
        sql = """
        select productos.nombre, especificacion, productos_detalle.detalle
        from productos, productos_detalle, especificaciones
        where productos.id = productos_detalle.producto_id
        and productos.categoria_id = '3'
        and productos_detalle.especificacion_id = especificaciones.id
        and lower(productos.nombre) like lower('%""" + nomm +"""%');"""
        cur.execute(sql)
        data = cur.fetchall()
        prod = []
        temp = ''
        for x in data:
            if x[0] != temp:
                prod.append(x[0])
            temp = x[0]
        data2=[]
        for x in prod:
            sql = """
            select tiendas.nombre, precios.precio, productos.nombre
            from precios, tiendas, productos
            where productos.id = precios.producto_id
            and tiendas.id = precios.tienda_id
            and lower(productos.nombre) like lower('%""" + x +"""%')
            ;"""
            cur.execute(sql)
            data2.append(cur.fetchall())
        return render_template('gpu.html',title='gpu', data = data, data2 = data2, nomm = nomm)
    return render_template('gpu.html',title='gpu')

@app.route('/index/ram', methods = ['POST' , 'GET'])
def ram():
    if request.method == 'POST':
        nomm = request.form['buscar_ram_nombre']
        print (nomm)
        sql = """
        select productos.nombre, especificacion, productos_detalle.detalle
        from productos, productos_detalle, especificaciones
        where productos.id = productos_detalle.producto_id
        and productos.categoria_id = '5'
        and productos_detalle.especificacion_id = especificaciones.id
        and lower(productos.nombre) like lower('%""" + nomm +"""%');"""
        cur.execute(sql)
        data = cur.fetchall()
        prod = []
        temp = ''
        for x in data:
            if x[0] != temp:
                prod.append(x[0])
            temp = x[0]
        data2=[]
        for x in prod:
            sql = """
            select tiendas.nombre, precios.precio, productos.nombre
            from precios, tiendas, productos
            where productos.id = precios.producto_id
            and tiendas.id = precios.tienda_id
            and lower(productos.nombre) like lower('%""" + x +"""%')
            ;"""
            cur.execute(sql)
            data2.append(cur.fetchall())
        return render_template('ram.html',title='ram', data = data, data2 = data2, nomm = nomm)
    return render_template('ram.html',title='ram')

@app.route('/index/add', methods = ['POST' , 'GET'])
def add():
    return render_template('add.html',title='Agregar')

@app.route('/index/delete', methods = ['POST' , 'GET'])
def delete():
    return render_template('delete.html',title='Eliminar')
