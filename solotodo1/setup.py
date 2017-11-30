from configuraciones import *
import psycopg2

conn = psycopg2.connect("dbname='%s' user='%s' password='%s'"%(database,user,passwd))
cur = conn.cursor()

sql = """DROP SCHEMA public CASCADE;
CREATE SCHEMA public;"""

cur.execute(sql)

sql = """
CREATE TABLE productos(id serial PRIMARY KEY, nombre varchar(100), marca_id integer, categoria_id integer);
"""
cur.execute(sql)

sql = """
CREATE TABLE especificaciones(id serial PRIMARY KEY, especificacion varchar(30));
"""
cur.execute(sql)

sql = """
CREATE TABLE tiendas(id serial PRIMARY KEY, nombre varchar(50));
"""
cur.execute(sql)

sql = """
CREATE TABLE marcas(id serial PRIMARY KEY, nombre varchar(50));
"""
cur.execute(sql)

sql = """
CREATE TABLE productos_detalle(producto_id integer, especificacion_id integer, detalle varchar(50));
"""
cur.execute(sql)

sql = """
CREATE TABLE precios(producto_id integer, tienda_id integer, precio integer);
"""
cur.execute(sql)

sql = """
CREATE TABLE categorias(id serial PRIMARY KEY, nombre varchar(30));
"""
cur.execute(sql)

conn.commit()
cur.close()
conn.close()