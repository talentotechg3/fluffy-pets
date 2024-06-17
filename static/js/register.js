function home(){
    window.location = "/";
}

function consult(){
    window.location = "/consult_page";
}

function register(){
    
    // Obtener variables del formulario
    var id = document.getElementById('id').value;
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var phone = document.getElementById('phone').value;
    var petName = document.getElementById('petName').value;
    var pets = document.getElementById('pets').value;
    var birthday = document.getElementById('birthday').value;
    
    // Crear un objeto con los datos del formulario
    var formData = new FormData();
    formData.append('id', id);
    formData.append('name', name);
    formData.append('email', email);
    formData.append('phone', phone);
    formData.append('petName', petName);
    formData.append('pets', pets);
    formData.append('birthday', birthday);

    // Enviar los datos usando fetch para consumir backend
    fetch('/register_user', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        
        // Mostrar el mensaje del backend
        alert(data.message);
        
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Hubo un error al guardar los datos.');
    });
    
}





