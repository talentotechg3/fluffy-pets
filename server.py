from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# VArible de lista global para almacenar los registros enviados por el formulario
global_data_list = []



@app.route("/")
def home_page():
    return render_template("home.html")
    
    
    
@app.route("/register_page")
def register_page():
    return render_template("register.html")
   
    
    
# Endpoint para registrar usuario
@app.route("/register_user", methods=["post"])
def register_user():
    
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

    # Devolver una respuesta JSON
    return jsonify({"message": "Datos guardados exitosamente!"})


@app.route("/consult_page")
def consult_page():
    return render_template("consult.html")

# Endpoint para consultar usuario
@app.route("/consult/<int:id>", methods=["GET"])
def get_data_by_id(id):
    # Acceder a la variable de tipo lista global
    global global_data_list 

    # Buscar el registro por el ID
    for data in global_data_list:
        if data['id'] == str(id):
            return jsonify(data)

    # Si no se encuentra el registro, retornar un mensaje de error
    return jsonify({"message": "Registro no encontrado"}), 404
    


if __name__ == "__main__":
    host = '0.0.0.0'
    port = '8080'
    app.run(host, port)