const dni_admin_input = document.getElementById("dni_admin_login")
const password_input = document.getElementById("password_login")

document.getElementById('form-login').onsubmit = function(prevent){
    prevent.preventDefault();

    const dni_admin = dni_admin_input.value;
    const password = password_input.value;

    console.log(dni_admin);
    console.log(password);

    fetch('/login/log_admin',{
        method: 'POST',
        body: JSON.stringify({
            'dni_admin_login': dni_admin,
            'password_login': password
        }),
        headers: {'Content-Type': 'application/json'}})
    .then(response => response.json())
    .then(function(jsonResponse) {
        console.log(jsonResponse);
        window.location.href = "http://127.0.0.1:5000/empleados";
    })
    .catch(function() {
        console.log("Error");
        document.getElementById('error').className = "";
    });
}
