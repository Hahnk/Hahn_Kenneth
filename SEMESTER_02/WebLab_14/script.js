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
    var y = document.forms.input.pass.value;

    if(y.length < 5) {
        alert("Invalid Password");
        return false;
    }
    else {
        return true;
    }
}

function validate()
{
    var x = document.forms.input.username.value;
    var y = document.forms.input.pass.value;
    alert(x);
    alert(y);
    var passRight = new Boolean (valpass());
    var userRight = new Boolean (validateUser());
    if(passRight == false && userRight == false) //if username or password is bad..
    {
        alert("Fix both username and password.");
    }
    else {
        if(passRight == true && userRight == true)
            alert("success");
    }
}

