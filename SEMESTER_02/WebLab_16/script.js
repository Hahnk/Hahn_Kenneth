function mouse()
{
 var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    var pic = new Image();
    pic.src = "http://datadragon.com/education/instruments/graphics/tuba.gif";
    pic.addEventListener("load", function() { canvas.drawImage(pic,0,0)}, false);
    window.addEventListener("mousemove", icon, false);
}

 function icon(e) {
     canvas.clearRect(0,0,600,600);
     var xPos = e.clientX;
     var yPos = e.clientY;
     var pic = new Image();
     pic.src = "http://datadragon.com/education/instruments/graphics/tuba.gif";
     pic.addEventListener("load", function() { canvas.drawImage(pic,xPos-50,yPos-50,100,100)}, false);
 }


window.addEventListener("load", mouse, false);

















//
// canvas.shadowOffsetX = 4;
// canvas.shadowOffsetY = 4;
// canvas.shadowColor = "rgba(0,145,0, .9";
// canvas.shadowBlur = 5;
// canvas.font = "bold 36px Tahoma";
// canvas.textAlign = "end";
// canvas.fillText("robinette", 300, 100);
//
// canvas.translate(100, 150);
// canvas.fillText("Translated", 300, 100);
//
// canvas.scale(1.4, 2);
// canvas.fillText("Big Man", 400, 0);
//
// canvas.rotate(82 * Math.PI/190);
// canvas.fillText("Get twisty", 300, 0);
