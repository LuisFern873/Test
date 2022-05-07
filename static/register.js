
const dni_admin_input = document.getElementById('dni_admin')
const nombres_input = document.getElementById('nombres')
const apellidos_input = document.getElementById('apellidos')
const correo_input = document.getElementById('correo')
const password_input = document.getElementById('password')
const confirm_password_input = document.getElementById('confirm_password')

document.getElementById('form').onsubmit = function(prevent) {
    prevent.preventDefault();
    const dni_admin = dni_admin_input.value;
    const nombres = nombres_input.value;
    const apellidos = apellidos_input.value;
    const correo = correo_input.value;
    const password = password_input.value;
    const confirm_password = confirm_password_input.value;

    fetch('/register/register_user',{
        method: 'POST',
        body: JSON.stringify({
            'dni_admin': dni_admin, 
            'nombres': nombres, 
            'apellidos': apellidos, 
            'correo': correo, 
            'password': password,
            'confirm_password': confirm_password
        }),
        headers: {'Content-Type': 'application/json'}})
    .then(response => response.json())
    .then(function(jsonResponse) {
        
        document.getElementById('error').className = "alert";
    
        if (jsonResponse['password'] === confirm_password)
        {
            const dni = document.createElement('dni_admin'); 
            const nom = document.createElement('nombres'); 
            const ape = document.createElement('apellidos');
            const cor = document.createElement('correo'); 
            const pass = document.createElement('password'); 
    
            dni.innerHTML = jsonResponse['dni_admin'];
            nom.innerHTML = jsonResponse['nombres'];
            ape.innerHTML = jsonResponse['apellidos'];
            cor.innerHTML = jsonResponse['correo'];
            pass.innerHTML = jsonResponse['password'];

            document.getElementById('name').appendChild(nom);
            document.getElementById('welcome').className = "";

        } else
        {
            document.getElementById('changepassword').className = "";
        }

    })
    .catch(function(){
        console.log("ERROR")
        document.getElementById('error').className = "";
    });
}