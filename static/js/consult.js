
function consult(){
    
    // Obtener el valor del campo de consulta "numero de documento"
    var id = document.getElementById('id').value;
    
    // Consultar nuemro de documento usando fetch para consumir backend
    fetch('/consult/'+id, {
        method: 'GET'
    })
    .then(response => response.json())
    .then(data => {
        
        // Mostrar el datos del backend
        var textarea = document.getElementById('datosRegistrados');
        // Formatear JSON
        textarea.value = JSON.stringify(data, null, 2); 
        
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Hubo un error al consultar los datos.');
    });
    
}



