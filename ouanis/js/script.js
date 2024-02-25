document.addEventListener('DOMContentLoaded', () => {

    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
  
    // Add a click event on each of them
    $navbarBurgers.forEach( el => {
      el.addEventListener('click', () => {
  
        // Get the target from the "data-target" attribute
        const target = el.dataset.target;
        const $target = document.getElementById(target);
  
        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        el.classList.toggle('is-active');
        $target.classList.toggle('is-active');
  
      });
    });
  
  });


  $( ".sender" ).on( "click", function() {
    $(".tr").css("display", "none");
    $(".sn").css("display", "block");
    $(".tr").css("transition", "transform 1s");

  } );


  $( ".travler" ).on( "click", function() {
    $(".tr").css("display", "block");
    $(".sn").css("display", "none");
    $(".sn").css("transition", "transform 1s");
    $(".sn").css("transition", "transform 1s");
  } );
