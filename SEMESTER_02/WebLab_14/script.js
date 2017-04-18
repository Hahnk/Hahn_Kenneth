function validateUser() {
    var x = document.forms.input.username.value;
    var atPos = x.indexOf("@");
    var dotPos = x.lastIndexOf(".");

    if (atPos < 1 || dotPos < atPos + 2 || dotPos + 2 > x.length)
        alert("Invalid Username");


    else
        alert("WELCOME")

}
validateUser();

function valpass() {
    var y = document.forms.input.password.length;
    if(y > 5)
        alert("!");
    else
        alert("Invalid Password");

}
valpass();

function validate() {
    validateUser();
    valpass();
    alert("user");
}