
from controller.control import *
from server import app

@app.route("/")
def home_page():
    return func_home_page()
    
@app.route("/register_page")
def register_page():
    return func_register_page()
   
# Endpoint para registrar usuario
@app.route("/register_user", methods=["post"])
def register_user():
    return func_register_user()

@app.route("/consult_page")
def consult_page():
    return func_consult_page()

# Endpoint para consultar usuario
@app.route("/consult_user", methods=["post"])
def consult_user():
    return func_consult_user()
    
"""@app.route("/consult/<int:id>", methods=["GET"])
def get_data_by_id(id):
    # Acceder a la variable de tipo lista global
    global global_data_list 

    # Buscar el registro por el ID
    for data in global_data_list:
        if data['id'] == str(id):
            return jsonify(data)

    # Si no se encuentra el registro, retornar un mensaje de error
    return jsonify({"message": "Registro no encontrado"}), 404"""