
static async Task Run()
{
    //Httpリスナーを立ち上げ、クライアントからの接続を待つ
    HttpListener s = new HttpListener();
    s.Prefixes.Add("http://localhost:8000/ws/");
    s.Start();
    var hc = await s.GetContextAsync();

    //クライアントからのリクエストがWebSocketでない場合は処理を中断
    if (!hc.Request.IsWebSocketRequest)
    {
        //クライアント側にエラー(400)を返却し接続を閉じる
        hc.Response.StatusCode = 400;
        hc.Response.Close();
        return;
    }

    //WebSocketでレスポンスを返却
    var wsc = await hc.AcceptWebSocketAsync(null);
    var ws = wsc.WebSocket;

    //１０回のレスポンスを返却
    for (int i = 0; i != 10; ++i)
    {
        //1回のレスポンスごとに2秒のウエイトを設定
        await Task.Delay(2000);

        //レスポンスのテストメッセージとして、現在時刻の文字列を取得
        var time = DateTime.Now.ToLongTimeString();

        //文字列をByte型に変換
        var buffer = Encoding.UTF8.GetBytes(time);
        var segment = new ArraySegment<byte>(buffer);

        //クライアント側に文字列を送信
        await ws.SendAsync(segment, WebSocketMessageType.Text,
          true, CancellationToken.None);
    }

    //接続を閉じる
    await ws.CloseAsync(WebSocketCloseStatus.NormalClosure,
      "Done", CancellationToken.None);
}
