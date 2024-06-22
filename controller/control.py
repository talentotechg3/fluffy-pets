from flask import render_template, request, jsonify
from database.db import *

# VArible de lista global para almacenar los registros enviados por el formulario
global_data_list = []

def func_home_page():
    return render_template("home.html")
    
def func_register_page():
    return render_template("register.html")

def func_register_user():

    # Se crea variable global para guardar registros en memoria
    global global_data_list
    
    # Capturar datos del formulario
    id      = request.form['id']
    name    = request.form['name']
    email   = request.form['email']
    phone   = request.form['phone']
    petName = request.form['petName']
    pets    = request.form['pets']
    birthday= request.form['birthday']
    
    # Crear un nuevo registro en variable global
    new_data = {
        'id': id,
        'name': name,
        'email': email,
        'phone': phone,
        'petName': petName,
        'pets': pets,
        'birthday': birthday
    }
    
    # Agregar el nuevo registro a la lista global
    global_data_list.append(new_data)
    
    add_user(id, name, email, phone, petName, pets, birthday)

    # Devolver una respuesta JSON
    return jsonify({"message": "Datos guardados exitosamente!"})
    
def func_consult_page():
    return render_template("consult.html")