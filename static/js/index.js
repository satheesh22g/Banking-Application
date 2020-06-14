$(document).ready(function() {

    setTimeout(function() {
        $('.alert').fadeOut('slow');
    }, 5000); // <-- time in milliseconds

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

    $('#cust_ssn_id, #age, #cust_id, #acc_id, #amount').keypress(function(event){
        if(event.which = 8 && isNaN(String.fromCharCode(event.which))){
            event.preventDefault(); //stop character from entering input
        }
    })

    $('#name, #state, #city').keypress(function(event){
        if(!((event.charCode > 64 && event.charCode < 91) || (event.charCode > 96 && event.charCode < 123) || event.charCode==32)){
            event.preventDefault(); //stop character from entering input
        }
    })

    $('#view_cust').validate({
        rules: {
            cust_id: {
                required: '#cust_ssn_id:blank'
            },
            cust_ssn_id: {
                required: '#cust_id:blank'
            }
          }
    })
});