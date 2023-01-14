var segundos = 0;
function contarSegundos(){
    segundos +=1;
}

setInterval(contarSegundos, 10000);

function redirectpage(){
    window.location="{% url 'ventas/medioPago' %}";
}