$(document).ready(function(){
    $("#submitBtn").click(function(){
        if ($("#id_email").val() !== $("#id_verify_email").val()) {
            alert("Please make sure Email and Confirm Email match!");
        }
    });
});