

const botones_completo = document.querySelectorAll('.completo')
var id = 0

for(let i = 0; i < botones_completo.length; i++)
{
    const boton_completo = botones_completo[i];
    boton_completo.onclick = function(e){
        id = boton_completo.getAttribute('id'); // dni del empleado
        
        fetch('/tareas/update_tarea/' + id,{
            method: 'PUT'
        })
        .then(function(){
            document.getElementById(id).style.display = 'none';
        });
    }
}