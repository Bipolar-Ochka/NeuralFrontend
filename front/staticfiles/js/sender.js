var pic = document.getElementById("paint");
var sendbtn = document.getElementById("sendbtn");
sendbtn.onclick = send;

async function send(){
    nani(2);
    let dataURL = canvas.toDataURL();
    let jsonObj = {
        imageBase64: dataURL,
    };
    let response = await fetch('',{
        method: 'POST',
        headers: {
        'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(jsonObj)
    });
    let content = await response.json();
    let result = content['result'];
    fill(result);
}
