function validateUser() {
    var x = document.forms.input.username.value;
    var atPos = x.indexOf("@");
    var dotPos = x.lastIndexOf(".");

    if (atPos < 1 || dotPos < atPos + 2 || dotPos + 2 > x.length)
    {
        alert("Invalid Username");
        return false;
    }
    else
        return true

}

function valpass() {
    var y = document.forms.input.pass.length;

    if(y > 5) {
        return true;
    }
    else {
        alert("Invalid Password");
        return false;
    }

}

function validate() 
{
    var x = document.forms.input.username.value;
    var y = document.forms.input.pass.length;
    if(valpass() == false || validateUser() == false) //if username or password is bad..
    {
        validateUser();
        valpass();
    }
    else
        alert("success")
}