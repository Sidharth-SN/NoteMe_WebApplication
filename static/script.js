
var myModal = document.getElementById('myModal')
var myInput = document.getElementById('myInput')

myModal.addEventListener('shown.bs.modal', function () {
  myInput.focus()
})


function myFunction() {

  var x = document.getElementById("snackbar");
  x.className = "show";
  setTimeout(function(){ 
    x.className = x.className.replace("show", ""); 
  }, 3000);
} 


document.getElementById('frmSearch').onsubmit = function() {
  window.location = 'http://www.google.com/' + document.getElementById('txtSearch').value;
  return false;
}
