
document.getElementById("show-form").addEventListener(
    "click", function(){
        document.querySelector(".popup-form").classList.add("active");
    } 
);

document.querySelector(".popup-form .popup .closebtn").addEventListener(
    "click", function(){
        document.querySelector(".popup-form").classList.remove("active");
    } 
);


/* Segundo formulario - Asignar tarea */

const tareas = document.querySelectorAll('.boton-tarea')

for(let i = 0; i < tareas.length; i++)
{
    const tarea = tareas[i];
    tarea.addEventListener(
        "click", function(){
            document.querySelector(".popup-form-task").classList.add("active");
        } 
    )
};

document.querySelector(".popup-form-task .popup .closebtn").addEventListener(
    "click", function(){
        document.querySelector(".popup-form-task").classList.remove("active");
    } 
);


/* Tercer formulario - Editar */

const edits = document.querySelectorAll('.boton-editar')

for(let i = 0; i < edits.length; i++)
{
    const edit = edits[i];
    edit.addEventListener(
        "click", function(){
            document.querySelector(".popup-form-edit").classList.add("active");
        } 
    )
};

document.querySelector(".popup-form-edit .popup .closebtn").addEventListener(
    "click", function(){
        document.querySelector(".popup-form-edit").classList.remove("active");
    } 
);

document.querySelector(".boton-editar-dato").addEventListener(
    "click", function(){
        document.querySelector(".popup-form-edit").classList.remove("active");
    } 
);
 

