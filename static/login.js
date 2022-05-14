const dni_admin_input = document.getElementById('dni_admin')
const password_input = document.getElementById('password')

document.getElementById('form').onsubmit = function(prevent)
{
    prevent,preventDefault();
    const dni_admin = dni_admin_input.value;
    const password = password_input.value;

    fetch('login/log_user',{
        method : "GET",
        body: JSON.stringify({
            'dni_admin' : dni_admin,
            'password' : password,
        }),
        headers: {'Content-Type': 'application/json'}})
    .then(response => response.json())
    
}
