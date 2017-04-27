function shapes()
{
    var x = document.getElementById("canvas");
    canvas =x.getContext("2d");
    canvas.beginPath();
    canvas.moveTo(50,50);
    canvas.lineTo(50, 60);
    canvas.lineTo(40, 60);
    canvas.closePath();
    canvas.stroke();


/*    var g = canvas.createLinearGradient(10, 10, 100, 200);
    canvas.fillRect(10, 10, 100, 200);
    g.addColorStop(0,"purple");
    g.addColorStop(.5, "white");
    g.addColorStop(1, "yellow");
    canvas.fillStyle = g;
    canvas.fillRect(10, 10, 100, 200);
    canvas.strokeRect(10, 10, 100, 200);
    /!** canvas.fillStyle = "blue";
    canvas.strokeStyle = "blue";


    /!**canvas.clearRect(35, 60, 50, 100); **!/*/
}

window.addEventListener("load", shapes, false)