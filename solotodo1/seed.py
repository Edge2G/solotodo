from configuraciones import *
import psycopg2

conn = psycopg2.connect("dbname = %s user = %s password = %s" % (database, user, passwd))
cur = conn.cursor()

sql= """
INSERT INTO tiendas VALUES(1,'PC Factory');
"""
cur.execute(sql)

sql= """
INSERT INTO tiendas VALUES(2,'SP Digital');
"""
cur.execute(sql)

sql= """
INSERT INTO tiendas VALUES(3,'TT Chile');
"""
cur.execute(sql)

sql= """
INSERT INTO tiendas VALUES(4,'Bip');
"""
cur.execute(sql)

sql= """
INSERT INTO marcas VALUES(1,'Western Digital');
"""
cur.execute(sql)

sql= """
INSERT INTO marcas VALUES(2,'Seagate');
"""
cur.execute(sql)

sql= """
INSERT INTO marcas VALUES(3,'Intel');
"""
cur.execute(sql)

sql= """
INSERT INTO marcas VALUES(4,'AMD');
"""
cur.execute(sql)

sql= """
INSERT INTO marcas VALUES(5,'Nvidia');
"""
cur.execute(sql)

sql= """
INSERT INTO marcas VALUES(6,'Kingston');
"""
cur.execute(sql)

sql= """
INSERT INTO marcas VALUES(7,'Gigabyte');
"""
cur.execute(sql)

sql= """
INSERT INTO categorias VALUES(1,'Disco duro');
"""
cur.execute(sql)

sql= """
INSERT INTO categorias VALUES(2,'Placa madre');
"""
cur.execute(sql)

sql= """
INSERT INTO categorias VALUES(3,'Tarjeta de video');
"""
cur.execute(sql)

sql= """
INSERT INTO categorias VALUES(4,'Procesador');
"""
cur.execute(sql)

sql= """
INSERT INTO categorias VALUES(5,'RAM');
"""
cur.execute(sql)

sql= """
INSERT INTO especificaciones VALUES(1,'Tamano');
"""
cur.execute(sql)

sql= """
INSERT INTO especificaciones VALUES(2,'Rpm');
"""
cur.execute(sql)

sql= """
INSERT INTO especificaciones VALUES(3,'Capacidad');
"""
cur.execute(sql)

sql= """
INSERT INTO especificaciones VALUES(4,'Bufer');
"""
cur.execute(sql)

sql= """
INSERT INTO especificaciones VALUES(5,'Numero de nucleos');
"""
cur.execute(sql)

sql= """
INSERT INTO especificaciones VALUES(6,'Socket');
"""
cur.execute(sql)

sql= """
INSERT INTO especificaciones VALUES(7,'Memoria');
"""
cur.execute(sql)

sql= """
INSERT INTO especificaciones VALUES(8,'Frecuencia');
"""
cur.execute(sql)

sql= """
INSERT INTO especificaciones VALUES(9,'Formato');
"""
cur.execute(sql)

sql= """
INSERT INTO especificaciones VALUES(10,'Latencia');
"""
cur.execute(sql)

sql= """
INSERT INTO especificaciones VALUES(11,'Voltaje');
"""
cur.execute(sql)

sql= """
INSERT INTO productos VALUES(1,'Western Digital Blue 500 GB WD5000LPCX',1,1);
"""
cur.execute(sql)


sql= """
INSERT INTO productos VALUES(6,'Test',1,1);
"""
cur.execute(sql)

sql= """
INSERT INTO productos VALUES(2,'Intel Core i5-7400 (BX80677I57400)',3,4);
"""
cur.execute(sql)

sql= """
INSERT INTO productos VALUES(3,'Kingston HyperX Fury White HX316C10FW/4 (1x4 GB | DIMM DDR3-1600)',6,5);
"""
cur.execute(sql)

sql= """
INSERT INTO productos VALUES(4,'Zotac GTX 1080 (ZT-P10800B-10P)',5,3);
"""
cur.execute(sql)

sql= """
INSERT INTO productos VALUES(5,'Gigabyte GA-AB350M-Gaming 3',7,2);
"""
cur.execute(sql)

sql= """
INSERT INTO precios VALUES(1,1,44000);
"""
cur.execute(sql)

sql= """
INSERT INTO precios VALUES(1,2,39000);
"""
cur.execute(sql)

sql= """
INSERT INTO precios VALUES(2,1,137000);
"""
cur.execute(sql)

sql= """
INSERT INTO precios VALUES(2,3,137000);
"""
cur.execute(sql)

sql= """
INSERT INTO precios VALUES(3,4,27700);
"""
cur.execute(sql)

sql= """
INSERT INTO precios VALUES(4,1,650000);
"""
cur.execute(sql)

sql= """
INSERT INTO precios VALUES(4,2,640000);
"""
cur.execute(sql)

sql= """
INSERT INTO precios VALUES(4,3,580000);
"""
cur.execute(sql)

sql= """
INSERT INTO precios VALUES(5,4,80000);
"""
cur.execute(sql)

sql= """
INSERT INTO productos_detalle VALUES(1,1,'2.5');
"""
cur.execute(sql)

sql= """
INSERT INTO productos_detalle VALUES(6,1,'2.5"');
"""
cur.execute(sql)

sql= """
INSERT INTO productos_detalle VALUES(1,2,'5400');
"""
cur.execute(sql)

sql= """
INSERT INTO productos_detalle VALUES(1,3,'500 GB');
"""
cur.execute(sql)

sql= """
INSERT INTO productos_detalle VALUES(1,4,'16 MB');
"""
cur.execute(sql)

sql= """
INSERT INTO productos_detalle VALUES(2,5,'4');
"""
cur.execute(sql)

sql= """
INSERT INTO productos_detalle VALUES(2,6,'LGA 1151');
"""
cur.execute(sql)

sql= """
INSERT INTO productos_detalle VALUES(3,7,'4 GB');
"""
cur.execute(sql)

sql= """
INSERT INTO productos_detalle VALUES(3,8,'1600 MHz');
"""
cur.execute(sql)

sql= """
INSERT INTO productos_detalle VALUES(3,9,'DIMM');
"""
cur.execute(sql)

sql= """
INSERT INTO productos_detalle VALUES(3,10,'CAS 10');
"""
cur.execute(sql)

sql= """
INSERT INTO productos_detalle VALUES(3,11,'1.5 V');
"""
cur.execute(sql)

sql= """
INSERT INTO productos_detalle VALUES(4,1,'325 mm');
"""
cur.execute(sql)

sql= """
INSERT INTO productos_detalle VALUES(4,7,'8 GB');
"""
cur.execute(sql)

sql= """
INSERT INTO productos_detalle VALUES(4,8,'1771 MHz');
"""
cur.execute(sql)

sql= """
INSERT INTO productos_detalle VALUES(5,6,'AM4');
"""
cur.execute(sql)

sql= """
INSERT INTO productos_detalle VALUES(5,9,'Micro ATX');
"""
cur.execute(sql)

sql= """
INSERT INTO cat_esp VALUES(1,1);
"""
cur.execute(sql)

sql= """
INSERT INTO cat_esp VALUES(1,2);
"""
cur.execute(sql)

sql= """
INSERT INTO cat_esp VALUES(1,3);
"""
cur.execute(sql)

sql= """
INSERT INTO cat_esp VALUES(1,4);
"""
cur.execute(sql)

sql= """
INSERT INTO cat_esp VALUES(2,6);
"""
cur.execute(sql)

sql= """
INSERT INTO cat_esp VALUES(2,9);
"""
cur.execute(sql)

sql= """
INSERT INTO cat_esp VALUES(3,1);
"""
cur.execute(sql)

sql= """
INSERT INTO cat_esp VALUES(3,7);
"""
cur.execute(sql)

sql= """
INSERT INTO cat_esp VALUES(3,8);
"""
cur.execute(sql)

sql= """
INSERT INTO cat_esp VALUES(4,5);
"""
cur.execute(sql)

sql= """
INSERT INTO cat_esp VALUES(4,6);
"""
cur.execute(sql)

sql= """
INSERT INTO cat_esp VALUES(5,7);
"""
cur.execute(sql)

sql= """
INSERT INTO cat_esp VALUES(5,8);
"""
cur.execute(sql)

sql= """
INSERT INTO cat_esp VALUES(5,9);
"""
cur.execute(sql)

sql= """
INSERT INTO cat_esp VALUES(5,10);
"""
cur.execute(sql)

sql= """
INSERT INTO cat_esp VALUES(5,11);
"""
cur.execute(sql)

conn.commit()
cur.close()
conn.close()
