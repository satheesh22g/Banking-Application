$(document).ready(function() {

    setTimeout(function() {
        $('.alert').fadeOut('slow');
    }, 2000); // <-- time in milliseconds

    $('#showPass').click(function(){
        var x = $("#passwordInput")[0]
        if (x.type === "password") {
            x.type = "text";
        } else {
            x.type = "password";
        }
    })
});