
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
    return render_template('index.html',title='home')

@app.route('/index/hdd', methods = ['POST' , 'GET'])
def hdd():
    if request.method == 'POST':
        nomm = request.form['buscar_hdd_nombre']
        #print (nomm)
        sql = """
        select productos.nombre, especificacion, productos_detalle.detalle, marcas.nombre
        from productos, productos_detalle, especificaciones, marcas
        where productos.id = productos_detalle.producto_id
        and productos.categoria_id = '1'
        and productos_detalle.especificacion_id = especificaciones.id
        and productos.marca_id = marcas.id
        and lower(productos.nombre) like lower('%""" + nomm +"""%')
        order by productos.nombre, especificacion, productos_detalle.detalle;
        """
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
            and lower(productos.nombre) like lower('%""" + x +"""%');
            """
            cur.execute(sql)
            data2.append(cur.fetchall())
            #print(data2)
        return render_template('hdd.html',title='hdd', data = data, data2 = data2, nomm = nomm)
    return render_template('hdd.html',title='hdd')

@app.route('/index/mobo', methods = ['POST' , 'GET'])
def mobo():
    if request.method == 'POST':
        nomm = request.form['buscar_mobo_nombre']
        #print (nomm)
        sql = """
        select productos.nombre, especificacion, productos_detalle.detalle, marcas.nombre
        from productos, productos_detalle, especificaciones, marcas
        where productos.id = productos_detalle.producto_id
        and productos.categoria_id = '2'
        and productos_detalle.especificacion_id = especificaciones.id
        and productos.marca_id = marcas.id
        and lower(productos.nombre) like lower('%""" + nomm +"""%')
        order by productos.nombre, especificacion, productos_detalle.detalle;
        """
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
            and lower(productos.nombre) like lower('%""" + x +"""%');
            """
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
        select productos.nombre, especificacion, productos_detalle.detalle, marcas.nombre
        from productos, productos_detalle, especificaciones, marcas
        where productos.id = productos_detalle.producto_id
        and productos.categoria_id = '4'
        and productos_detalle.especificacion_id = especificaciones.id
        and productos.marca_id = marcas.id
        and lower(productos.nombre) like lower('%""" + nomm +"""%')
        order by productos.nombre, especificacion, productos_detalle.detalle;
        """
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
            and lower(productos.nombre) like lower('%""" + x +"""%');
            """
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
        select productos.nombre, especificacion, productos_detalle.detalle, marcas.nombre
        from productos, productos_detalle, especificaciones, marcas
        where productos.id = productos_detalle.producto_id
        and productos.categoria_id = '3'
        and productos_detalle.especificacion_id = especificaciones.id
        and productos.marca_id = marcas.id
        and lower(productos.nombre) like lower('%""" + nomm +"""%')
        order by productos.nombre, especificacion, productos_detalle.detalle;
        """
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
            and lower(productos.nombre) like lower('%""" + x +"""%');
            """
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
        select productos.nombre, especificacion, productos_detalle.detalle, marcas.nombre
        from productos, productos_detalle, especificaciones, marcas
        where productos.id = productos_detalle.producto_id
        and productos.categoria_id = '5'
        and productos_detalle.especificacion_id = especificaciones.id
        and productos.marca_id = marcas.id
        and lower(productos.nombre) like lower('%""" + nomm +"""%')
        order by productos.nombre, especificacion, productos_detalle.detalle;
        """
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
            and lower(productos.nombre) like lower('%""" + x +"""%');
            """
            cur.execute(sql)
            data2.append(cur.fetchall())
        return render_template('ram.html',title='ram', data = data, data2 = data2, nomm = nomm)
    return render_template('ram.html',title='ram')

@app.route('/index/add_hdd', methods = ['POST' , 'GET'])
def add_hdd():
    if request.method == 'POST':
        nombre=request.form['nuevo_hdd']
        precio=request.form['precio']
        tienda=request.form['tienda']

        tamano=request.form['tamano']
        rpm=request.form['RPM']
        cap=request.form['capacidad']
        buf=request.form['bufer']
        marca=request.form['marca']

        sql = """
        select max(id)+1 as maximo from productos;
        """
        cur.execute(sql)
        new_id = cur.fetchall()

        sql = """
        select id from marcas where nombre = '"""+marca+"""';
        """
        cur.execute(sql)
        marca_id = cur.fetchall()

        new_id = str(new_id[0][0])
        marca_id = str(marca_id[0][0])

        sql= """
        INSERT INTO productos VALUES("""+new_id+""",'"""+nombre+"""',"""+marca_id+""",1);
        """
        print(sql)
        cur.execute(sql)
        conn.commit()

        sql="""
        insert into productos_detalle values("""+new_id+""",1,'"""+tamano+"""');
        """
        cur.execute(sql)
        conn.commit()

        sql="""
        insert into productos_detalle values("""+new_id+""",2,'"""+rpm+"""');
        """
        cur.execute(sql)
        conn.commit()

        sql="""
        insert into productos_detalle values("""+new_id+""",3,'"""+cap+"""');
        """
        cur.execute(sql)
        conn.commit()

        sql="""
        insert into productos_detalle values("""+new_id+""",4,'"""+buf+"""');
        """
        cur.execute(sql)
        conn.commit()

        sql = """
        select * from tiendas;
        """
        cur.execute(sql)
        tablatiendas = cur.fetchall()
        tienda_id = 0
        for x in tablatiendas:
            if tienda == x[1]:
                tienda_id = x[0]

        tienda_id = str(tienda_id)
        sql = """
        INSERT INTO precios VALUES("""+new_id+""", """+tienda_id+""", """+precio+""");
        """
        cur.execute(sql)
        conn.commit()

    return render_template('add_hdd.html',title='Agregar')

@app.route('/index/add_mobo', methods = ['POST' , 'GET'])
def add_mobo():
    if request.method == 'POST':
        nombre=request.form['nuevo_mobo']
        precio=request.form['precio']
        tienda=request.form['tienda']

        socket=request.form['socket']
        formato=request.form['formato']
        marca=request.form['marca']

        sql = """
        select max(id)+1 as maximo from productos;
        """
        cur.execute(sql)
        new_id = cur.fetchall()

        sql = """
        select id from marcas where nombre = '"""+marca+"""';
        """
        cur.execute(sql)
        marca_id = cur.fetchall()

        new_id = str(new_id[0][0])
        marca_id = str(marca_id[0][0])

        sql= """
        INSERT INTO productos VALUES("""+new_id+""",'"""+nombre+"""',"""+marca_id+""",2);
        """
        print(sql)
        cur.execute(sql)
        conn.commit()

        sql="""
        insert into productos_detalle values("""+new_id+""",6,'"""+socket+"""');
        """
        cur.execute(sql)
        conn.commit()

        sql="""
        insert into productos_detalle values("""+new_id+""",9,'"""+formato+"""');
        """
        cur.execute(sql)
        conn.commit()


        sql = """
        select * from tiendas;
        """
        cur.execute(sql)
        tablatiendas = cur.fetchall()
        tienda_id = 0
        for x in tablatiendas:
            if tienda == x[1]:
                tienda_id = x[0]

        tienda_id = str(tienda_id)
        sql = """
        INSERT INTO precios VALUES("""+new_id+""", """+tienda_id+""", """+precio+""");
        """
        cur.execute(sql)
        conn.commit()

    return render_template('add_mobo.html',title='Agregar')

@app.route('/index/add_cpu', methods = ['POST' , 'GET'])
def add_cpu():
    if request.method == 'POST':
        nombre=request.form['nuevo_cpu']
        precio=request.form['precio']
        tienda=request.form['tienda']

        cores=request.form['cores']
        socket=request.form['socket']
        marca=request.form['marca']

        sql = """
        select max(id)+1 as maximo from productos;
        """
        cur.execute(sql)
        new_id = cur.fetchall()

        sql = """
        select id from marcas where nombre = '"""+marca+"""';
        """
        cur.execute(sql)
        marca_id = cur.fetchall()

        new_id = str(new_id[0][0])
        marca_id = str(marca_id[0][0])

        sql= """
        INSERT INTO productos VALUES("""+new_id+""",'"""+nombre+"""',"""+marca_id+""",4);
        """
        print(sql)
        cur.execute(sql)
        conn.commit()

        sql="""
        insert into productos_detalle values("""+new_id+""",5,'"""+cores+"""');
        """
        cur.execute(sql)
        conn.commit()

        sql="""
        insert into productos_detalle values("""+new_id+""",6,'"""+socket+"""');
        """
        cur.execute(sql)
        conn.commit()

        sql = """
        select * from tiendas;
        """
        cur.execute(sql)
        tablatiendas = cur.fetchall()
        tienda_id = 0
        for x in tablatiendas:
            if tienda == x[1]:
                tienda_id = x[0]

        tienda_id = str(tienda_id)
        sql = """
        INSERT INTO precios VALUES("""+new_id+""", """+tienda_id+""", """+precio+""");
        """
        cur.execute(sql)
        conn.commit()

    return render_template('add_cpu.html',title='Agregar')

@app.route('/index/add_gpu', methods = ['POST' , 'GET'])
def add_gpu():
    if request.method == 'POST':
        nombre=request.form['nuevo_gpu']
        precio=request.form['precio']
        tienda=request.form['tienda']

        tamano=request.form['tamano']
        memoria=request.form['memoria']
        frecuencia=request.form['frecuencia']
        marca=request.form['marca']

        sql = """
        select max(id)+1 as maximo from productos;
        """
        cur.execute(sql)
        new_id = cur.fetchall()

        sql = """
        select id from marcas where nombre = '"""+marca+"""';
        """
        cur.execute(sql)
        marca_id = cur.fetchall()

        new_id = str(new_id[0][0])
        marca_id = str(marca_id[0][0])

        sql= """
        INSERT INTO productos VALUES("""+new_id+""",'"""+nombre+"""',"""+marca_id+""",3);
        """
        print(sql)
        cur.execute(sql)
        conn.commit()

        sql="""
        insert into productos_detalle values("""+new_id+""",1,'"""+tamano+"""');
        """
        cur.execute(sql)
        conn.commit()

        sql="""
        insert into productos_detalle values("""+new_id+""",7,'"""+memoria+"""');
        """
        cur.execute(sql)
        conn.commit()

        sql="""
        insert into productos_detalle values("""+new_id+""",8,'"""+frecuencia+"""');
        """
        cur.execute(sql)
        conn.commit()

        sql = """
        select * from tiendas;
        """
        cur.execute(sql)
        tablatiendas = cur.fetchall()
        tienda_id = 0
        for x in tablatiendas:
            if tienda == x[1]:
                tienda_id = x[0]

        tienda_id = str(tienda_id)
        sql = """
        INSERT INTO precios VALUES("""+new_id+""", """+tienda_id+""", """+precio+""");
        """
        cur.execute(sql)
        conn.commit()


    return render_template('add_gpu.html',title='Agregar')

@app.route('/index/add_ram', methods = ['POST' , 'GET'])
def add_ram():
    if request.method == 'POST':
        nombre=request.form['nuevo_ram']
        precio=request.form['precio']
        marca=request.form['marca']
        tienda=request.form['tienda']

        memoria=request.form['memoria']
        frecuencia=request.form['frecuencia']
        formato=request.form['formato']
        latencia=request.form['latencia']
        voltaje=request.form['voltaje']

        sql = """
        select max(id)+1 as maximo from productos;
        """
        cur.execute(sql)
        new_id = cur.fetchall()

        sql = """
        select id from marcas where nombre = '"""+marca+"""';
        """
        cur.execute(sql)
        marca_id = cur.fetchall()

        new_id = str(new_id[0][0])
        marca_id = str(marca_id[0][0])

        sql= """
        INSERT INTO productos VALUES("""+new_id+""",'"""+nombre+"""',"""+marca_id+""",5);
        """
        print(sql)
        cur.execute(sql)
        conn.commit()

        sql="""
        insert into productos_detalle values("""+new_id+""",7,'"""+memoria+"""');
        """
        cur.execute(sql)
        conn.commit()

        sql="""
        insert into productos_detalle values("""+new_id+""",8,'"""+frecuencia+"""');
        """
        cur.execute(sql)
        conn.commit()

        sql="""
        insert into productos_detalle values("""+new_id+""",9,'"""+formato+"""');
        """
        cur.execute(sql)
        conn.commit()

        sql="""
        insert into productos_detalle values("""+new_id+""",10,'"""+latencia+"""');
        """
        cur.execute(sql)
        conn.commit()

        sql="""
        insert into productos_detalle values("""+new_id+""",11,'"""+voltaje+"""');
        """
        cur.execute(sql)
        conn.commit()

        sql = """
        select * from tiendas;
        """
        cur.execute(sql)
        tablatiendas = cur.fetchall()
        tienda_id = 0
        for x in tablatiendas:
            if tienda == x[1]:
                tienda_id = x[0]

        tienda_id = str(tienda_id)
        sql = """
        INSERT INTO precios VALUES("""+new_id+""", """+tienda_id+""", """+precio+""");
        """
        cur.execute(sql)
        conn.commit()


    return render_template('add_ram.html',title='Agregar')

@app.route('/index/delete', methods = ['POST' , 'GET'])
def delete():
    if request.method=='POST':
        delete_nombre = request.form['delete_nombre']
        print(delete_nombre)
        sql ="""
        select id from productos where nombre = '"""+delete_nombre+"""';
        """
        cur.execute(sql)
        id_productos=cur.fetchall()
        print(id_productos)
        print(len(id_productos))
        for x in range(0,len(id_productos)):
            print(id_productos[x][0])
            id_prod=str(id_productos[x][0])
            sql = """
            delete from productos_detalle where producto_id="""+id_prod+""";
            """
            cur.execute(sql)
            conn.commit()
            sql = """
            delete from precios where producto_id="""+id_prod+""";
            """
            cur.execute(sql)
            conn.commit()

        sql = """
        delete from productos where nombre='"""+delete_nombre+"""';
        """
        cur.execute(sql)
        conn.commit()

    return render_template('delete.html',title='Eliminar')
