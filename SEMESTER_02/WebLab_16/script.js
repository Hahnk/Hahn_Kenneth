function text()
{
 var x = document.getElementById("canvas");
    canvas = x.getContext("2d");

    canvas.shadowOffsetX = 4;
    canvas.shadowOffsetY = 4;
    canvas.shadowColor = "rgba(0,145,0, .9";
    canvas.shadowBlur = 5;
    canvas.font = "bold 36px Tahoma";
    canvas.textAlign = "end";
    canvas.fillText("robinette", 300, 100);

    canvas.translate(100, 150);
    canvas.fillText("Translated", 300, 100);

    canvas.scale(1.4, 2);
    canvas.fillText("Big Man", 400, 0);

    canvas.rotate(82 * Math.PI/190);
    canvas.fillText("Get twisty", 300, 0);



}

window.addEventListener("load", text, false);
//images