console.log("scr")
var canvas = document.getElementById("paint");
var resetbutton = document.getElementById("clearbtn");
resetbutton.onclick = reset;
var ctx = canvas.getContext("2d");
var width = canvas.width, height = canvas.height;
var curX, curY, prevX, prevY;
var hold = false;
var fill_value = true, stroke_value = false;
var canvas_data = { "pencil": [], "eraser": [] };
ctx.lineWidth = 10;

function reset (){
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    canvas_data = { "pencil": [], "eraser": [] };
    nani(1);
}

function pencil (){

    canvas.onmousedown = function (e){
        curX = e.clientX - canvas.offsetLeft;
        curY = e.clientY - canvas.offsetTop;
        hold = true;

        prevX = curX;
        prevY = curY;
        ctx.beginPath();
        ctx.moveTo(prevX, prevY);
    };

    canvas.onmousemove = function (e){
        if(hold){
            curX = e.clientX - canvas.offsetLeft;
            curY = e.clientY - canvas.offsetTop;
            draw();
        }
    };

    canvas.onmouseup = function (e){
        hold = false;
    };

    canvas.onmouseout = function (e){
        hold = false;
    };

    function draw (){
        ctx.lineTo(curX, curY);
        ctx.stroke();
        canvas_data.pencil.push({ "startx": prevX, "starty": prevY, "endx": curX, "endy": curY,
            "thick": ctx.lineWidth, "color": ctx.strokeStyle });
    }
}

pencil();
console.log("script_loaded")