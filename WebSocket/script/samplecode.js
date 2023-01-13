
//WebSocket通信を開始する処理
const connection = new WebSocket('通信先のURL');
//URLのはじまりは「ws://」または「wss://」にする必要がある


//通信が開始されたときに実行される処理
connection.onopen = function(e) {
    
}


//サーバーからデータを受信したときに実行される処理
connection.onmessage = function(e) {
//    ※ここに処理を記述
};


//通信が切断された時に実行される処理
connection.onclose = function(e) {
//    ※ここに処理を記述
};


//通信中にエラーが発生した時に実行される処理
connection.onerror = function(e) {
//    ※ここに処理を記述
};

//データをサーバーへ送信する処理
connection.send('送信内容');


//通信を切断する処理
connection.close();

