document.getElementById('form-login').onsubmit = function(prevent){
    prevent.preventDefault();

    fetch('/login/log_admin',{
        method: 'POST',
        body: JSON.stringify({
            'dni_admin_login': document.getElementById("dni_admin_login").value,
            'password_login': document.getElementById("password_login").value
        }),
        headers: {'Content-Type': 'application/json'}})
    .then(response => response.json())
    .then(function(jsonResponse) {
        console.log(jsonResponse);
        

        if(jsonResponse['mensaje'] == '¡Combinación DNI/contraseña inválida!'){
            document.getElementById('error').className = "";
        }
        else{
            window.location.href="/empleados";
        }
        
    })
    .catch(function() {
        console.log("Error");
    });
}