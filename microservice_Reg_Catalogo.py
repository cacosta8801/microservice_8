#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, request #import main Flask class and request object
import pika
import MySQLdb
import json
import sys
import time
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import parse_qs
import cgi


class Microservice:
   
    @staticmethod
    def microserviceLogic (nombre,estado,fecha_fin,fecha_inicio):

        try:

            db = MySQLdb.connect(host="35.199.86.113", user="root", passwd="root2018", db="microservice")        
            cur = db.cursor()
            fechaCreacion= time.strftime('%Y-%m-%d')
            cur.execute("INSERT INTO `microservice`.`catalogo` VALUES (null,'"+nombre+"','"+estado+"','"+fecha_fin+"','"+fecha_inicio+"','"+fechaCreacion+"')")
            db.commit()
            
        except IOError as e:
            db.rollback()
            db.close()
            return "Error BD: ".format(e.errno, e.strerror)
            
        db.close() 

        return {"id":str(cur.lastrowid)  ,"nombre": nombre+' '+estado} 

		
app = Flask(__name__)
@app.route('/microservicio/reg_catalogo',methods=['GET', 'POST'])

def registrar_provedor ():

    if request.method == "POST":

      req_data = request.get_json()
      nombre = req_data['nombre']
      estado = req_data['estado']
      fecha_fin = req_data['fecha_fin']
      fecha_inicio = req_data['fecha_inicio']
      
      
      data = Microservice.microserviceLogic(nombre,estado,fecha_fin,fecha_inicio)
      
      response = {} 
      response['catalogo_info'] = "Catalogo "+data["nombre"]+" persistido."
      response['msg'] = 'Hecho'

      return json.dumps(response)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5007)