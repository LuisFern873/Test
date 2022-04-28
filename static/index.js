
const fullname_input = document.getElementById('fullname')
const username_input = document.getElementById('username')
const email_input = document.getElementById('email')
const phone_input = document.getElementById('phone')
const password_input = document.getElementById('password')

document.getElementById('form').onsubmit = function(prevent) {
    prevent.preventDefault();
    const fullname = fullname_input.value;
    const username = username_input.value;
    const email = email_input.value;
    const phone = phone_input.value;
    const password = password_input.value;

    fetch('/login/user_added',{
        method: 'POST',
        body: JSON.stringify({'fullname': fullname, 'username': username, 'email': email, 'phone': phone, 'password': password}),
        headers: {'Content-Type': 'application/json'}})
    .then(response => response.json())
    .then(function(jsonResponse) {
        console.log("jsonResponse: ", jsonResponse);
        document.getElementById('error').className = "alert";

        const full = document.createElement('full'); // full name
        const usnm = document.createElement('usnm'); // username
        const eml = document.createElement('eml'); // email
        const phn = document.createElement('phn'); // phone number
        const pass = document.createElement('pass'); // password

        full.innerHTML = jsonResponse['fullname'];
        usnm.innerHTML = jsonResponse['username'];
        eml.innerHTML = jsonResponse['email'];
        phn.innerHTML = jsonResponse['phone'];
        pass.innerHTML = jsonResponse['password'];

        document.getElementById('full').appendChild(full);
        // document.getElementById('u').appendChild(usnm);
        // document.getElementById('e').appendChild(eml);
        // document.getElementById('p').appendChild(phn);
        // document.getElementById('w').appendChild(pass);

        // quitamos la clase y con ello la propiedad display: none
        // De ello, aparece la bienvenida
        document.getElementById('welcome').className = "";
    })
    .catch(function(){
        // quitamos la clase y con ello la propiedad display: none
        // De ello, aparece la alerta
        document.getElementById('error').className = "";
    });
}