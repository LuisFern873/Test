
const fullname_input = document.getElementById('fullname')
const username_input = document.getElementById('username')
const email_input = document.getElementById('email')
const phone_input = document.getElementById('phone')
const password_input = document.getElementById('password')
const cpassword_input = document.getElementById('cpassword')

document.getElementById('form').onsubmit = function(prevent) {
    prevent.preventDefault();
    const fullname = fullname_input.value;
    const username = username_input.value;
    const email = email_input.value;
    const phone = phone_input.value;
    const password = password_input.value;
    const cpassword = cpassword_input.value;

    fetch('/register/user_added',{
        method: 'POST',
        body: JSON.stringify({
            'fullname': fullname, 
            'username': username, 
            'email': email, 
            'phone': phone, 
            'password': password,
            'cpassword': cpassword
        }),
        headers: {'Content-Type': 'application/json'}})
    .then(response => response.json())
    .then(function(jsonResponse) {
        console.log("jsonResponse: ", jsonResponse);
        document.getElementById('error').className = "alert";
    
        if (jsonResponse['password'] === cpassword)
        {
            const full = document.createElement('full'); 
            const usnm = document.createElement('usnm'); 
            const eml = document.createElement('eml');
            const phn = document.createElement('phn'); 
            const pass = document.createElement('pass'); 
            const cpass = document.createElement('cpass'); 
    
            full.innerHTML = jsonResponse['fullname'];
            usnm.innerHTML = jsonResponse['username'];
            eml.innerHTML = jsonResponse['email'];
            phn.innerHTML = jsonResponse['phone'];
            pass.innerHTML = jsonResponse['password'];
            cpass.innerHTML = jsonResponse['cpassword'];

            document.getElementById('name').appendChild(full);
            
            document.getElementById('welcome').className = "";
        } else
        {
            document.getElementById('changepassword').className = "";
        }

    })
    .catch(function(){
        document.getElementById('error').className = "";
    });
}