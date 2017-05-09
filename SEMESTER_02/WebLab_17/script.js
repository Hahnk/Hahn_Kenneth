function drag(){
    mantis = document.getElementById("rock");
    leftbox =document.getElementById("leftbox");

    Rock.addEventListener("dragstart", startDrag, false);

    leftbox.addEventListener("dragenter", function(e){e.preventDefault()}, false);
    leftbox.addEventListener("ddragover", function(e){e.preventDefault()}, false);
    leftbox.addEventListener("drop", drop, false);

}

function startDrag(e) {
    var pic =  '<img id = "rock" src = "https://img.clipartfox.com/b8aa9e2342688c1a5cd910e263e32aa8_3d-big-rock-boulde-rock-3d-clipart_400-400.jpeg">';
    e.dataTransfer.setData("Picture", pic);
}

function drop(e) {
    e.preventDefault();
    leftbox.innerHTML= e.dataTransfer.getData("Picture");
}

window.addEventListener("load", drag, false);