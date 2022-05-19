

// Código javascript para agregar empleados

const dni_empleado_input = document.getElementById('dni_empleado')
const nombres_input = document.getElementById('nombres')
const apellidos_input = document.getElementById('apellidos')
var genero_input = document.getElementById('male')

document.getElementById('form-add').onsubmit = function(event)
{
    event.preventDefault();
    if(document.getElementById('female').checked) {
        genero_input = document.getElementById('female');
        document.getElementById('mujer').id = "";
    }
    else{
        document.getElementById('hombre').id = "";
    }

    const dni_empleado = dni_empleado_input.value;
    const nombres = nombres_input.value;
    const apellidos = apellidos_input.value;
    const genero = genero_input.value;

    fetch('empleados/new_empleado',{
        method: 'POST',
        body: JSON.stringify({
            'dni_empleado': dni_empleado, 
            'nombres': nombres, 
            'apellidos': apellidos,
            'genero': genero
        }),
        headers: {'Content-Type': 'application/json'}})
    .then(response => response.json())
    .then(function(jsonResponse) 
    {
        console.log(jsonResponse);

        const dni = document.createElement('dni_empleado'); 
        const nom = document.createElement('nombres'); 
        const ape = document.createElement('apellidos');
        const gen = document.createElement('genero');
        
        dni.innerHTML = jsonResponse['dni_empleado'];
        nom.innerHTML = jsonResponse['nombres'];
        ape.innerHTML = jsonResponse['apellidos'];
        gen.innerHTML = jsonResponse['genero'];

        document.getElementById("new_id").appendChild(dni);
        document.getElementById("new_nombres").appendChild(nom);
        document.getElementById("new_apellidos").appendChild(ape);
        document.getElementById('new_genero').appendChild(gen);

        // Aparece el aviso de añadido
        document.getElementById('welcome').className = "";
        // Aparece la nueva ficha de información del empleado
        document.getElementById('new-box').id = "";
        // Quita el formulario
        document.querySelector(".popup-form").classList.remove("active");

        // Limpiamos el formulario
        dni_empleado_input.value = '';
        nombres_input.value = '';
        apellidos_input.value = '';
        document.getElementById("male").checked = false;
        document.getElementById("female").checked = false;
    })
    .catch(function(){
        console.log("Error");
    });
}

// Código javascript para eliminar empleados

const empleados = document.querySelectorAll('.boton-eliminar')

for(let i = 0; i < empleados.length; i++)
{
    const empleado = empleados[i];
    empleado.onclick = function(e){
        console.log("e: ", e);
        const dni_empleado = empleado.getAttribute('id');

        fetch('empleados/delete_empleado/' + dni_empleado,
        {
            method: 'DELETE'
        })
        .then(function(){
            document.getElementById(dni_empleado).style.display = 'none';
            console.log("Delete: ", dni_empleado);
            document.getElementById('eliminar').className = "";
        })
        .catch(function(){
            console.log("Error");
            document.getElementById('error').className = "";
        });
    }
}

// Código javascript para actualizar datos de los empleados

document.getElementById('radio_dni').onclick = function()
{
    document.getElementById('popup-form-edit-dni').style.display = 'block';
    document.getElementById('popup-form-edit-nombres').style.display = 'none';
    document.getElementById('popup-form-edit-apellidos').style.display = 'none';

    // Dentro del formulario Editar, dado que el campo de dni se ha desplegado, este dato es obligatorio
    document.getElementById("nuevo_dni").required = true;
    document.getElementById("nuevos_nombres").required = false;
    document.getElementById("nuevos_apellidos").required = false;

}

document.getElementById('radio_nombres').onclick = function()
{
    document.getElementById('popup-form-edit-dni').style.display = 'none';
    document.getElementById('popup-form-edit-nombres').style.display = 'block';
    document.getElementById('popup-form-edit-apellidos').style.display = 'none';

    document.getElementById("nuevo_dni").required = false;
    document.getElementById("nuevos_nombres").required = true;
    document.getElementById("nuevos_apellidos").required = false;

}

document.getElementById('radio_apellidos').onclick = function()
{
    document.getElementById('popup-form-edit-dni').style.display = 'none';
    document.getElementById('popup-form-edit-nombres').style.display = 'none';
    document.getElementById('popup-form-edit-apellidos').style.display = 'block';

    document.getElementById("nuevo_dni").required = false;
    document.getElementById("nuevos_nombres").required = false;
    document.getElementById("nuevos_apellidos").required = true;
}

const edit_dni_empleado_input = document.getElementById('nuevo_dni')
const edit_nombres_input = document.getElementById('nuevos_nombres')
const edit_apellidos_input = document.getElementById('nuevos_apellidos')

const botones_edit = document.querySelectorAll('.boton-editar')
var dni_empleado = 0

for(let i = 0; i < botones_edit.length; i++)
{
    const boton_edit = botones_edit[i];
    boton_edit.onclick = function(e){
        dni_empleado = boton_edit.getAttribute('id'); // dni del empleado
        console.log(dni_empleado);
    }
}

document.getElementById('form-edit').onsubmit = function(event)
{
    event.preventDefault();
    var edit_dni_empleado = edit_dni_empleado_input.value;
    var edit_nombres = edit_nombres_input.value;
    var edit_apellidos = edit_apellidos_input.value;

    fetch('empleados/update_empleado/' + dni_empleado,{
        method: 'PUT',
        body: JSON.stringify({
            'edit_dni_empleado': edit_dni_empleado, 
            'edit_nombres': edit_nombres, 
            'edit_apellidos': edit_apellidos
        }),
        headers: {'Content-Type': 'application/json'}})
        .then(response => response.json())
        .then(function (jsonResponse){
            const dni = document.createElement('dni_empleado');
            const nom = document.createElement('nombres');
            const ape = document.createElement('apellidos');
            dni.innerHTML = edit_dni_empleado;
            nom.innerHTML = edit_nombres;
            ape.innerHTML = edit_apellidos;
            
            if(edit_dni_empleado !== ""){
                const tag = document.getElementById("edit-dni-" + dni_empleado);
                tag.innerHTML = "DNI: ";
                document.getElementById("edit-dni-" + dni_empleado).appendChild(dni);
            }
            if(edit_nombres !== ""){
                const tag = document.getElementById("edit-nombres-" + dni_empleado);
                tag.innerHTML = "Nombres: ";
                document.getElementById("edit-nombres-" + dni_empleado).appendChild(nom);
            }
            if(edit_apellidos !== ""){
                const tag = document.getElementById("edit-apellidos-" + dni_empleado);
                tag.innerHTML = "Apellidos: ";
                document.getElementById("edit-apellidos-" + dni_empleado).appendChild(ape);
            }
            // Aparece aviso de editado exitosamente
            document.getElementById('success-edit').className = "";
            // Desaparecer el form
            document.querySelector(".popup-form-edit").classList.remove("active");

        }).catch(function(){
            console.log("Error");
        });
}

// Código javascript para asignar tareas a los empleados

const titulo_input = document.getElementById('titulo')
const descripcion_input = document.getElementById('descripcion')

const botones_asignar = document.querySelectorAll('.boton-tarea')
var dni_empleado = 0

for(let i = 0; i < botones_asignar.length; i++)
{
    const boton_asignar = botones_asignar[i];
    boton_asignar.onclick = function(e){
        dni_empleado = boton_asignar.getAttribute('id'); // dni del empleado
        console.log(dni_empleado);
    }
}

document.getElementById('form-task').onsubmit = function(prevent)
{
    prevent.preventDefault();
    const titulo = titulo_input.value;
    const descripcion = descripcion_input.value;

    fetch('/empleados/asignar_tarea/' + dni_empleado,{
        method: 'POST',
        body: JSON.stringify({
            'titulo': titulo,
            'descripcion': descripcion
        }),
        headers: {'Content-Type': 'application/json'}})
    .then(response => response.json())
    .then(function(jsonResponse) 
    {
        console.log(jsonResponse);
        document.querySelector(".popup-form-task").classList.remove("active");
        document.getElementById("success-tarea").className = "";
    })
    .catch(function(){
        console.log("ERROR");
    });
}