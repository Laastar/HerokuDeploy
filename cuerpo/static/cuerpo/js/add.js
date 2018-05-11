$(document).ready(function(){
    $('.sidenav').sidenav();
 	$('.slider').slider();
 	$('.carousel').carousel();
    $('.parallax').parallax();
    $('select').formSelect();
 });

function Ejecuta() {
 	alert("Mensaje enviado, Tus comentarios nos ayudan a seguir creciendo")
 }

 function Finalizar() {
 	alert("Tu cita se ha registrado gracias por tu preferencia")
 }

 function Registro() {
 	alert("Registro exitoso, Gracias por tu preferencia")
 	document.location.href=index.html;
 }