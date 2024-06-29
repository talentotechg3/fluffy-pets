function home(){
    window.location = "/";
}

function register(){
    window.location = "/register_page";
}

function consult(){
    cleanData()
    let id_user = document.getElementById("id").value
    let obj_user = {
        "id": id_user,
       // "passw": "12345"
    }
    resp = fetch("/consult_user", {
        "method": "post",
        "headers":{"Content-Type":"application/json"},
        "body":JSON.stringify(obj_user)
    })
    .then(resp => resp.json())
    .then(data => {
        
        //var textarea = document.getElementById("datosRegistrados")
        //textarea.value = JSON.stringify(data, null, 2);
        if (data.status == "ok"){
            var fila = '<tr><td>'+data.id+'</td><td>'+data.usuario+'</td><td>'+data.email+'</td><td>'+data.celular+'</td><td>'+data.nombre_mascota+'</td><td>'+data.tipo_mascota+'</td></tr>';
            document.getElementById("resultData").innerHTML = fila;
            document.getElementById("img-user").src = data.url_file 
        }
        else{
            alert(data.name)
        }
    })
    .catch(err =>{
        alert("Error consulta" + err)
    })
}

function cleanData(){
    document.getElementById("resultData").innerHTML = ""
    document.getElementById("img-user").src = ""
}

/*function consult(){
    
    // Obtener el valor del campo de consulta "numero de documento"
    var id = document.getElementById('id').value;
    
    // Consultar numero de documento usando fetch para consumir backend
    fetch('/consult/'+id, {
        method: 'GET'
    })
    .then(response => response.json())
    .then(data => {
        
        // Mostrar los datos del backend
        var textarea = document.getElementById('datosRegistrados');
        // Formatear JSON
        textarea.value = JSON.stringify(data, null, 2); 
        
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Hubo un error al consultar los datos.');
    });
    
}*/



