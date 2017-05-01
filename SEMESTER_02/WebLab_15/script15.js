function shapes() {
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    canvas.beginPath();
    canvas.moveTo(50,50);
    canvas.lineTo(150,100);
    canvas.lineTo(170,0);
    canvas.lineTo(200,100);
    canvas.lineTo(300,50);
    canvas.lineTo(200,150);
    canvas.lineTo(300,200);
    canvas.lineTo(180,200);
    canvas.lineTo(150,300);
    canvas.lineTo(140,200);
    canvas.lineTo(50,200);
    canvas.lineTo(140,150);
    canvas.closePath();
    canvas.stroke();
    var g = canvas.createLinearGradient(50, 75, 150, 200);
    g.addColorStop(0,"purple");
    g.addColorStop(.75, "white");
    g.addColorStop(1, "yellow");
    canvas.fillStyle = g;
    canvas.fill();
//     canvas.strokeRect(10, 10, 100, 200);
//     canvas.fillStyle = "blue";
//     canvas.strokeStyle = "blue";
//     canvas.clearRect(35, 60, 50, 100); **!
// }
}
window.addEventListener("load", shapes, false);