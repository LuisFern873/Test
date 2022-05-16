
const dni_admin_input = document.getElementById('dni_admin')
const nombres_input = document.getElementById('nombres')
const apellidos_input = document.getElementById('apellidos')
const correo_input = document.getElementById('correo')
const password_input = document.getElementById('password')
const confirm_password_input = document.getElementById('confirm_password')

document.getElementById('form').onsubmit = function(prevent)
{
    prevent.preventDefault();
    const dni_admin = dni_admin_input.value;
    const nombres = nombres_input.value;
    const apellidos = apellidos_input.value;
    const correo = correo_input.value;
    const password = password_input.value;
    const confirm_password = confirm_password_input.value;

    fetch('/register/register_admin',{
        method: 'POST',
        body: JSON.stringify({
            'dni_admin': dni_admin, 
            'nombres': nombres, 
            'apellidos': apellidos, 
            'correo': correo, 
            'password': password,
            'confirm_password': confirm_password
        }),
        headers: {'Content-Type': 'application/json'}
    })
    .then(response => response.json())
    .then(function(jsonResponse) {
        console.log(jsonResponse);

        if (jsonResponse['mensaje'] === 'success'){
            const nom = document.createElement('nombres'); 
            nom.innerHTML = jsonResponse['nombres'];
            document.getElementById('name').appendChild(nom);
            document.getElementById('welcome').className = "";

            window.location.href="/login";
        } else{
            document.getElementById('changepassword').className = "";
        }
    })
    .catch(function(){
        console.log("Error");
        document.getElementById('error').className = "";
    });
}
