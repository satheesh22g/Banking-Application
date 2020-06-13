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
    });

    $('.reset_btn').click(function(event){
        event.preventDefault();
        $("#cust_ssn_id")[0].value = "";
        $("#name")[0].value = "";
        $("#address")[0].value = "";
        $("#age")[0].value = "";
        $("#state")[0].value = "";
        $("#city")[0].value = "";
    });
});