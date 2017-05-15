function drag(){
    rock = document.getElementById("rock");
    leftbox =document.getElementById("leftbox");

    rock.addEventListener("dragstart", startDrag, false);
    rock.addEventListener("dragend", endDrag, false);

    leftbox.addEventListener("dragenter", dragenter, false);
    leftbox.addEventListener("dragleave", dragleave, false);
    leftbox.addEventListener("dragover", function(e){e.preventDefault()}, false);
    leftbox.addEventListener("drop", drop, false);

}

function startDrag(e) {
    var pic =  '<img id = "rock" src = "https://img.clipartfox.com/b8aa9e2342688c1a5cd910e263e32aa8_3d-big-rock-boulde-rock-3d-clipart_400-400.jpeg">';
    e.dataTransfer.setData("Picture", pic);
}

function dragenter(e) {
    e.preventDefault();
    leftbox.style.background = "pink";
    leftbox.style.border = "3px solid green";
}

function dragleave(e) {
    e.preventDefault();
    leftbox.style.background = "white";
    leftbox.style.border = "3px solid purple";
    
}

function drop(e) {
    e.preventDefault();
    leftbox.innerHTML = e.dataTransfer.getData("Picture");
}

function endDrag(e) {
    pic = e.target;
    pic.style.visibility = "hidden";
}

window.addEventListener("load", drag, false);