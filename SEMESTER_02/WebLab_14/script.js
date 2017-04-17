/**
 * Created by hahnk7862 on 4/7/2017.
 */
function validate() {
    var x = document.forms.input.username.value;
    var atPos = x.indexOf("@");
    var dotPos = x.lastIndexOf(".");

    if (atPos < 1 || dotPos < atPos + 2 || dotPos + 2 > x.length)
        alert("Invalid Username");


    else
        alert("WELCOME")

}
validate()
