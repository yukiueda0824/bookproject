
$(window).addEventListener('DOMContentLoaded', function(event) {

    let targetElement = document.getElementById('inputPassword');
    let triggerElement = document.getElementById('inputCheckbox');
  
    triggerElement.addEventListener('change', function(event) {
      if ( this.checked ) {
        //targetElement.setAttribute('type', 'text');
        //targetElement.type = "text";
      } else {
        //targetElement.setAttribute('type', 'password');
        //targetElement.type = "password";
      }
    }, false);
  
  }, false);
  