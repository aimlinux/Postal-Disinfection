console.log("これはテストです。"); 
alert("現在テスト中！！"); 


var connection = new WebSocket('wss://echo.websocket.org'); 


btn.addEventListener('click', function(e) {
    var text = document.getElementById("text")
    connection.send('サンプルデータ'); 
})


connection.onmessage = function(e) {
 
    console.log(e.data);
 
};