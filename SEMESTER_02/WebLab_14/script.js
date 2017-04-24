function validateUser() {
    var x = document.forms.input.username.value;
    var atPos = x.indexOf("@");
    var dotPos = x.lastIndexOf(".");

    if (atPos < 1 || dotPos < atPos + 2 || dotPos + 2 > x.length)
        alert("Invalid Username");
    else
        return true
        alert("WELCOME");
}

function valpass() {
    var y = document.forms.input.password.length;

    if(y > 5)
        return true
        alert("!");
    else
        alert("Invalid Password");

}

function validate() {
    var x = document.forms.input.username.value;
    var y = document.forms.input.password.length;
    //if username and password are bad...
        //alert "both are bad"
    else if(valpass == true || validateUser == true) //if username or password is bad..
    {
        validateUser();
        valpass();
    }
    else
        alert("success")
}