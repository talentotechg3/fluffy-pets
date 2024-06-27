from flask import render_template, request, jsonify
from database.db import *
from controller.admin_s3 import *

# VArible de lista global para almacenar los registros enviados por el formulario
global_data_list = []

def func_home_page():
    return render_template("home.html")
    
def func_register_page():
    return render_template("register.html")

def func_register_user():
    # Capturar datos del formulario
    id = request.form["id"]
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    petName = request.form["petName"]
    pets = request.form["pets"]
    birthday = request.form["birthday"]
    photo = request.files["photo"]
    print(id, name, petName, pets)
    print(photo.filename) 
    
    # Registrar el usuario en la base de datos
    result_user = add_user(id, name, email, phone, petName, pets, birthday)
    
    if result_user:
       s3_resource = connection_s3()
       photo_path_local = save_file(photo)
       result_file = upload_file(s3_resource, photo_path_local, photo, id)
       if result_file:
           return "<h1>Usuario registrado correctamente</h1>"
       else:
           return "<h1>Usuario registrado sin imagen</h1>"
    else:
       return "<h1>Error registrando usuario</h1>"

"""def func_register_user():

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
    #photo = request.files['photo']
    print(id, name, petName, pets)
    #print(photo.filename) 
    
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
    
    # Registrar el usuario en la base de datos
    result_user = add_user(id, name, email, phone, petName, pets, birthday)"""
    
def func_consult_page():
    return render_template("consult.html")
    
def func_consult_user():
    obj_user = request.get_json()
    id = obj_user["id"]
    print("consultar id:"+id)
    result_data = consult_user(id)
    response = ""
    if result_data != False:
        s3_resource = connection_s3()
        path_file = consult_file(s3_resource, id)
        #print(path_file)
        if path_file != None:
            url_file = "https://bucket-fluffy-pets.s3.us-east-2.amazonaws.com/" + path_file
        else:
            url_file = "Sin imágen cargada"
        response = {
            'status': "ok",
            'Tipo mascota': result_data[0][5],
            'Nombre mascota': result_data[0][4],
            'Celular': result_data[0][3],
            'email': result_data[0][2],
            'usuario': result_data[0][1],
            'id': result_data[0][0],
            'url_file': url_file
        }
    else:
        response = {
            'status': "error",
            'name': "Usuario no encontrado"
        }
    print (response)
    return response
    